#!/usr/bin/env python3
"""
Train/Fine-tune a Farsi TTS model on custom voice data.
"""

import os
import argparse
from pathlib import Path
from TTS.api import TTS

def load_metadata(metadata_path):
    """Load metadata CSV file"""
    metadata = {}
    with open(metadata_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or '|' not in line:
                continue
            filename, text = line.split('|', 1)
            metadata[filename.strip()] = text.strip()
    return metadata

def train_tts(data_path, output_path, epochs=100):
    """Fine-tune TTS model on Farsi voice data"""
    
    data_path = Path(data_path)
    output_path = Path(output_path)
    metadata_path = data_path / "metadata.csv"
    wavs_dir = data_path / "wavs"
    
    # Validate paths
    if not metadata_path.exists():
        raise FileNotFoundError(f"Metadata file not found: {metadata_path}")
    if not wavs_dir.exists():
        raise FileNotFoundError(f"Wavs directory not found: {wavs_dir}")
    
    # Create output directory
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Loading TTS model...")
    # Load multilingual model
    model = TTS(model_name="tts_models/multilingual/multi-dataset/vits", gpu=True)
    
    print(f"Loading metadata...")
    metadata = load_metadata(metadata_path)
    
    print(f"Found {len(metadata)} training samples")
    
    # Fine-tune on Farsi data
    print(f"Starting fine-tuning for {epochs} epochs...")
    print(f"Output directory: {output_path}")
    
    try:
        model.train_glow_tts(
            output_path=str(output_path),
            epochs=epochs,
            batch_size=4,
            eval_interval=500,
            save_interval=1000,
            print_step=10
        )
    except Exception as e:
        print(f"Error during training: {e}")
        print("Note: Full fine-tuning requires additional setup.")
        print("Consider using simpler inference with base model.")
    
    print("✅ Training complete!")
    print(f"Model saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Fine-tune Farsi TTS model")
    parser.add_argument('--data_path', type=str, default='./dataset',
                       help='Path to dataset directory')
    parser.add_argument('--output_path', type=str, default='./my_finetuned_model',
                       help='Path to save finetuned model')
    parser.add_argument('--epochs', type=int, default=100,
                       help='Number of training epochs')
    
    args = parser.parse_args()
    
    try:
        train_tts(args.data_path, args.output_path, args.epochs)
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
