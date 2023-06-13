import speech_recognition as sr
import pyaudio

def find_microphone_index(name):
    p = pyaudio.PyAudio()
    for index in range(p.get_device_count()):
        info = p.get_device_info_by_index(index)
        if info["name"] == name:
            return index
    return None
while True:
    # device_index = find_microphone_index("Headset (Muffs M)")
    device_index = find_microphone_index("Headphones (Realtek(R) Audio)")
    # device_index = find_microphone_index("Speakers(Realtek(R) Audio)")

    print(device_index)
    
    if device_index is not None:
        r = sr.Recognizer()
        with sr.Microphone(device_index=device_index) as source:
            print("Calibrating microphone...")
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Listening...")
            audio = r.listen(source)
            print("Processing...")

        try:
            text = r.recognize_google(audio)
            print(f"Recognized Text: {text}")
        except sr.UnknownValueError:
            print("Unable to recognize speech")
        except sr.RequestError as e:
            print(f"Error: {str(e)}")
    else:
        print("Desired microphone not found. Please check the device name.")




