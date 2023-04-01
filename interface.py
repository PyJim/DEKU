import PySimpleGUI as sg
import threading
from deku import run_deku, talk


def stop(stop_flag):
    stop_flag.set()
    talk("Call me when you need me!")

def start(stop_flag):
    while not stop_flag.is_set():
        run_deku()

current_thread = None
stop_flag = threading.Event()


layout = [
    [sg.Text("Deku Virtual Assistant")],
    [sg.Image(key="-IMAGE-", filename="Ellipse_1.png")],
    [sg.Button("START")],
    [sg.Button("STOP")]
]
window = sg.Window(title="Deku Virtual Assistant", layout=layout, margins=(250,250))


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "START":
        talk("My name is Deku. I am your friend. Let me know what I can do for you.")
        run_deku()
    
    elif event == "STOP":
        talk("Let me know when you need me")

    


window.close()