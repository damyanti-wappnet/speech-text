import gtts
import playsound
from pydub import AudioSegment
from pydub.playback import play

text = input("Enter text: ")
sound = gtts.gTTS(text,lang='en')
sound.save('temp.mp3')

# Load the mp3 file
audio = AudioSegment.from_mp3('temp.mp3')
play(audio)
# Export the audio in wav format
# audio.export('temp.wav', format='wav')

# playsound.playsound('temp.wav')
# sound = AudioSegment.from_wav('temp.wav')
# play(sound)


# from gtts import gTTS
# import pygame

# def play_audio(filename):
#     pygame.mixer.init()
#     try:
#         pygame.mixer.music.load(filename)
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy():
#             continue
#     except pygame.error as e:
#         print("Error loading the audio file:", str(e))

# text = input("Enter text: ")
# sound = gTTS(text, lang='en')
# # sound.save('demo.wav')
# play_audio('demo.wav')
# # sound = AudioSegment.from_wav('demo.wav')
# # play(sound)
