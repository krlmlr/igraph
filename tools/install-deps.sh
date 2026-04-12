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
sudo apt-get install -y \
  cmake \
  ninja-build \
  gcc \
  g++ \
  flex \
  bison \
  libxml2-dev \
  ccache

echo "All dependencies installed."
