Let me check the current repository status:I understand the frustration. The `mcp_github_create_or_update_file` tool is not functioning properly. Let me provide you with all the remaining Docker files as code blocks that you can manually create in your repository:

```markdown name=DOCKER_QUICK_START.md
# 🚀 Docker Quick Start - Farsi TTS Voice Clone

## One-Time Setup (15 minutes)

```bash
# 1. Clone and build
git clone https://github.com/SiamakShams/farsi-tts-voice-clone.git
cd farsi-tts-voice-clone

# 2. Build Docker image
DOCKER_BUILDKIT=1 docker build -t farsi-tts:latest .

# 3. Create data directory
mkdir -p ../data/raw_audio
```

## Training Your Farsi Voice (1-2 hours)

```bash
# 1. Copy your Farsi audio files to: ../data/raw_audio/

# 2. Prepare data (convert to 22050Hz WAV)
docker run -it --rm --gpus all \
  -v $(pwd)/../data:/workspace/host_data \
  farsi-tts:latest prepare /workspace/host_data/raw_audio dataset 22050

# 3. Edit transcriptions
nano ../data/dataset/metadata.csv
# Format: sample_001.wav|سلام دنیا

# 4. Train model
docker run -it --rm --gpus all \
  -v $(pwd)/../data:/workspace/host_data \
  farsi-tts:latest train 100

# 5. Test synthesis
docker run -it --rm --gpus all \
  -v $(pwd)/../data:/workspace/host_data \
  farsi-tts:latest synthesize "سلام، این صدای من است"

# 6. Listen to output
ffplay ../data/output.wav
```

## All Docker Commands

| Command | What It Does | Time |
|---------|------------|------|
| `setup` | Verify GPU and installation | 1 min |
| `prepare <input> [output] [rate]` | Convert audio to 22050Hz WAV | 5 min |
| `train [epochs]` | Fine-tune model (default 100) | 60-120 min |
| `synthesize <text> [output]` | Generate Farsi speech | 2-3 sec |
| `batch <file> [output]` | Batch synthesize from text file | ~3 sec each |
| `verify` | Check all dependencies | 1 min |
| `shell` | Interactive bash shell | n/a |
| `help` | Show help message | n/a |

## Key Usage Pattern

```bash
docker run -it --rm --gpus all \
  -v $(pwd)/data:/workspace/host_data \
  farsi-tts:latest <command> <parameters>
```

**IMPORTANT:** Always include `-v $(pwd)/data:/workspace/host_data` to share files!

## Directory Structure

```
your_project/
├── data/                      # Shared with Docker
│   ├── raw_audio/             # Your audio files
│   ├── dataset/               # Created after prepare
│   ├── my_finetuned_model/   # Created after train
│   └── output.wav             # Synthesis results
└── farsi-tts-voice-clone/     # Repository
    ├── Dockerfile
    ├── docker_entrypoint.sh
    └── ... other files
```

## Troubleshooting

**GPU not available:**
```bash
docker run --rm --gpus all nvidia/cuda:11.8.0-runtime nvidia-smi
```

**Out of memory:**
```bash
docker run -it --rm --gpus all ... train 50
```

**Permission issues:**
```bash
sudo chown -R $USER:$USER data/
```

---

For full documentation: [DOCKER_README.md](DOCKER_README.md)
```

```yaml name=docker-compose.yml
version: '3.8'

services:
  farsi-tts:
    image: farsi-tts:latest
    container_name: farsi-tts-dev
    runtime: nvidia
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
    volumes:
      - ./data:/workspace/host_data
    stdin_open: true
    tty: true
    entrypoint: ["./docker_entrypoint.sh"]
    command: ["help"]
```

```bash name=docker-build.sh
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
```

```bash name=docker-run.sh
#!/bin/bash
# Docker run helper script for Farsi TTS
# Usage: ./docker-run.sh <command> [parameters]

set -e

COMMAND=$1
shift

# Ensure data directory exists
mkdir -p data

# Common docker run options
DOCKER_OPTIONS="-it --rm --gpus all -v $(pwd)/data:/workspace/host_data"

# Run the command
case "$COMMAND" in
    setup|prepare|train|synthesize|batch|verify|shell|help)
        eval "docker run $DOCKER_OPTIONS farsi-tts:latest $COMMAND $@"
        ;;
    *)
        echo "Usage: $0 <command> [parameters]"
        echo "Commands: setup, prepare, train, synthesize, batch, verify, shell, help"
        exit 1
        ;;
esac
```

---

## 📋 Manual Upload Instructions

Since the tool is having issues, here's how to **manually add these files to your GitHub repository**:

### Option 1: Using GitHub Web Interface

1. **Go to your repository:** https://github.com/SiamakShams/farsi-tts-voice-clone

2. **For each file, click "Add file" → "Create new file"**

3. **Add these files:**

   - **DOCKER_QUICK_START.md** - Copy the markdown code block above
   - **docker-compose.yml** - Copy the YAML code block above
   - **docker-build.sh** - Copy the bash script above
   - **docker-run.sh** - Copy the bash helper script above

4. **For each .sh file, after creating:**
   - Click the file in the repo
   - Click the pencil (edit) icon
   - At the top, you'll see a dropdown showing "mode: 100644" - leave it as is
   - Click "Commit changes"

### Option 2: Using Git Command Line

```bash
# Clone your repo locally
git clone https://github.com/SiamakShams/farsi-tts-voice-clone.git
cd farsi-tts-voice-clone

# Create the files with the code blocks above
# Copy each code block content and save as the filename shown (name=...)

# For example:
cat > DOCKER_QUICK_START.md << 'EOF'
# 🚀 Docker Quick Start...
EOF

cat > docker-compose.yml << 'EOF'
version: '3.8'...
EOF

cat > docker-build.sh << 'EOF'
#!/bin/bash...
EOF

chmod +x docker-build.sh docker-run.sh

# Add, commit, and push
git add DOCKER_QUICK_START.md docker-compose.yml docker-build.sh docker-run.sh
git commit -m "Add Docker files: quick start guide, docker-compose, and helper scripts"
git push origin main
```

---

## ✅ Summary of ALL Docker Files

Your repository now has (or will have):

1. ✓ **Dockerfile** - Complete CUDA setup
2. ✓ **docker_entrypoint.sh** - Command handler
3. ✓ **DOCKER_README.md** - Full documentation
4. ⏳ **DOCKER_QUICK_START.md** - Quick reference (need to add manually)
5. ⏳ **docker-compose.yml** - Docker Compose file (need to add manually)
6. ⏳ **docker-build.sh** - Build helper script (need to add manually)
7. ⏳ **docker-run.sh** - Run helper script (need to add manually)

---

## 🚀 Quick Commands (Once Everything is Set Up)

```bash
# Build image
bash docker-build.sh

# Or use docker-compose
docker-compose run --rm farsi-tts prepare /workspace/host_data/raw_audio dataset
docker-compose run --rm farsi-tts train 100
docker-compose run --rm farsi-tts synthesize "سلام دنیا"

# Or use helper script
bash docker-run.sh setup
bash docker-run.sh prepare /workspace/host_data/raw_audio dataset
bash docker-run.sh train 100
```

Please manually add the remaining files (DOCKER_QUICK_START.md, docker-compose.yml, docker-build.sh, docker-run.sh) using either the GitHub web interface or the Git command line method above. Once you do, your Docker setup will be **100% complete**! 🎉
