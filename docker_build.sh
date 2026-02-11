#!/bin/bash
# Docker setup and build script for Farsi TTS
# This script builds the Docker image and performs initial setup

set -e

echo "🐳 Farsi TTS Voice Clone - Docker Setup"
echo "========================================"
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed."
    echo "Please install Docker from: https://docs.docker.com/get-docker/"
    exit 1
fi

echo "✓ Docker version: $(docker --version)"
echo ""

# Check if NVIDIA Docker is installed
echo "Checking for NVIDIA Container Runtime..."
if docker run --rm --gpus all nvidia/cuda:11.8.0-runtime-ubuntu22.04 nvidia-smi > /dev/null 2>&1; then
    echo "✓ NVIDIA Container Runtime is available"
else
    echo "⚠ NVIDIA Container Runtime not found"
    echo "For GPU support, install from:"
    echo "https://github.com/NVIDIA/nvidia-docker"
    echo ""
fi

echo ""
echo "Building Docker image..."
echo "This will take 10-15 minutes on first build..."
echo ""

# Build image with BuildKit
DOCKER_BUILDKIT=1 docker build -t farsi-tts:latest .

echo ""
echo "✅ Docker image built successfully!"
echo ""
echo "Image size:"
docker images farsi-tts:latest --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"
echo ""
echo "Next steps:"
echo "1. Create data directory: mkdir -p ../data/raw_audio"
echo "2. Verify setup: docker run -it --rm --gpus all -v \$(pwd)/../data:/workspace/host_data farsi-tts:latest setup"
echo "3. See DOCKER_QUICK_START.md for usage examples"
echo ""
