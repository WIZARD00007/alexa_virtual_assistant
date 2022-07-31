import random
import speech_recognition as sr
import pyttsx3
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()


def takeQSN():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)





    except:
         pass
    return command
talk('hello! im alexa! by the way what is your name')
command = takeQSN()

command=command.replace('my name is','')
talk(' nice name'+command)
talk('by the way'+command+'how can i help you')
nme=command
def stChat():
    command = takeQSN()

    if command=='how are you' or command=='whats up':
        talk('I’m fine thanks! How are you doing?')

    elif 'i am good' in command:
        talk('thats cool'+command+'can i ask you a question')
try:
    while True:
      stChat()
except:
    talk('some unknown error occured')
