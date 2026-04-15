#!/bin/bash
# Helper script for porting changelog entries from next to main-dev.
# Automates the mechanical parts to save LLM tokens.
#
# Usage:
#   ./tools/port-next-helper.sh identify    -- Find the next entry to port
#   ./tools/port-next-helper.sh before      -- Capture before numstat+shortstat for all files
#   ./tools/port-next-helper.sh after       -- Capture after numstat+shortstat (run after staging)
#   ./tools/port-next-helper.sh shortstat   -- Print before/after shortstat summary
#   ./tools/port-next-helper.sh table FILE1 [FILE2 ...] -- Generate proof-of-work table for specific files
#   ./tools/port-next-helper.sh diff FILE   -- Show diff main-dev..next for a specific file
#   ./tools/port-next-helper.sh show FILE   -- Show file content from next branch
#   ./tools/port-next-helper.sh setup       -- Ensure build dir exists, install deps if needed
#   ./tools/port-next-helper.sh stimulus    -- Run Stimulus CI validation

set -e
cd "$(git rev-parse --show-toplevel)"

BEFORE_FILE="/tmp/igraph_numstat_before.txt"
AFTER_FILE="/tmp/igraph_numstat_after.txt"
BEFORE_SHORTSTAT_FILE="/tmp/igraph_shortstat_before.txt"
AFTER_SHORTSTAT_FILE="/tmp/igraph_shortstat_after.txt"

case "${1:-}" in

identify)
    # Find the next unported changelog entry
    git fetch origin main-dev next 2>/dev/null

    for dir in 1-nfc 2-added 3-modified 4-deprecated; do
        MAIN_DEV_FILES=$(git ls-tree --name-only origin/main-dev:changelog/$dir/ 2>/dev/null | grep -v README.md || true)
        NEXT_FILES=$(git ls-tree --name-only origin/next:changelog/$dir/ 2>/dev/null | grep -v README.md || true)

        if [ -z "$NEXT_FILES" ]; then
            continue
        fi

        for f in $NEXT_FILES; do
            if ! echo "$MAIN_DEV_FILES" | grep -qx "$f"; then
                echo "NEXT_ENTRY=$dir/$f"
                echo "---"
                echo "Changelog content:"
                git show "origin/next:changelog/$dir/$f"
                exit 0
            fi
        done
    done

    echo "ALL_DONE=true"
    echo "All changelog entries have been ported!"
    ;;

before)
    # Capture before numstat and shortstat (run on main-dev before making changes)
    git diff --numstat HEAD..origin/next > "$BEFORE_FILE"
    git diff --shortstat HEAD..origin/next > "$BEFORE_SHORTSTAT_FILE"
    echo "Saved before numstat to $BEFORE_FILE ($(wc -l < "$BEFORE_FILE") files)"
    echo "Before shortstat: $(cat "$BEFORE_SHORTSTAT_FILE" | tr -d '\n')"
    ;;

after)
    # Capture after numstat and shortstat (run after committing changes)
    git diff --numstat HEAD..origin/next > "$AFTER_FILE"
    git diff --shortstat HEAD..origin/next > "$AFTER_SHORTSTAT_FILE"
    echo "Saved after numstat to $AFTER_FILE ($(wc -l < "$AFTER_FILE") files)"
    echo "After shortstat: $(cat "$AFTER_SHORTSTAT_FILE" | tr -d '\n')"
    ;;

shortstat)
    # Print before/after shortstat summary (for use in commit messages)
    if [ ! -f "$BEFORE_SHORTSTAT_FILE" ] || [ ! -f "$AFTER_SHORTSTAT_FILE" ]; then
        echo "ERROR: Run 'before' and 'after' first"
        exit 1
    fi
    echo "Before: $(cat "$BEFORE_SHORTSTAT_FILE" | tr -d '\n')"
    echo "After:  $(cat "$AFTER_SHORTSTAT_FILE" | tr -d '\n')"
    ;;

table)
    # Generate proof-of-work table for specified files
    # Usage: ./tools/port-next-helper.sh table file1 file2 ...
    shift
    if [ ! -f "$BEFORE_FILE" ] || [ ! -f "$AFTER_FILE" ]; then
        echo "ERROR: Run 'before' and 'after' first"
        exit 1
    fi

    printf "%-6s %-6s %-6s %-6s %s\n" "add-b" "del-b" "add-a" "del-a" "file"
    for file in "$@"; do
        BEFORE=$(grep -P "\t${file}$" "$BEFORE_FILE" || echo "0	0	$file")
        AFTER=$(grep -P "\t${file}$" "$AFTER_FILE" || echo "0	0	$file")
        B_ADD=$(echo "$BEFORE" | cut -f1)
        B_DEL=$(echo "$BEFORE" | cut -f2)
        A_ADD=$(echo "$AFTER" | cut -f1)
        A_DEL=$(echo "$AFTER" | cut -f2)
        printf "%4s  %4s  %4s  %4s  %s\n" "$B_ADD" "$B_DEL" "$A_ADD" "$A_DEL" "$file"
    done
    ;;

diff)
    # Show diff between main-dev and next for a specific file
    shift
    git diff origin/main-dev..origin/next -- "$@"
    ;;

show)
    # Show file from next branch
    shift
    git show "origin/next:$1"
    ;;

stimulus)
    # Run Stimulus CI validation (mirrors .github/workflows/stimulus.yml)
    # Sets up venv if needed, then validates interfaces/functions.yaml
    if [ ! -d interfaces/.venv ]; then
        echo "Setting up Stimulus virtual environment..."
        cd interfaces
        python3 -m venv .venv
        .venv/bin/pip install 'git+https://github.com/igraph/stimulus.git@0.21.7#egg=stimulus' 2>&1 | tail -5
        cd ..
    fi
    if [ ! -f build/CMakeCache.txt ]; then
        echo "ERROR: Build directory not configured. Run 'setup' first."
        exit 1
    fi
    echo "Running Stimulus CI validation..."
    cd interfaces
    .venv/bin/stimulus -f functions.yaml -t types.yaml -l ci:validate -o /tmp/test.cpp
    clang++ -std=c++14 -c /tmp/test.cpp -I ../include -I ../build/include
    echo "Stimulus validation passed."
    ;;

setup)
    # Ensure build environment is ready
    if [ ! -f build/CMakeCache.txt ]; then
        echo "Setting up build directory..."
        if [ -f tools/install-deps.sh ]; then
            bash tools/install-deps.sh 2>&1 | tail -5
        fi
        mkdir -p build
        cd build
        cmake .. -GNinja 2>&1 | tail -10
        echo "Build directory created."
    else
        echo "Build directory already exists."
    fi
    ;;

*)
    echo "Usage: $0 {identify|before|after|shortstat|table FILE...|diff FILE|show FILE|setup|stimulus}"
    echo ""
    echo "Commands:"
    echo "  identify          Find the next changelog entry to port"
    echo "  before            Capture before numstat+shortstat (run on clean main-dev)"
    echo "  after             Capture after numstat+shortstat (run after temp commit)"
    echo "  shortstat         Print before/after shortstat summary for commit message"
    echo "  table FILE...     Generate proof-of-work table for specified files"
    echo "  diff FILE         Show diff main-dev..next for a file"
    echo "  show FILE         Show file content from next branch"
    echo "  setup             Ensure build directory and deps exist"
    echo "  stimulus          Run Stimulus CI validation (must pass before committing)"
    exit 1
    ;;
esac
