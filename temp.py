from googletrans import Translator
from langdetect import detect


translator = Translator()


def translate():
    # raw_text = str(input("Please, enter your target text here:  "))
    raw_text = 'Ich werde in die Tannen gehen'
    lang_suppose = detect(raw_text)
    translated_text = translator.translate(raw_text, src=lang_suppose, dest='en')

    print(translated_text)


if __name__ == '__main__':
    translate()
