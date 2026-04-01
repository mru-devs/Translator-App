import pytesseract
from PIL import Image


def extractText(path):
        image = Image.open(path)
        return pytesseract.image_to_string(image, lang='jpn')