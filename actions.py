import speech_recognition as sr

listener = sr.Recognizer()

def take_command():
    try:
        while True:
            with sr.Microphone() as source:
                print("listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                while command != None:
                    command = command.lower()
                    if 'deku' in command:
                        command = command.replace('deku', "")
                    return command
    except:
        pass
