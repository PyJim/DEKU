import pyautogui
import time


def takeScreenshot():
    time.sleep(5)
    image = pyautogui.screenshot()

    PATH = r'C:\Users\jimmy\OneDrive\Desktop\screenshot.png'

    image.save(PATH)