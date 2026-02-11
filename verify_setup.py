#!/usr/bin/env python3
"""
Verify that all dependencies for Farsi TTS are correctly installed.
Run this after setup.sh to validate your environment.
"""

import sys

def check_python_version():
    """Check Python version is 3.9+"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("❌ Python 3.9+ required")
        return False
    print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")
    return True

def check_pytorch():
    """Check PyTorch is installed with CUDA support"""
    try:
        import torch
        print(f"✓ PyTorch version: {torch.__version__}")
        
        if torch.cuda.is_available():
            print(f"✓ CUDA available: True")
            print(f"✓ GPU: {torch.cuda.get_device_name(0)}")
            gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1e9
            print(f"✓ GPU Memory: {gpu_memory:.2f} GB")
        else:
            print("⚠ CUDA not available (CPU mode will be slow)")
        return True
    except ImportError:
        print("❌ PyTorch not installed")
        return False

def check_tts():
    """Check Coqui TTS is installed"""
    try:
        import TTS
        print(f"✓ Coqui TTS installed")
        return True
    except ImportError:
        print("❌ Coqui TTS not installed")
        return False

def check_audio_libs():
    """Check audio processing libraries"""
    try:
        import librosa
        import soundfile
        import scipy
        print("✓ Audio libraries (librosa, soundfile, scipy) installed")
        return True
    except ImportError:
        print("❌ Audio libraries not fully installed")
        return False

def check_ffmpeg():
    """Check FFmpeg is available"""
    import subprocess
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        print("✓ FFmpeg available")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠ FFmpeg not found (needed for audio conversion)")
        return False

def main():
    """Run all verification checks"""
    print("=" * 50)
    print("Farsi TTS Voice Clone - Setup Verification")
    print("=" * 50)
    print()
    
    checks = [
        ("Python Version", check_python_version),
        ("PyTorch", check_pytorch),
        ("Coqui TTS", check_tts),
        ("Audio Libraries", check_audio_libs),
        ("FFmpeg", check_ffmpeg),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"Checking {name}...")
        try:
            result = check_func()
            results.append(result)
        except Exception as e:
            print(f"❌ Error checking {name}: {e}")
            results.append(False)
        print()
    
    print("=" * 50)
    if all(results):
        print("✅ All checks passed! Ready to use.")
        return 0
    else:
        print("❌ Some checks failed. Please review the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
