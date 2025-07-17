import torch
from transformers import pipeline

# path to the audio file to be transcribed
audio = "/media/vksit/data/Samsung_Prism_2025/Hearing_Impaired_Data/1_HI_High/F02/F02_001_1.wav"
device = "cuda:0" if torch.cuda.is_available() else "cpu"

transcribe = pipeline(task="automatic-speech-recognition", model="vasista22/whisper-kannada-small", chunk_length_s=30, device=device)
transcribe.model.config.forced_decoder_ids = transcribe.tokenizer.get_decoder_prompt_ids(language="kn", task="transcribe")

print('Transcription: ', transcribe(audio)["text"])
