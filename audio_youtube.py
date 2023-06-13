#Importing Pytube library
# import pytube
# # Reading the above Taken movie Youtube link
# video = 'https://www.youtube.com/watch?v=hFo_3dw8uAc'
# data = pytube.YouTube(video)
# # Converting and downloading as 'MP4' file
# audio = data.streams.get_audio_only()
# audio.download()

import pytube
from moviepy.editor import *

# Reading the YouTube video link
video_url = 'https://www.youtube.com/watch?v=hFo_3dw8uAc'
yt = pytube.YouTube(video_url)

# Download the video
stream = yt.streams.first()
video_filename = stream.default_filename
stream.download()

# Convert the video to WAV format
video_path = video_filename
output_path = 'output.wav'

video = VideoFileClip(video_path)
video.audio.write_audiofile(output_path, codec='pcm_s16le')
