# Farsi TTS Documentation

This repository provides scripts and resources for building a Farsi Text-to-Speech (TTS) system using the Coqui TTS library and fine-tuning a multilingual VITS model.

## Table of Contents
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/SiamakShams/farsi-tts-voice-clone.git
   cd farsi-tts-voice-clone
   ```
2. Run the setup script to create a virtual environment and install dependencies:
   ```bash
   bash setup.sh
   ```
3. Prepare your Farsi audio data:
   ```bash
   python3 prepare_data.py --input_dir raw_audio --output_dir dataset
   ```
4. Fine-tune the model with:
   ```bash
   bash train.sh
   ```
5. Synthesize speech with:
   ```bash
   bash synthesize.sh 'متن فارسی شما'
   ```

## Usage
Use the following scripts for various tasks:
- **Train a new model**: `bash train.sh`  
- **Synthesize speech**: `bash synthesize.sh 'متن فارسی'`  
- **Batch synthesize**: `python batch_synthesize.py --text_file texts.txt`  

## File Structure
```
.
├── .gitignore
├── batch_synthesize.py
├── requirements.txt
├── verify_setup.py
├── prepare_data.py
├── train.py
├── synthesize.py
├── setup.sh
├── train.sh
├── synthesize.sh
├── run_webui.sh
└── my_finetuned_model/
```

- `.gitignore`: Specifies files and directories that should be ignored by Git.
- `batch_synthesize.py`: Script for synthesizing multiple texts.
- `train.py`: Script for fine-tuning the TTS model.
- `synthesize.py`: Script for synthesizing speech from text.
- `setup.sh`: Script to set up the environment and dependencies.
- `train.sh`, `synthesize.sh`, `run_webui.sh`: Various bash scripts for training and synthesis tasks.
- `my_finetuned_model/`: Directory where the fine-tuned model will be saved.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.