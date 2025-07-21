# Tie all these steps together behind a single, easy-to-use interface 
import os
from transcribe.speech_text import get_audio
from interpret.text_intent import get_text
from synthesize.text_audio import get_reply
from extract.extract_fields import extract

def initiate(input_file):
    file_path = os.path.splitext(input_file)[1].lower()

    if file_path in [".wav", ".mp3"]:
        speech_to_text = get_audio(input_file) # speech to text
        infer_text = get_text(speech_to_text) # get the text intent
        user_intent = infer_text["infer_intent"]
        # replies to user
        if user_intent == "get_weather":
            response = "It's a rainy weather with light wind."
        elif user_intent == "ask_name":
            response = "My name is Receptro AI."
        elif user_intent == "ask_age":
            response = "I have been here for thousand of years."
        else:
            response = "Sorry, I didn't understand that. Can you please say that again."
        output = "outputs/response.mp3"
        get_reply(response, output)

        return {
            "speech_to_text": speech_to_text,
            "infer_intent": infer_text,
            "response_with_audio": output
        }

    elif file_path in [".png", ".jpg", ".jpeg"]:
        extract_image = extract(input_file)
        return {"extract_output": extract_image}

    else:
        return {"error": "file type not supported"}

