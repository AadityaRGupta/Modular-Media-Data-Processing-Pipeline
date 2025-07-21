# Convert text back into an audio reply 
from gtts import gTTS
# google text to speech library

def get_reply(response, path):
    result = gTTS(text=response, lang="en") # text to speech using Google API
    result.save(path)
