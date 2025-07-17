# Kannada Audio Transcription File 
This project provides a simple transcription script for Kannada audio using the Hugging Face `transformers` library and Whisper model.

# Overview
The script uses a pre-trained model (`vasista22/whisper-kannada-small`) to transcribe a given Kannada `.wav` audio file. The transcription result is printed directly to the terminal.

# Features
- Kannada transcription using a fine-tuned Whisper model
- Runs on both CPU and GPU (automatically detects CUDA)
- Supports long audio using chunked processing
- Easy-to-understand script using Hugging Face's pipeline API

# Model
- **Model Name**: [`vasista22/whisper-kannada-small`](https://huggingface.co/vasista22/whisper-kannada-small)
- **Architecture**: OpenAI Whisper
- **Task**: Automatic Speech Recognition (ASR) in Kannada

# Files in This Repository
transcription-file/
├── transcription.py # Main transcription script
├── README.md # Project overview and instructions
└── .gitignore # (Optional) Ignores audio and temp files


# Setup Instructions
1. Install required Python packages:
   ```bash
   pip install torch transformers
2. Edit the path to your audio file in transcription.py:
   audio = "/path/to/your/audio.wav"
3. Run the script:
   python transcription.py


# Example Output
  Transcription: ನೀವು ಹೇಗಿದ್ದೀರಾ? ನಾನು ಚೆನ್ನಾಗಿದ್ದೇನೆ.


# License:
  This project is intended for academic and educational use. Check individual model licenses on Hugging Face before using in production.

# Acknowledgements:
  Hugging Face Transformers
  vasista22 Whisper Kannada Model

