from  googletrans import Translator
def trans(text_text,lang):
    if  lang == '':
        lang = 'ru'
    translator = Translator()
    r = translator.translate(text_text, dest=lang)

    print (f'Оригинальный текст: {r.origin}')
    print (f'Переведенный текст: {r.text}')
    return
