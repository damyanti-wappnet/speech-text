from transformers import WhisperProcessor, WhisperForConditionalGeneration
import soundfile as sf
from scipy.signal import resample
import numpy as np
import mysql.connector
import os
import time

# Load Wihsper-base model and processor
model_name = "openai/whisper-base" 
processor = WhisperProcessor.from_pretrained(model_name)
model = WhisperForConditionalGeneration.from_pretrained(model_name)
model.config.forced_decoder_ids = None

# Set parameters
target_sampling_rate = 16000
segment_duration = 10  # Duration of each audio segment in seconds

# Function to split audio into segment of 10 seconds
def split_audio(audio_data, sampling_rate, segment_duration):
    segment_length = int(segment_duration * sampling_rate)
    num_segments = (len(audio_data) + segment_length - 1) // segment_length
    segments = []
    for i in range(num_segments):
        start = i * segment_length
        end = min((i + 1) * segment_length, len(audio_data))
        segment = audio_data[start:end]
        segments.append(segment)
    return segments

# Function to process an audio segment and transribe it into text
def process_audio_segment(segment):
    input_features = processor(segment, sampling_rate=target_sampling_rate, return_tensors="pt").input_features
    predicted_ids = model.generate(input_features)
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
    return transcription

# Function to process audio files and convert them into text and combine all segment transcribe together
def convert_audio_to_text(audio_path):
    # Load audio file
    audio_data, audio_sampling_rate = sf.read(audio_path)

    # Resample audio if needed
    if audio_sampling_rate != target_sampling_rate:
        num_samples = int(len(audio_data) * target_sampling_rate / audio_sampling_rate)
        audio_data = resample(audio_data, num_samples)

    # Convert stereo audio to mono
    if audio_data.ndim > 1:
        audio_data = np.mean(audio_data, axis=1)

    # Split audio into segments
    audio_segments = split_audio(audio_data, target_sampling_rate, segment_duration)

    # Process each audio segment and combine the results
    transcriptions = []
    for segment in audio_segments:
        transcription = process_audio_segment(segment)
        transcriptions.append(transcription)

    # Combine transcriptions from all segments
    complete_transcription = ' '.join([segment[0] for segment in transcriptions])
    return complete_transcription

#######################################################################################################################
########################################### -Insert Data into Database -###############################################

#create database connection
mydb = mysql.connector.connect(
  host="localhost",
  port = 3306,
  user="root",
  password="",
  database = "audio_text"
)

username='Damyanti'
#insert audio file path
audio_path = 'Audio/test3.wav'  # Path to the audio file
file_name = os.path.basename(audio_path) # filename

start = time.time()
transcription = convert_audio_to_text(audio_path) #transcript audio to text
print(transcription)
end = time.time()
diff = end - start
print(diff)

mycursor = mydb.cursor()

#insert data into database
sql = "insert into user_query(username,file_name, file_path,speech_text) values (%s,%s,%s,%s)"
values  = (username,file_name,audio_path,transcription)
mycursor.execute(sql, values)
mydb.commit()

mycursor.execute("select * from user_query")
result = mycursor.fetchall()
for i in result:
	print(i)

