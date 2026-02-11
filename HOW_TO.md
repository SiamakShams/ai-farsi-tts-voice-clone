# 1. Verify setup
```
docker-compose run --rm farsi-tts setup
```
**What it does:** Checks if everything is installed correctly (Python, PyTorch, GPU, FFmpeg).

**Inputs:** None needed.

**When to use:** First thing after building the Docker image. Run once to confirm everything works.

**Expected output:** Shows versions of installed software and says "✅ All checks passed!"

---

# 2. Prepare data
```
docker-compose run --rm farsi-tts prepare /workspace/host_data/raw_audio dataset
```
**What it does:** Converts your audio files to the format the AI needs (22050Hz WAV files).

**Inputs needed:** Your Farsi audio files (MP3, WAV, M4A, etc.)

**Where to get them:** You provide them. Put them in `data/raw_audio/` folder on your computer.

**How it works:**
- Looks in `/workspace/host_data/raw_audio/` (which is your `data/raw_audio/` folder)
- Converts each audio file to WAV format
- Creates `data/dataset/wavs/` folder with converted files
- Creates `data/dataset/metadata.csv` file (template)

**After this:** You need to edit `data/dataset/metadata.csv` and add the Persian text that matches each audio file.

---

# 3. Train model
```
docker-compose run --rm farsi-tts train 100
```
**What it does:** Teaches the AI to speak in your voice.

**Inputs needed:**
- Audio files (from step 2)
- Metadata file with Persian text (from step 2, edited by you)

**Process:**
- 100 = number of training iterations (more = better quality but takes longer)
- Takes 60-120 minutes to run
- Creates `data/my_finetuned_model/` folder with the trained model

**After this:** You can synthesize speech in your voice.

---

# 4. Synthesize speech
```
docker-compose run --rm farsi-tts synthesize "سلام دنیا"
```
**What it does:** Generates speech from Persian text using your trained voice.

**Inputs needed:**
- Trained model (from step 3)
- Persian text you want to speak (in the quotes)

**How it works:**
- Takes the text `"سلام دنیا"` (can be any Persian sentence)
- Uses your trained model to generate audio
- Saves as `data/output.wav`

**Output:** Audio file you can listen to with any media player.

---

# 5. Batch synthesis
```
docker-compose run --rm farsi-tts batch /workspace/host_data/texts.txt /workspace/host_data/results
```
**What it does:** Generates speech for many sentences at once instead of one by one.

**Inputs needed:**
- Text file with Persian sentences (one sentence per line)
- Trained model (from step 3)

**Where to get the text file:** Create it yourself. Example:
```
سلام دنیا
خوب صبح
خوشحال می‌شم
```
Save as `data/texts.txt`

**How it works:**
- Reads each line from `data/texts.txt`
- Generates audio for each line
- Saves all audio files to `data/results/` folder

**Output:** Multiple WAV files (output_001.wav, output_002.wav, etc.)

---

# 6. Interactive shell
```
docker-compose run --rm farsi-tts shell
```
**What it does:** Opens a terminal inside the Docker container where you can run commands manually.

**Inputs:** None needed.

**When to use:** For debugging or if you want to run custom commands.

**How to exit:** Type `exit` and press Enter.

---

# 7. Show help
```
docker-compose run --rm farsi-tts help
```
**What it does:** Displays a list of all available commands and examples.

**Inputs:** None needed.

**When to use:** When you forget how to use a command or need to see all available options.

---

## The Typical Workflow (Simple Order)

1. **docker-compose run --rm farsi-tts setup** → Check if installed
2. Put audio files in `data/raw_audio/`
3. **docker-compose run --rm farsi-tts prepare /workspace/host_data/raw_audio dataset** → Convert audio
4. Edit `data/dataset/metadata.csv` → Add Persian text
5. **docker-compose run --rm farsi-tts train 100** → Train (takes 1-2 hours)
6. **docker-compose run --rm farsi-tts synthesize "سلام"** → Generate speech
7. Listen to `data/output.wav`

Done! 🎉
