#!/usr/bin/env python3
"""
Synthesize Farsi speech from text using trained TTS model.
"""

import argparse
from pathlib import Path
from TTS.api import TTS

def synthesize(text, model_path, config_path, output_path, language='fa'):
    """
    Synthesize speech from Persian text.
    
    Args:
        text: Persian text to synthesize
        model_path: Path to trained model
        config_path: Path to model config
        output_path: Path to save output audio
        language: Language code (default: 'fa' for Farsi)
    """
    
    model_path = Path(model_path)
    output_path = Path(output_path)
    
    if not model_path.exists():
        raise FileNotFoundError(f"Model not found: {model_path}")
    
    print(f"Loading model from: {model_path}")
    
    try:
        # Load TTS model
        model = TTS(model_name="tts_models/multilingual/multi-dataset/vits", gpu=True)
        
        print(f"Synthesizing text: {text}")
        print(f"Language: Farsi (fa)")
        
        # Synthesize speech
        model.tts_to_file(
            text=text,
            file_path=str(output_path),
            language=language
        )
        
        print(f"✅ Synthesis complete!")
        print(f"Output saved to: {output_path}")
        
    except Exception as e:
        print(f"Error during synthesis: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description="Synthesize Farsi speech")
    parser.add_argument('--text', type=str, required=True,
                       help='Persian text to synthesize')
    parser.add_argument('--model_path', type=str, default='my_finetuned_model/best_model.pth',
                       help='Path to trained model')
    parser.add_argument('--config_path', type=str, default='my_finetuned_model/config.json',
                       help='Path to model config')
    parser.add_argument('--output_path', type=str, default='output.wav',
                       help='Output audio file path')
    parser.add_argument('--language', type=str, default='fa',
                       help='Language code (default: fa for Farsi)')
    
    args = parser.parse_args()
    
    try:
        synthesize(args.text, args.model_path, args.config_path, 
                  args.output_path, args.language)
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
