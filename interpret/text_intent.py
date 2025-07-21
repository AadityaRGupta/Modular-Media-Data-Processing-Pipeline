# Infer intent and parameters from that text
def get_text(input_text):
    output_text = {}

    if "weather" in input_text.lower():
        output_text["infer_intent"] = "get_weather" # what's the weather today
    elif "name" in input_text.lower():
        output_text["infer_intent"] = "ask_name" # what your name
    elif "age" in input_text.lower():
        output_text["infer_intent"] = "ask_age" # what's your age
    else:
        output_text["infer_intent"] = "unknown" # nothing matches

    output_text["text"] = input_text
    return output_text