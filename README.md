# Modular Media and Data Processing Pipeline

# A python based data pipeline that:
1. Turn speech in an audio file into text
2. Infer intent and parameters from that text
3. Convert text back into an audio reply
4. Pull structured fields out of a photographed document
5. Tie all these steps together behind a single, easy-to-use interface

# Folder Structure:
1. transcribe/speech_text.py - converts speech to audio
2. interpret/text_intent.py - interprets text from audio
4. synthesize/text_audio.py - converts text to audio
5. extract/extract_fields.py - extract all the fields
6. orchestrator/interface.py - implements all the steps in the interface
7. main.py - runs the whole interface pipeline

# How to run:
py main.py inputs/audio.wav
py main.py inputs/image.png

# Libraries Installed:
py -m pip install SpeechRecognition gTTS pytesseract Pillow pyaudio

# Overall Design
The project represents the modular media and data processing pipeline implemented using Python and its libraries. Everything is well designed and well organized showing core functionality in separately defined modules. The design includes:
1. Speech to text - converts the given speech into text.
2. Interpret Intent - gets the user's intent and interpret text using keywords.
3. Text to audio - converts the text (response) to audio.
4. Text extraction from image - extracting structured fields such as name, age from a image document.
5. Orchesting pipeline - implementing everything together and routing the input file to the proper pipeline.

# Key Decisions:
1. Simple audio and image creation - a simple 5 sec audio asking a question and a proper response based on the question, and a simple image creation showing name, age and date.
2. Keyword interpretation - easy detection of words using specific keywords to identify the user's intent.
3. Open libraries - all the libraries used are easily available and were quickly installed in the system such as speech recognition, gTTS, pytesseract.

# Assumptions:
1. Suitable programming language will be Python and tools such as Visual Studio Code can be used.
2. Any library can be used and implemented.
3. Audio files mush be in .wav and image files mush be in .png.
4. Image should be structured and use clear formatting for easier readability.
5. User's input will use a keyword which will be easy enough to be extracted.
6. User's input will be shorter and smaller, like asking a question.

# Swapping Components:
# Speech to text
Uses: speech recognition with Google's API.
Swap: can be swapped with openAI's AssemblyAI.
Change: modify the speech_text.py in transcribe to implement the new logic.

# Interpret Intent
Uses: simple if/else statements for basic keywords detection.
Swap: can be swapped with a high performance LLM.
Change: modify the text_intent.py in interpret to implement the new logic.

# Text to audio
Uses: Google's text to speech (gTTS).
Swap: can be swapped with advanced text detection LLMs.
Change: modify the text_audio.py in synthesize to implement the new logic.

# OCR image extraction
Uses: pytesseract.
Swap: can be swapped with Google Vision API or Azure OCR.
Change: modify the extract_fields.py in extract to implement the new logic.


































