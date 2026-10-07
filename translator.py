from translate import Translator

translator = Translator(to_lang="ja") 
#https://en.wikipedia.org/wiki/ISO_639-1
#Examples: (e.g. en, ja, ko, pt, zh, zh-TW, ...)

try:
    with open(r" python/Translate source.txt", "r", encoding="utf-8") as file:
        text = file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as e:
    print(f"The file was not found: {e}")
