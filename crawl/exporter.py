import json

file = open('hdoj.json')
text = json.loads(file.read())

file_obj = open('hdoj.csv', 'a')
file_obj.write('单词,次数\n')
for (k,v) in text.items():
    file_obj.write(k+','+str(v)+'\n')
file_obj.close()

