from translate import Translator
import OCR


class functionTranslate:
    def __init__(self):
        self.translator = Translator(to_lang="en")

    def JapaneseToEnglish(self, path):
        extractedText = OCR.extractText(path)
        if(extractedText != ""):
            extractedText = " ".join(extractedText)
            translatedText = self.translator.translate(extractedText)
            print(translatedText)


    def KoreanToEnglish(self, path):
        pass

    def SwedishToEnglish(self, path):
        pass


#obj1 = functionTranslate()
#obj1.JapaneseToEnglish('Translator App/page3.png')
#obj1.JapaneseToEnglish('Translator App/page2.png')