# Automatic-Indian-Sign-Language-Translator

This project is a desktop application designed to assist individuals with hearing impairments by recognizing spoken words and translating them into Indian Sign Language (ISL) phrases or displaying corresponding letters. The application leverages Python's speech recognition capabilities and graphical user interface (GUI) to facilitate communication for the hearing impaired.

## Features
- **Speech Recording:** Record audio through the microphone.
- **Speech Recognition:** Convert the recorded speech into text using Google's Web Speech API.
- **ISL Phrase Display:** Display GIFs for recognized ISL phrases.
- **Letter Display:** Show corresponding letters for unrecognized or non-ISL words.
- **User Interface:** A simple GUI built using Tkinter.

## Requirements
- Python 3.6+
- Libraries:
  - `speech_recognition`
  - `sounddevice`
  - `numpy`
  - `matplotlib`
  - `tkinter`
  - `PIL` (Pillow)
  - `scipy`

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/faraj-momin/Automatic-Indian-Sign-Language-Translator.git
   cd Automatic-Indian-Sign-Language-Translator

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Run the Application:**
   ```bash
   python main3.py

**Usage**

- **Start Recording:** Click the "Start Recording" button to begin recording your speech.

- **Stop Recording:** Click the "Stop Recording" button to stop recording and process the audio.

- **View Results:** The application will either display a corresponding ISL GIF for recognized phrases or show the letters for unrecognized words.

- **Exit:** Click the "Exit" button to close the application.

**File Structure**

- **main3.py:** The main application script.

- **ISL_Gifs/:** Directory containing GIFs for ISL phrases.

- **letters/:** Directory containing images of letters for non-ISL words.
