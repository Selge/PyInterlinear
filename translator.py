from googletrans import Translator
from langdetect import detect


TARGET_LANG = 'en'
translator = Translator()


def start_menu():
    print("""
    Welcome to PyTranslate!
    Please, choose one of the options below or push 'q' to quit the program:
    - 't' - to input text manually;
    - 'f' - to translate a .txt file.
    """)

    user_choice = str(input("Please, make a choice:  ")).lower()

    match user_choice:
        case 'q':
            exit()
        case 't':
            read_input()
        case 'f':
            read_from_file()
        case _:
            print("Please, use built-in options!")
            start_menu()


def read_input():
    raw_text = str(input("Please, enter your target text here:  "))

    language_detect(raw_text)


def read_from_file():
    raw_text = ''

    language_detect(raw_text)


def language_detect(raw_text):
    lang_suppose = detect(raw_text)

    translate(raw_text, lang_suppose)


def translate(alien_text, lang_suppose, dest=TARGET_LANG):
    translated_text = translator.translate(alien_text, src=lang_suppose, dest=dest)

    print("""Please, choose an output option:
             - 'f' - to write the result to file;
             - 'p' - to print the result to console;        
          """)

    write_to_file(translated_text)


def write_to_file(translated_text):
    ...


def print_result(translated_text):
    print(translated_text)


if __name__ == '__main__':
    start_menu()
