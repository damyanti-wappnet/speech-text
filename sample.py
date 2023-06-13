from transformers import WhisperProcessor, WhisperForConditionalGeneration
import soundfile as sf
import librosa
import torch
import time

model_name = "openai/whisper-base"
# load model and processor
tokenizer = WhisperProcessor.from_pretrained(model_name)
model = WhisperForConditionalGeneration.from_pretrained(model_name)
model.config.forced_decoder_ids = None

start = time.time()


end = time.time()
diff = end - start
print(diff)
