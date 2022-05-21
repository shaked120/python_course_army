import gtts
from playsound import playsound

tts = gtts.gTTS("first time im using a package in next.py course")
tts.save("hello.mp3")
playsound("hello.mp3")

