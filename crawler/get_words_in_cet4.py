import json


origin_data = open('../data/all_filter_by_stop_words.json').read()
cet4_data = open('../data/cet4.json').read()

origin_list = json.loads(origin_data)
cet4_list = json.loads(cet4_data)
final_list = []

for each in origin_list:
    if each[0] in cet4_list:
        final_list.append((each[0], each[1]))

final_list.sort(key=lambda a:a[1], reverse=True)
file_obj = open('words_in_cet4.json', 'w')
file_obj.write(json.dumps(final_list))
file_obj.close()