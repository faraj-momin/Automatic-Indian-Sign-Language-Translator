import speech_recognition as sr
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from scipy.io.wavfile import write
import tempfile
import string

# Global variables to manage recording state
is_recording = False
audio_data = None
fs = 44100  # Sample rate
duration = 5  # Default recording duration


# Function to start recording
def start_recording():
    global is_recording, audio_data
    if is_recording:
        messagebox.showinfo("Info", "Recording is already in progress!")
        return
    is_recording = True
    print("Recording started...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')


# Function to stop recording and save the audio file
def stop_recording():
    global is_recording, audio_data
    if not is_recording:
        messagebox.showinfo("Info", "No active recording to stop!")
        return None
    sd.wait()  # Wait until the recording is finished
    print("Recording stopped.")
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(temp_file.name, fs, audio_data)
    is_recording = False
    return temp_file.name


# Function to process the recorded audio and display sign language or letters
def process_audio():
    r = sr.Recognizer()
    isl_gif = ['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
                'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 'do you have money',
                'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dont worry', 'flower is beautiful',
                'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch', 'happy journey',
                'hello what is your name', 'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing', 
                 'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i love to shop',
                'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
                'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later',
                'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 'shall I help you',
                'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam', 'wait I am thinking',
                'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your job',
                'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go', 'where do you stay',
                'where is the bathroom', 'where is the police station', 'you are wrong','address','agra','ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
'bihar','bihar','bridge','cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile','dasara',
'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes', 'gujrat', 'hello',
'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango',
'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station',
'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica',
'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village',
'voice', 'wednesday', 'weight','please wait for sometime','what is your mobile number','what are you doing','are you busy']  # Add your ISL phrases here
    alphabet = list(string.ascii_lowercase)  # ['a', 'b', ..., 'z']

    audio_file = stop_recording()
    if not audio_file:
        print("No audio file to process.")
        return

    try:
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)

        # Recognize speech using Google Web Speech API
        recognized_text = r.recognize_google(audio).lower()
        print(f'You Said: {recognized_text}')

        # Remove punctuation
        for c in string.punctuation:
            recognized_text = recognized_text.replace(c, "")

        if recognized_text in ['goodbye', 'bye']:
            messagebox.showinfo("Info", "Goodbye!")
            root.quit()
        elif recognized_text in isl_gif:
            display_gif(recognized_text)
        else:
            display_letters(recognized_text, alphabet)

    except Exception as e:
        print("Error during recognition:", e)
        messagebox.showerror("Error", f"Speech recognition failed: {e}")


# Function to display GIF for ISL phrases
def display_gif(phrase):
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

    gif_window = tk.Toplevel()
    gif_window.title("ISL Translation")
    lbl = ImageLabel(gif_window)
    lbl.pack()
    lbl.load(f'ISL_Gifs/{phrase}.gif')
    gif_window.mainloop()


# Function to display letters as images
def display_letters(recognized_text, alphabet):
    for char in recognized_text:
        if char in alphabet:
            image_path = f'letters/{char}.jpg'
            image = Image.open(image_path)
            plt.imshow(np.asarray(image))
            plt.axis('off')
            plt.show()
        else:
            continue


# GUI Setup
root = tk.Tk()
root.title("Hearing Impairment Assistant")
root.geometry("300x200")

# Buttons
btn_record = tk.Button(root, text="Start Recording", command=start_recording, width=20, height=2, bg="green", fg="white")
btn_record.pack(pady=10)

btn_stop = tk.Button(root, text="Stop Recording", command=process_audio, width=20, height=2, bg="red", fg="white")
btn_stop.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", command=root.quit, width=20, height=2, bg="gray", fg="white")
btn_exit.pack(pady=10)

# Main Loop
root.mainloop()
