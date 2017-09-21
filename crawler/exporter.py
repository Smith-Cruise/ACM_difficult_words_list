import json

data = open('../data/words_in_cet4_translated.json', encoding='utf-8').read()
word_list = json.loads(data)

csv_obj = open('words_in_cet4_translated.csv', 'a')
csv_obj.write('单词,解释,次数\n')
for each in word_list:
    csv_obj.write(each[0]+','+each[1]+','+str(each[2])+'\n')
csv_obj.close()

