import json

origin_data = open('../data/all.json')
stop_words_data = open('../data/stop_words.json')
origin_dict = json.loads(origin_data.read())
stop_words_list = json.loads(stop_words_data.read())

final_data = []
for key in list(origin_dict):
    if key not in stop_words_list:
        final_data.append((key, origin_dict[key]))


final_data.sort(key=lambda a:a[1], reverse=True)
file_obj = open('all_filter_by_stop_words.json', 'w')
file_obj.write(json.dumps(final_data))
file_obj.close()