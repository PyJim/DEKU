import PySimpleGUI as sg
import threading
from deku import run_deku, talk
import sys

import PySimpleGUI as sg
sg.set_options(font=('Arial Bold', 16))


layout = [[sg.Text("Deku Virtual Assistant", background_color="black")],[sg.Image(key="-IMAGE-", filename="deku-image.png", size=(300, 300), background_color="black")],[sg.Button("START")]]

window = sg.Window(title="Deku Virtual Assistant", layout=layout, margins=(200,200), background_color="black", element_justification="c")


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    
    if event == "START":
        talk("My name is Deku. I am your friend. Let me know what I can do for you.")
        while True:
            to_do = run_deku()
            if to_do == 'quit':
                sys.exit()



window.close()