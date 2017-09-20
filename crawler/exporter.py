import json
import function as tool

file1 = open('../data/acdream.json')
file2 = open('../data/acmhit.json')
file3 = open('../data/bj.json')
file4 = open('../data/dzkj.json')
file5 = open('../data/fz.json')
file6 = open('../data/hzdzkj.json')
file7 = open('../data/zj.json')

list_dict = []
list_dict.append(json.loads(file1.read()))
list_dict.append(json.loads(file2.read()))
list_dict.append(json.loads(file3.read()))
list_dict.append(json.loads(file4.read()))
list_dict.append(json.loads(file5.read()))
list_dict.append(json.loads(file6.read()))
list_dict.append(json.loads(file7.read()))

word_dict = {}
for each_dict in list_dict:
    for (k, v) in each_dict.items():
        if k not in word_dict:
            word_dict[k] = v
        else:
            word_dict[k] = word_dict[k] + v

sorted_list = sorted(word_dict.items(), key=lambda d:d[1], reverse=True)
word_dict.clear()
for i in sorted_list:
    word_dict[i[0]] = i[1]
tool.write_to_file(word_dict, 'all.json')


csv_obj = open('all.csv', 'a')
csv_obj.write('单词,次数\n')
for (k,v) in word_dict.items():
    csv_obj.write(k+','+str(v)+'\n')
csv_obj.close()

