import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
    return text

def take_command():
    try:
        while True:
            with sr.Microphone() as source:
                print("listening...")
                talk("speak now")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                while command != None:
                    command = command.lower()
                    if 'deku' in command:
                        command = command.replace('deku', "")
                    return command
    except:
        pass
