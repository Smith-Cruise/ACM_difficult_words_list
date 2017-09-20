import json
import function as tool

data = open('../data/words_in_cet6.json').read()
word_list = json.loads(data)

csv_obj = open('words_in_cet6.csv', 'a')
csv_obj.write('单词,次数\n')
for each in word_list:
    csv_obj.write(each[0]+','+str(each[1])+'\n')
csv_obj.close()

