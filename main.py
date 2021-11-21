import speech_recognition as sr
from time import ctime
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()
m = sr.Microphone()

def record_audio(ask = False):
    with m as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)
        voice_data =''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexis_speak("Oops! Didn't catch that")
        except sr.RequestError as e:
            alexis_speak('Sorry, my speech service is down')
        return voice_data

def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(0, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('My name is Alexis')
    if 'what is the time' in voice_data:
        alexis_speak(ctime())
    if 'can you go online' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What location do you wanna find?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
alexis_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)