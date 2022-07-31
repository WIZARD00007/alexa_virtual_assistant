import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import challenge
import wizzQn


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')


    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'challenge' in command:
          challenge.challenges()
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif command=='ask me a question':
         wizzQn.randQsn()
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif command=='do you want date me':
        talk('sorry, I have a headache')
    elif command=='are you single':
        talk('I am in a relationship with siri')
    # elif command=='calculation':
    #     abstulu.calculateAbs()
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        try:
           res=pywhatkit.info(command,lines=5)
           print(res)


        except:
            talk('an unknown error occured')


try:

   while True:
       run_alexa()
except:
    pass


