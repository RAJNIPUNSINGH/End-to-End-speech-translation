import tkinter as tk
from tkinter import filedialog
from translate import Translator
from gtts import gTTS
import os
import speech_recognition as sr
import pygame

def translate_text(text, target_language='en'):
    translator = Translator(to_lang=target_language)
    translated_text = translator.translate(text)
    return translated_text

def recognize_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio, language="en")
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def translate_and_save():
    target_language = language_entry.get()
    text = text_entry.get('1.0', tk.END)
    
    if not text.strip():
        result_label.config(text="Please provide text or use microphone.")
        return
    
    translated_text = translate_text(text, target_language)
    
    if not translated_text.strip():
        result_label.config(text="Translation failed. Please try again.")
        return
    
    translated_audio_file = "final_translated_speech.mp3"
    # Delete existing file, if any
    if os.path.exists(translated_audio_file):
        os.remove(translated_audio_file)
    tts = gTTS(text=translated_text, lang=target_language)
    tts.save(translated_audio_file)
    result_label.config(text="Translation complete. Translated audio saved as: " + translated_audio_file)

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

def translate_file():
    file_path = file_path_entry.get()
    if not os.path.exists(file_path):
        result_label.config(text="File not found.")
        return
    
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    
    target_language = language_entry.get()
    translated_text = translate_text(text, target_language)
    translated_audio_file = "final_translated_speech.mp3"
    # Delete existing file, if any
    if os.path.exists(translated_audio_file):
        os.remove(translated_audio_file)
    tts = gTTS(text=translated_text, lang=target_language)
    tts.save(translated_audio_file)
    result_label.config(text="Translation complete. Translated audio saved as: " + translated_audio_file)

def translate_from_mic():
    text = recognize_audio()
    if not text:
        result_label.config(text="Failed to recognize speech.")
        return
    
    target_language = language_entry.get()
    translated_text = translate_text(text, target_language)
    
    if not translated_text.strip():
        result_label.config(text="Translation failed. Please try again.")
        return
    
    translated_audio_file = "final_translated_speech.mp3"
    # Delete existing file, if any
    if os.path.exists(translated_audio_file):
        os.remove(translated_audio_file)
    tts = gTTS(text=translated_text, lang=target_language)
    tts.save(translated_audio_file)
    result_label.config(text="Translation complete. Translated audio saved as: " + translated_audio_file)

def play_translated_audio():
    translated_audio_file = "final_translated_speech.mp3"
    if os.path.exists(translated_audio_file):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(translated_audio_file)
        pygame.mixer.music.play()

# Create GUI
root = tk.Tk()
root.title("Audio Translation Tool")
root.geometry("400x350")

# Create widgets
text_label = tk.Label(root, text="Text to Translate:")
text_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

text_entry = tk.Text(root, height=5, width=40)
text_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

file_path_label = tk.Label(root, text="File Path:")
file_path_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

file_path_entry = tk.Entry(root, width=30)
file_path_entry.grid(row=1, column=1, padx=5, pady=5)

file_dialog_button = tk.Button(root, text="Browse", command=open_file_dialog)
file_dialog_button.grid(row=1, column=2, padx=5, pady=5)

language_label = tk.Label(root, text="Target Language Code:")
language_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

language_entry = tk.Entry(root, width=10)
language_entry.grid(row=2, column=1, padx=5, pady=5)

translate_button = tk.Button(root, text="Translate Text", command=translate_and_save, bg="#4CAF50", fg="white")
translate_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="we")

translate_file_button = tk.Button(root, text="Translate File", command=translate_file, bg="#2196F3", fg="white")
translate_file_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="we")

mic_button = tk.Button(root, text="Translate from Microphone", command=translate_from_mic, bg="#FFC107", fg="black")
mic_button.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="we")

play_button = tk.Button(root, text="Play Translated Audio", command=play_translated_audio, bg="#FF9800", fg="white")
play_button.grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky="we")

result_label = tk.Label(root, text="", wraplength=300)
result_label.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
