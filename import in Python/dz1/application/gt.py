from  googletrans import Translator
def trans(text_text,):
    translator = Translator()
    r = translator.translate(text_text, dest='ru')
    print (f'Оригинальный текст: {r.origin}')
    print (f'Переведенный текст: {r.text}')
    return

