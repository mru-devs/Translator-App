import pytesseract
from translate import Translator
from PIL import Image


class functionTranslate:
    def __init__(self):
        self.translator = Translator(to_lang="en")

    def JapaneseToEnglish(self, path):
        image = Image.open(path)
        readerOutput = pytesseract.image_to_string(image, lang='jpn')
        #print(readerOutput)
        readerOutput = " ".join(readerOutput)
        translation = self.translator.translate(readerOutput)
        print(translation)



    def KoreanToEnglish(self, path):
        pass

    def SwedishToEnglish(self, path):
        pass


#obj1 = functionTranslate()
#obj1.JapaneseToEnglish('Translator App/page3.png')
#obj1.JapaneseToEnglish('Translator App/page2.png')