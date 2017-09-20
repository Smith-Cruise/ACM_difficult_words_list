from googletrans import Translator
import json
import threading


get_lock = threading.Lock()
write_lock = threading.Lock()
word_dict = json.loads(open('../data/acdream.json').read())
word_key_list = list(word_dict)
start = 0
end = len(word_key_list)


def getTask():
    global start

# def translate():
#     translator = Translator(service_urls=[
#         'translate.google.cn',
#     ])
#     for t in range(100):
#         a = translator.translate('hello', dest='zh-CN', src='en')
#         print(a.text)
#
#
# for i in range(50):
#     threading.Thread(target=translate).start()
