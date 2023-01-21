from googletrans import Translator
from langdetect import detect


translator = Translator()


class Text:
    def initiate_text(filename):
        with open(f'{filename}', 'r') as text_source:
            raw_text = " ".join(text_source.readlines())

        return raw_text

    def language_detect(raw_text):
        lang_suppose = detect(raw_text)
        return lang_suppose

    def translate(raw_text, lang_suppose, dest=None):
        TARGET_LANG = 'en'
        translated_text = translator.translate(raw_text, src=lang_suppose, dest=TARGET_LANG)
        return translated_text


filename = 'Ohne dich'
income_file = f'{filename}.txt'
alien_text = Text.initiate_text(income_file)


def text_work():
    text_lang = Text.language_detect(alien_text)
    translated_text = str(Text.translate(alien_text, text_lang))
    write_to_file(translated_text)


def write_to_file(translated_text):
    with open(f'{filename}_translated.txt', 'w') as data:
        data.write(translated_text + '\n')

    compose_interlinear(income_file, f'{filename}_translated.txt')


def compose_interlinear(income_file, translated_file):
    with open(income_file, 'r') as file1, \
         open(translated_file, 'r') as file2, \
         open(f'{filename}_interlinear.txt', 'w') as file3:
        file3.write(f'The file was translated automatically.\n'
                    f'Source language is: {Text.language_detect(alien_text)}\n'
                    f'Translation language is English.')
        for p in zip(file1, file2):
            print(*map(lambda s: s.strip(), p), sep='\n', file=file3)


if __name__ == '__main__':
    text_work()
