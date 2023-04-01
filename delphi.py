import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import poetry
import stories
from actions import take_command
from keys import sendSMSmessage, call
from weather import getWeatherData

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("Hi. I am your alexa. How may I assist you?")


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("The time is" + time)

    elif 'tell me about' in command:
        search = command.replace('tell me about',"")
        info = wikipedia.summary(search, 1)
        talk(info)
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'how are you' in command:
        talk('I am so much alive. How may I be of help?')
    
    elif 'who are you' in command:
        talk('I am Delphi')

    elif 'poem' in command:
        pass
    
    elif "call my phone" in command:
        call()

    elif "send me an sms" in command:
        talk("What message do you want me to send?")
        message = take_command()
        sendSMSmessage(message)

    elif "weather" in command:
        talk("Which city do you want to get the weather condition of?")
        message = take_command()
        try:
            result = getWeatherData(message)
            talk(result)
        except:
            talk(f"Could not get weather of {message}")


    else:
        talk('Please come clearer')


while True:
    run_alexa()
    