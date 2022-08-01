# Rickroll-Python-Scripts
A collection of Python Rickroll scripts, with three versions: Basic, Intermediate and Advanced.

## Basic
'Basic' simply uses the webbrowser module to open the YouTube link.

## Intermediate
'Intermediate' uses the pynput module to simulate keypresses of the volume up key to maximise the volume.

## Advanced
'Advanced' creates a shortcut in the Windows startup folder, so the script executes every time the device is turned on. It also hides the file and makes it a system file, so it is not visible even with the option to show hidden files on.

## Converting to executable
You can use PyInstaller to convert the script to an .exe. Firstly, import PyInstaller using:

```
import pyinstaller
```

Next, open the folder your script is located in and enter 'cmd' in the address bar. After command prompt is opened, enter:

```
pyinstaller --onefile -w script.py
```
