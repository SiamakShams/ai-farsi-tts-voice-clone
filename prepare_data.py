#!/usr/bin/env python3
"""
Prepare Farsi audio data for TTS training.
Converts audio files to 22050Hz WAV format and creates metadata CSV.
"""

import os
import argparse
import subprocess
from pathlib import Path
import csv

def convert_audio_to_wav(input_file, output_file, sample_rate=22050):
    """Convert any audio format to WAV at specified sample rate using FFmpeg"""
    try:
        cmd = [
            'ffmpeg', '-i', str(input_file),
            '-acodec', 'pcm_s16le',
            '-ar', str(sample_rate),
            '-ac', '1',
            '-y',
            str(output_file)
        ]
        subprocess.run(cmd, capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"�� Error converting {input_file}: {e}")
        return False

def prepare_dataset(input_dir, output_dir, sample_rate=22050):
    """
    Prepare dataset by converting all audio files to WAV format.
    
    Args:
        input_dir: Directory containing audio files
        output_dir: Output directory for processed files
        sample_rate: Target sample rate (default: 22050 Hz)
    """
    
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Create output directories
    output_wavs = output_path / "wavs"
    output_wavs.mkdir(parents=True, exist_ok=True)
    
    # Supported audio formats
    audio_extensions = {'.wav', '.mp3', '.m4a', '.flac', '.ogg', '.aac'}
    
    # Find all audio files
    audio_files = []
    for ext in audio_extensions:
        audio_files.extend(input_path.glob(f'**/*{ext}'))
        audio_files.extend(input_path.glob(f'**/*{ext.upper()}'))
    
    if not audio_files:
        print(f"❌ No audio files found in {input_dir}")
        return False
    
    print(f"✓ Found {len(audio_files)} audio files")
    print(f"Converting to {sample_rate}Hz WAV format...")
    
    converted_files = []
    for i, audio_file in enumerate(sorted(audio_files), 1):
        # Create output filename
        output_filename = f"sample_{i:03d}.wav"
        output_filepath = output_wavs / output_filename
        
        print(f"  [{i}/{len(audio_files)}] Converting {audio_file.name}...", end=" ")
        
        if convert_audio_to_wav(audio_file, output_filepath, sample_rate):
            print("✓")
            converted_files.append(output_filename)
        else:
            print("❌")
    
    if not converted_files:
        print("❌ No files were successfully converted")
        return False
    
    # Create metadata template
    metadata_path = output_path / "metadata.csv"
    print(f"\n✓ Creating metadata template at {metadata_path}")
    
    with open(metadata_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='|')
        for filename in converted_files:
            # Template row: filename|[ADD_FARSI_TEXT_HERE]
            writer.writerow([filename, "[متن فارسی را اینجا بنویسید]"])
    
    print(f"\n✅ Dataset prepared successfully!")
    print(f"   - Converted files: {output_wavs}/")
    print(f"   - Metadata template: {metadata_path}")
    print(f"\n📝 Next steps:")
    print(f"   1. Edit {metadata_path} and replace Persian text for each file")
    print(f"   2. Format: filename.wav|متن فارسی")
    print(f"   3. Run training: bash train.sh")
    
    return True

def main():
    parser = argparse.ArgumentParser(
        description="Prepare Farsi audio data for TTS training"
    )
    parser.add_argument(
        '--input_dir',
        type=str,
        default='raw_audio',
        help='Input directory containing audio files'
    )
    parser.add_argument(
        '--output_dir',
        type=str,
        default='dataset',
        help='Output directory for processed files'
    )
    parser.add_argument(
        '--sample_rate',
        type=int,
        default=22050,
        help='Target sample rate in Hz (default: 22050)'
    )
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.input_dir):
        print(f"❌ Input directory not found: {args.input_dir}")
        return 1
    
    success = prepare_dataset(args.input_dir, args.output_dir, args.sample_rate)
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
