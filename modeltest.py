# from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
# import soundfile as sf
# import librosa
# import torch
# import time


# model_name = "jonatasgrosman/wav2vec2-large-xlsr-53-english"

# model = Wav2Vec2ForCTC.from_pretrained(model_name)
# tokenizer = Wav2Vec2Processor.from_pretrained(model_name)
# start = time.time()

# audio_file = "temp_rec.wav"
# audio, sample_rate = sf.read(audio_file)

# # Resample the audio if necessary
# audio, sample_rate = librosa.load(audio_file, sr=16000)

# # Convert the audio to tensor input
# input_values = tokenizer(audio, return_tensors="pt").input_values

# # Pass the input values through the model
# with torch.no_grad():
#     logits = model(input_values).logits

# # Use the tokenizer to decode the predicted tokens
# predicted_ids = torch.argmax(logits, dim=-1)
# transcription = tokenizer.batch_decode(predicted_ids)[0]
# print("Transcription:", transcription)
# end = time.time()
# diff = end - start
# print(diff)



from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torchaudio
import torch

# load model and processor
processor = WhisperProcessor.from_pretrained("openai/whisper-base")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-base")
model.config.forced_decoder_ids = None

# Load the audio file
audio_file = "Audio/temp_rec.wav"

# Read the audio file
waveform, sample_rate = torchaudio.load(audio_file, sr=16000)

# Convert the audio to mono if it has multiple channels
if waveform.shape[0] > 1:
    waveform = torch.mean(waveform, dim=0, keepdim=True)

# Resample the audio if required
if sample_rate != processor.feature_extractor.sampling_rate:
    resampler = torchaudio.transforms.Resample(sample_rate, processor.feature_extractor.sampling_rate)
    waveform = resampler(waveform)

# Extract input features
input_features = processor(
    waveform.squeeze().numpy(),
    sampling_rate=processor.feature_extractor.sampling_rate,
    return_tensors="pt"
).input_features

# Generate token ids
predicted_ids = model.generate(input_features, max_length=1000000)
# Decode token ids to text
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

print("Transcription:", transcription)
