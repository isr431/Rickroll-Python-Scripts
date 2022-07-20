import webbrowser
from pynput.keyboard import Key, Controller

keyboard = Controller()

for i in range(50):
    keyboard.press(Key.media_volume_up)
    keyboard.release(Key.media_volume_up)

webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")