import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import speech_recognition as sr

class MainFrame:

    def __init__(self, root):
        self.root = root
        self.root.title("inMoov RAG System")

        # Создание полей для ввода и вывода текста
        self.input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.input_text.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.output_text.grid(row=0, column=2, padx=10, pady=10, columnspan=2)

        # Создание кнопок
        self.start_listen_button = tk.Button(root, text="Старт прослушивания", command=self.start_listening)
        self.start_listen_button.grid(row=1, column=0, padx=5, pady=10)

        self.stop_listen_button = tk.Button(root, text="Стоп прослушивания", command=self.stop_listening)
        self.stop_listen_button.grid(row=1, column=1, padx=5, pady=10)

        self.start_speak_button = tk.Button(root, text="Старт озвучивания", command=self.start_speaking)
        self.start_speak_button.grid(row=1, column=2, padx=5, pady=10)

        self.stop_speak_button = tk.Button(root, text="Стоп озвучивания", command=self.stop_speaking)
        self.stop_speak_button.grid(row=1, column=3, padx=5, pady=10)

        # Инициализация распознавания речи
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.listening = False

        # Инициализация синтеза речи
        self.engine = pyttsx3.init()
        self.speaking = False

    def start_listening(self):
        if not self.listening:
            self.listening = True
            self.listen_thread = self.root.after(100, self.listen)

    def stop_listening(self):
        if self.listening:
            self.listening = False
            self.root.after_cancel(self.listen_thread)

    def listen(self):
        if self.listening:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
                try:
                    text = self.recognizer.recognize_google(audio, language="ru-RU")
                    self.input_text.insert(tk.END, text + "\n")
                except sr.UnknownValueError:
                    pass
                except sr.RequestError:
                    pass
            self.listen_thread = self.root.after(100, self.listen)

    def start_speaking(self):
        if not self.speaking:
            self.speaking = True
            text = self.output_text.get("1.0", tk.END)
            self.engine.say(text)
            self.engine.runAndWait()
            self.speaking = False

    def stop_speaking(self):
        if self.speaking:
            self.engine.stop()
            self.speaking = False

