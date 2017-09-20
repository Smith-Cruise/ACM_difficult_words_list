import function as my_tool
import threading

lock_task = threading.Lock()
lock_list = threading.Lock()
task_id = 1001
task_end_id = 3262
word_dict = {}
word_list = []
thread_number = 20


def get_task():
    global task_id
    if task_id >= task_end_id:
        return 0
    lock_task.acquire()
    temp_id = task_id
    task_id = task_id+1
    lock_task.release()
    return temp_id


def catch():
    temp_id = get_task()
    retry = 0
    while temp_id != 0:
        try:
            temp_list = my_tool.get_remote_word_acmhit('http://acm.hit.edu.cn/hojx/showproblem/'+str(temp_id))
            print('success', temp_id)
            write_to_list(temp_list)
            temp_id = get_task()
        except Exception:
            print('fail', temp_id, 'retry', retry)
            if retry >= 5:
                temp_id = get_task()
            else:
                retry = retry + 1


def write_to_list(temp_list):
    lock_list.acquire()
    word_list.extend(temp_list)
    lock_list.release()


threads = []
for i in range(thread_number):
    t = threading.Thread(target=catch)
    t.start()
    threads.append(t)


for t in threads:
    t.join()


print('start process')
washed_list = my_tool.wash(word_list)
for word in washed_list:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        times = word_dict[word]
        word_dict[word] = times + 1

sorted_list = sorted(word_dict.items(), key=lambda d:d[1], reverse=True)
word_dict.clear()
for i in sorted_list:
    word_dict[i[0]] = i[1]

my_tool.write_to_file(word_dict, 'acmhit.json')
print('end process')