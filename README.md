# Screen Translator

**STATUS:** In Progress (On-going)

Screen Translator is a Python application that translates any snipped screen region in real-time. It is a simple and straight-forward application. 
Many screen translator applications lack an option to setting your own API-request frequency regarding an LLM, thus leading to 429-Many Requests. This application will include that option on top of being 
simple and intuitive in usage.

PyTesseract as an OCR-library is more efficient than the likes of EasyOCR, which is crucial for achieving real-time translation. Performance prioritized over accuracy regarding text extraction.
The application currently supports two options, either a simple translate library based on Google Translate or LLM API for higher accuracy regarding context and other intricacies. This allows the user to use the app for a wide range of activities, e.g. reading books, documents, video captions and even game captions.

The pipeline is as follows:
1. User snips an image through the GUI
2. MSS captures the image
4. Pillow processes and feeds the image to PyTesseract
5. PyTesseract extracts the text from the image
6. The chosen translation model is used to translate
7. The translation is printed out 

## Requirements
Required programming language:
Python 3.9+

The libraries required are as follows:
PyTesseract,
Pillow,
PySide6,
Python MSS,
Google Genai SDK,
Translate

## Installation
The required libraries can be installed with the pip command below:
```bash
pip install pytesseract pillow PySide6 mss google-genai translate
```

## Usage
Download or clone this repository. Run GUI.py in your Python environment.
After the GUI window appears, press on New Snip. Immediately after, press and hold the left button and drag the mouse cursor over a chosen region of the screen and finally release the mouse button. 
The terminal will then print out the translation of the text.



