import speech_recognition as sr
import mysql.connector

username='Damyanti'
file_name = "temp_rec.wav"

# Path to the audio file you want to transcribe
audio_path = 'Audio/temp_rec.wav'

# Create a recognizer instance
recognizer = sr.Recognizer()

# Read the audio file
with sr.AudioFile(audio_path) as source:
    audio = recognizer.record(source)

# Perform the speech-to-text conversion
text = recognizer.recognize_whisper(audio)

mydb = mysql.connector.connect(
  host="localhost",
  port = 3306,
  user="root",
  password="",
  database = "audio_text"
)

mycursor = mydb.cursor()

#insert data into database
sql = "insert into user_query(username,file_name, file_path,speech_text) values (%s,%s,%s,%s)"
values  = (username,file_name,audio_path,text)
mycursor.execute(sql, values)
mydb.commit()
# print(mycursor.rowcount)

mycursor.execute("select * from user_query")
result = mycursor.fetchall()
for i in result:
	print(i)


###############################################################################