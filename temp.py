import speech_recognition as sr
import pyttsx3
import pyaudio

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print(f"Microphone with index {index}: {name}")

# System --> Microphone Array (Realtek(R) Audio)

# Initialize the recognizer
r = sr.Recognizer()

def get_active_microphone():
    p = pyaudio.PyAudio()
    default_input_device_index = p.get_default_input_device_info()["index"]
    devices = []
    for index in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(index)
        if device_info["maxInputChannels"] > 0:
            devices.append(device_info)
            if index == default_input_device_index:
                return device_info
    return None
        
# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
        
# Loop infinitely for user to speak

while True:
    active_microphone = get_active_microphone()
    if active_microphone is not None:
        print("Active Microphone:")
        print(f"Name: {active_microphone['name']}")
        print(f"ID: {active_microphone['index']}")
        try:
            with sr.Microphone(device_index=active_microphone['index']) as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("speaking")
                #listens for the user's input
                audio2 = r.listen(source2)
            
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print("Did you say ",MyText)
                SpeakText(MyText)
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occurred")
    else:
        print("No active microphone found.")

######################

# import speech_recognition as sr
# import pyttsx3
# import pyaudio
# import wave

# # Initialize the recognizer
# r = sr.Recognizer()

# def get_active_microphone():
#     p = pyaudio.PyAudio()
#     default_input_device_index = p.get_default_input_device_info()["index"]
#     devices = []
#     for index in range(p.get_device_count()):
#         device_info = p.get_device_info_by_index(index)
#         if device_info["maxInputChannels"] > 0:
#             devices.append(device_info)
#             if index == default_input_device_index:
#                 return device_info
#     return None

# # Function to convert text to speech
# def SpeakText(command):
#     # Initialize the engine
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()

# # Loop infinitely for the user to speak
# while True:
#     active_microphone = get_active_microphone()
#     if active_microphone is not None:
#         print("Active Microphone:")
#         print(f"Name: {active_microphone['name']}")
#         print(f"ID: {active_microphone['index']}")
#         try:
#             with sr.Microphone(device_index=active_microphone['index']) as source2:
#                 r.adjust_for_ambient_noise(source2, duration=0.2)
#                 print("Speaking...")
#                 # Listens for the user's input
#                 audio2 = r.listen(source2)

#                 # Save the audio as a .wav file
#                 wav_filename = "recognized_audio.wav"
#                 with wave.open(wav_filename, 'wb') as wav_file:
#                     wav_file.setnchannels(1)
#                     wav_file.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
#                     wav_file.setframerate(16000)
#                     wav_file.writeframes(audio2.get_wav_data())

#                 # Using Google to recognize audio
#                 MyText = r.recognize_google(audio2)
#                 MyText = MyText.lower()

#                 print("Did you say: ", MyText)
#                 SpeakText(MyText)
#         except sr.RequestError as e:
#             print("Could not request results; {0}".format(e))
#         except sr.UnknownValueError:
#             print("Unknown error occurred")
#     else:
#         print("No active microphone found.")

# ########################################