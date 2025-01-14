import speech_recognition as sr
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
import tkinter as tk
import string
from scipy.io.wavfile import write
import tempfile

# Function to record audio using sounddevice and save it as a WAV file
def record_audio(duration=5, fs=44100):
    print("Recording...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    print("Recording complete.")
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(temp_file.name, fs, audio_data)
    return temp_file.name

# Speech recognition and sign language translation
def func():
    r = sr.Recognizer()
    isl_gif = [...]  # Use your existing list of ISL phrases
    arr = ['a', 'b', 'c', ..., 'z']  # Alphabet list

    while True:
        print("Recording audio for recognition...")
        audio_file = record_audio(duration=5)  # Record 5 seconds of audio
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)

        # Recognize speech using Google Web Speech API
        try:
            a = r.recognize_google(audio).lower()
            print(f'You Said: {a}')

            for c in string.punctuation:
                a = a.replace(c, "")

            if a in ['goodbye', 'good bye', 'bye']:
                print("Oops! Time to say goodbye")
                break
            elif a in isl_gif:
                class ImageLabel(tk.Label):
                    def load(self, im):
                        if isinstance(im, str):
                            im = Image.open(im)
                        self.loc = 0
                        self.frames = []

                        try:
                            for i in range(1000):  # Assuming GIF has 1000 frames
                                self.frames.append(ImageTk.PhotoImage(im.copy()))
                                im.seek(i)
                        except EOFError:
                            pass

                        self.delay = im.info.get('duration', 100)

                        if len(self.frames) == 1:
                            self.config(image=self.frames[0])
                        else:
                            self.next_frame()

                    def unload(self):
                        self.config(image=None)
                        self.frames = None

                    def next_frame(self):
                        if self.frames:
                            self.loc = (self.loc + 1) % len(self.frames)
                            self.config(image=self.frames[self.loc])
                            self.after(self.delay, self.next_frame)

                root = tk.Tk()
                lbl = ImageLabel(root)
                lbl.pack()
                lbl.load(f'ISL_Gifs/{a}.gif')
                root.mainloop()
            else:
                for char in a:
                    if char in arr:
                        image_path = f'letters/{char}.jpg'
                        image = Image.open(image_path)
                        plt.imshow(np.asarray(image))
                        plt.draw()
                        plt.pause(0.8)
                    else:
                        continue
        except Exception as e:
            print("Error:", e)
        plt.close()

while True:
    image = "signlang.png"
    msg = "HEARING IMPAIRMENT ASSISTANT"
    choices = ["Live Voice", "All Done!"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == choices[0]:
        func()
    if reply == choices[1]:
        quit(q)
