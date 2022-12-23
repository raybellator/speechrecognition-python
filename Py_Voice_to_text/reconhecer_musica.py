import speech_recognition as sr
import time

r = sr.Recognizer()

with sr.AudioFile('musica.wav') as source:
    audio = r.record(source)
subtitles = ""
frases = []
for i, word in enumerate(r.recognize_google(audio, language='pt-BR').split()):
    subtitles += str(i+1) + "\n" + time.strftime('%H:%M:%S', time.gmtime(i)) + " --> " + time.strftime('%H:%M:%S', time.gmtime(i+1)) + "\n" + word +  "\n\n"

with open('subtitles.srt', 'w') as file:
    file.write(subtitles)