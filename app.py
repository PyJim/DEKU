import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from actions import take_command
from keys import sendSMSmessage, call
from weather import getWeatherData
from news import getNews
from quotes import getQuote
from mail import sendEmail
from screenshot import takeScreenshot


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    return text


talk("Hi. I am Deku, and this is your hero academia. How may I assist you?")



def run_deku():
    command = take_command()
    my_command = command
    print(command == None)
    while command == None:
        command = take_command()
        print(command)

        
    if 'play' in command:
        song = command.replace('play', '')
        action = talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        action = talk("The time is" + time)

    elif 'tell me about' in command:
        search = command.replace('tell me about',"")
        info = wikipedia.summary(search, 1)
        action = talk(info)
    
    elif 'who is' in command or 'who is' in command:
        search = command
        info = wikipedia.summary(search, 1)
        action = talk(info)

    elif 'joke' in command:
        action = talk(pyjokes.get_joke())

    elif 'how are you' in command:
        action = talk('I am so much alive. How may I be of help?')
    
    elif 'who are you' in command:
        action = talk(
            'I am Deku. The most intelligent being in the universe. This is my hero academia. How can I assist you?')

    elif 'quote'in command:
        quote = getQuote()
        action = talk(quote)
    
    elif "call my phone" in command:
        action = talk('Calling your phone now')
        call()

    elif "send me an sms" in command:
        action = talk("What message do you want me to send?")
        message = take_command()
        sendSMSmessage(message)
        action = talk("Message sent successfully")

    elif "weather" in command:
        talk("Which city do you want to get the weather condition of?")
        message = take_command()
        try:
            result = getWeatherData(message)
            action = talk(result)
        except:
            action = talk(f"Could not get weather of {message}")

    elif "news" in command:
        latest_news = getNews()
        print(latest_news)
        action = talk(latest_news)

    elif 'screenshot' in command:
        takeScreenshot()
        action = talk("Screenshot taken successfully")

    elif 'send me an email' in command:
        sendEmail()
        action = talk("Email sent successfully")

    else:
        action = talk('Can you please come again?')    

while True:
    run_deku()