#!/bin/bash
# synthesize.sh - Generate speech in trained voice

set -e

# Activate virtual environment if it exists
if [ -d "tts-env" ]; then
    source tts-env/bin/activate
fi

# Get text from argument
TEXT="${1:-سلام دنیا}"
OUTPUT="${2:-output.wav}"

# Check model exists
if [ ! -f "my_finetuned_model/best_model.pth" ]; then
    echo "❌ Model not found. Run 'bash train.sh' first."
    exit 1
fi

echo "🎤 Synthesizing: $TEXT"
echo "Output: $OUTPUT"
echo ""

python3 synthesize.py \
    --text "$TEXT" \
    --model_path my_finetuned_model/best_model.pth \
    --config_path my_finetuned_model/config.json \
    --output_path "$OUTPUT"

echo ""
echo "✅ Synthesis complete!"
echo "Output saved to: $OUTPUT"
echo "Play audio: ffplay $OUTPUT"
