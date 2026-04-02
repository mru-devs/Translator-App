from google import genai
import KEYAPI

class LLM:

    language = 'English'
    def __init__(self, key):

        self.client = genai.Client(api_key = key)
        
        self.language = 'English'
        self.text = 'Detta är bara ett exempeltext som ska användas för LLM översättning. Vad kommer resultatet att bli?'
        self.response = self.client.models.generate_content(
            model="gemini-2.5-flash", contents=f'Strictly print out the translation of this {self.text} this to {self.language}'
        )

        self.printText()

    
    def printText(self):
        print(self.response.text)

    def selectedLanguage(text):
        language = text
    

obj1 = LLM(KEYAPI.KEY)




