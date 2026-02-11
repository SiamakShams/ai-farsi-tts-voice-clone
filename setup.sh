#!/bin/bash
# setup.sh - Complete installation and setup for Farsi TTS Voice Cloning

set -e

echo "🚀 Farsi TTS Voice Clone - Complete Setup"
echo "============================================"
echo ""

echo "📌 Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✓ Python version: $PYTHON_VERSION"

echo ""
echo "📌 Creating virtual environment..."
if [ -d "tts-env" ]; then
    echo "✓ Virtual environment already exists"
else
    python3 -m venv tts-env
    echo "✓ Virtual environment created"
fi

echo ""
echo "📌 Activating virtual environment..."
source tts-env/bin/activate
echo "✓ Virtual environment activated"

echo ""
echo "📌 Upgrading pip..."
pip install --upgrade pip setuptools wheel

echo ""
echo "📌 Installing PyTorch with CUDA support..."
pip install torch torchaudio torchvision --index-url https://download.pytorch.org/whl/cu118

echo ""
echo "📌 Installing Coqui TTS and dependencies..."
pip install -r requirements.txt

echo ""
echo "📌 Downloading multilingual VITS model..."
python3 << 'EOFPYTHON'
from TTS.utils.manage import ModelManager
m = ModelManager()
m.download_model('tts_models/multilingual/multi-dataset/vits')
print("✓ Model downloaded successfully")
EOFPYTHON

echo ""
echo "📌 Creating dataset directories..."
mkdir -p dataset/wavs
mkdir -p raw_audio
mkdir -p my_finetuned_model
mkdir -p batch_output

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Place audio files in raw_audio/"
echo "2. Run: python3 prepare_data.py --input_dir raw_audio --output_dir dataset"
echo "3. Edit: dataset/metadata.csv with Farsi transcriptions"
echo "4. Train: bash train.sh"
echo "5. Synthesize: bash synthesize.sh 'متن فارسی'"