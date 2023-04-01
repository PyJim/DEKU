import speech_recognition as sr

listener = sr.Recognizer()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            while command != None:
                if 'alexa' in command:
                    command = command.replace('alexa', "")
                return command
    except:
        pass
