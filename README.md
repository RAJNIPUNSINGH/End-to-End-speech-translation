## SPEECH TO SPEECH TRANSLATION

This Python script provides a simple graphical user interface (GUI) for translating text and audio files into different languages. It also allows for translation directly from microphone input.

## Dependencies
- Python 3.x
- [tkinter](https://docs.python.org/3/library/tkinter.html) - Standard GUI library for Python.
- [translate](https://pypi.org/project/translate/) - Python library for translating text using various translation APIs.
- [gtts](https://pypi.org/project/gTTS/) - Google Text-to-Speech library for converting text to speech.
- [speech_recognition](https://pypi.org/project/SpeechRecognition/) - Library for performing speech recognition with support for several engines and APIs.
- [pygame](https://pypi.org/project/pygame/) - Library for multimedia applications such as sound and video playback.

## Usage
1. Run the script `S2Sfinal.py`.
2. Enter text to be translated in the "Text to Translate" field.
3. Optionally, provide a target language code in the "Target Language Code" field (for e.g., "hi" for "Hindi").
4. Click the "Translate Text" button to translate the entered text. The translated audio will be saved as "final_translated_speech.mp3".
5. Alternatively, you can translate an audio file by clicking the "Browse" button to select an audio file, then clicking the "Translate File" button.
6. To translate from microphone input, click the "Translate from Microphone" button and speak into the microphone when prompted.
7. Click the "Play Translated Audio" button to play the translated audio.

## GUI Components
- **Text to Translate:** Text entry field for entering the text to be translated.
- **File Path:** Entry field for displaying the selected file path when translating audio files.
- **Target Language Code:** Entry field for specifying the target language code for translation(for e.g., "hi" for "Hindi").
- **Translate Text:** Button for translating entered text and saving the translated audio.
- **Translate File:** Button for translating selected audio file.
- **Translate from Microphone:** Button for translating speech input from the microphone.
- **Play Translated Audio:** Button for playing the translated audio.
- **Result Label:** Label for displaying the status of translation operations.

## How to Run
1. Ensure all dependencies are installed (`tkinter`, `translate`, `gtts`, `speech_recognition`, `pygame`).
2. Run the script `S2Sfinal.py` using a Python interpreter.

## Credits
tkinter: Standard GUI library for Python.

translate: Developed by Saphyraex and contributors.

gtts: Developed by Pierre Nicolas Durette and contributors.

speech_recognition: Developed by Anthony Zhang and contributors.

pygame: Developed by the pygame community.

