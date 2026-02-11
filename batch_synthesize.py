#!/usr/bin/env python3
"""
Batch synthesize multiple Farsi texts to speech.
"""

import argparse
from pathlib import Path
from TTS.api import TTS

def batch_synthesize(text_file, model_path, config_path, output_dir, language='fa'):
    """
    Synthesize multiple texts to speech.
    
    Args:
        text_file: Text file with one sentence per line
        model_path: Path to trained model
        config_path: Path to model config  
        output_dir: Directory to save output audio files
        language: Language code (default: 'fa' for Farsi)
    """
    
    text_file = Path(text_file)
    output_dir = Path(output_dir)
    
    if not text_file.exists():
        raise FileNotFoundError(f"Text file not found: {text_file}")
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Loading model from: {model_path}")
    model = TTS(model_name="tts_models/multilingual/multi-dataset/vits", gpu=True)
    
    # Read texts
    with open(text_file, 'r', encoding='utf-8') as f:
        texts = [line.strip() for line in f if line.strip()]
    
    print(f"Found {len(texts)} texts to synthesize\n")
    
    for i, text in enumerate(texts, 1):
        output_file = output_dir / f"output_{i:03d}.wav"
        
        print(f"[{i}/{len(texts)}] Synthesizing: {text[:50]}...")
        
        try:
            model.tts_to_file(
                text=text,
                file_path=str(output_file),
                language=language
            )
            print(f"       ✓ Saved to: {output_file}")
        except Exception as e:
            print(f"       ❌ Error: {e}")
    
    print(f"\n✅ Batch synthesis complete!")
    print(f"Output files saved to: {output_dir}/")

def main():
    parser = argparse.ArgumentParser(description="Batch synthesize Farsi speech")
    parser.add_argument('--text_file', type=str, required=True,
                       help='Text file with one sentence per line')
    parser.add_argument('--model_path', type=str, default='my_finetuned_model/best_model.pth',
                       help='Path to trained model')
    parser.add_argument('--config_path', type=str, default='my_finetuned_model/config.json',
                       help='Path to model config')
    parser.add_argument('--output_dir', type=str, default='batch_output',
                       help='Output directory for audio files')
    parser.add_argument('--language', type=str, default='fa',
                       help='Language code (default: fa for Farsi)')
    
    args = parser.parse_args()
    
    try:
        batch_synthesize(args.text_file, args.model_path, args.config_path,
                        args.output_dir, args.language)
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
