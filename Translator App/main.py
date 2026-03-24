import easyocr
from translate import Translator

class functionTranslate:
    def __init__(self):
        self.japaneseReader = easyocr.Reader(['ja'])
        self.englishReader = easyocr.Reader(['en'])  
        self.translator = Translator(to_lang="en")

    def JapaneseToEnglish(self, path):
        readerOutput = self.japaneseReader.readtext(path, detail=0)
        readerOutput = " ".join(readerOutput)
        translation = self.translator.translate(readerOutput)
        print(translation)

    def KoreanToEnglish(self, path):
        pass
    def SwedishToEnglish(self, path):
        pass


obj1 = functionTranslate()
obj1.JapaneseToEnglish('Translator App\page3.png')
