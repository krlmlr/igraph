#!/usr/bin/env bash
# Install build and test dependencies for igraph on Debian/Ubuntu systems.
# Usage: bash tools/install-deps.sh
set -euo pipefail

if ! command -v apt-get &>/dev/null; then
  echo "This script requires apt-get (Debian/Ubuntu). Install dependencies manually:" >&2
  echo "  cmake (>=3.18), ninja-build, gcc, g++, flex, bison" >&2
  exit 1
fi

sudo apt-get update -y

packages=(libxml2-dev)

if ! command -v cmake &>/dev/null; then
  packages+=("cmake")
fi

if ! command -v ninja &>/dev/null; then
  packages+=("ninja-build")
fi

if ! command -v gcc &>/dev/null; then
  packages+=("gcc")
fi

if ! command -v g++ &>/dev/null; then
  packages+=("g++")
fi

if ! command -v flex &>/dev/null; then
  packages+=("flex")
fi

if ! command -v bison &>/dev/null; then
  packages+=("bison")
fi

if ! command -v ccache &>/dev/null; then
  packages+=("ccache")
fi

sudo apt-get install -y "${packages[@]}"

echo "All dependencies installed."
