import speech_recognition as sr
import tensorflow as tf

# Path to the audio file you want to transcribe
audio_path = 'Audio/temp_rec.wav'

# Create a recognizer instance
recognizer = sr.Recognizer()

# Read the audio file
with sr.AudioFile(audio_path) as source:
    audio = recognizer.record(source)

# Perform the speech-to-text conversion using TensorFlow backend
text = recognizer.recognize_whisper(audio)

# Print the transcribed text
print("Transcription:", text)
