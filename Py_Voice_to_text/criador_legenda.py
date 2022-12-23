# --IMPORTANDO AS BIBLIOTECAS--
import moviepy.editor as mp
import speech_recognition as sr
import sys
import time
from pydub import AudioSegment
# --TRANSFORMANDO VÍDEO EM ÁUDIO--
# Variável com o nome do arquivo de vídeo
path = "video.mp4"
# Convertendo de mp4 para mp3
clip = mp.VideoFileClip(path).subclip()
clip.audio.write_audiofile("./audio.mp3")
# Convertendo mp3 para wav
sound = AudioSegment.from_mp3("./audio.mp3")
sound.export("./audio.wav", format="wav")
file_audio = sr.AudioFile(r"./audio.wav")
# Fazendo a Transcrição
r = sr.Recognizer()
with file_audio as source:
    audio_text = r.record(source)
    text = r.recognize_google(audio_text,language='pt-BR')
# Salvando o texto em um arquivo txt
arq = open('transcricao.txt', 'w')
arq.write(text)
arq.close()