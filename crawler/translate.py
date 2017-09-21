from googletrans import Translator


def translate(word):
    translator = Translator(service_urls=[
        'translate.google.cn',
    ])
    a = translator.translate('hello', dest='zh-CN', src='en')
    print(a.text)


translate('hello')



