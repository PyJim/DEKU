import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

engine.say('I am your alexa')
engine.say('What can I do for you?')
try:
    with sr.Microphone() as source:
        print("listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)
except:
    pass