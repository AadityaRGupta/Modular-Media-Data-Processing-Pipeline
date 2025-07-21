# Pull structured fields out of a photographed document 
import pytesseract
#python optical recognition tool

from PIL import Image
# python image library

def extract(image_path):
    load_image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(load_image) # extracting text from image

    data_parsing = {"raw_text": extracted_text}
    if "Name" in extracted_text:
        line = extracted_text.split("Name")[-1].strip().split("\n")[0]
        data_parsing["name"] = line

    return data_parsing
