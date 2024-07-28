import os
from tkinter import filedialog

directory = ""

def changeDownloadDir():
    global directory
    directory = filedialog.askdirectory()
    os.chdir(directory)
    print(directory)