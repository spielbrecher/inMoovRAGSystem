import vosk
import wave
import sys
from vosk import Model, KaldiRecognizer, SetLogLevel
import argparse
import queue
import sys
import sounddevice as sd
from main_frame import MainFrame
import tkinter as tk


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == "__main__":
    root = tk.Tk()
    app = MainFrame(root)
    root.mainloop()