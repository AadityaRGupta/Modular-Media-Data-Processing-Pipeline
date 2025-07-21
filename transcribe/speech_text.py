# Turn speech in an audio file into text
import speech_recognition as sr

def get_audio(audio_file):
    recognize_audio = sr.Recognizer()

    with sr.AudioFile(audio_file) as audio:
        recorded_audio = recognize_audio.record(audio)

    try:
        convert_text = recognize_audio.recognize_google(recorded_audio)
        return convert_text
    except Exception as unknown:
        return str(unknown)


