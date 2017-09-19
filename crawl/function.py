import requests
import json
import enchant
from bs4 import BeautifulSoup


def wash(str_list):
    if not isinstance(str_list, list):
        raise TypeError('please use list type')

    word_list = []
    # filter invalid character
    temp_list = []
    for eachList in str_list:
        new_each_list = ''
        for index, each_char in enumerate(eachList):
            if text_is_valid(each_char):
                new_each_list = new_each_list + each_char
            elif 0 < index < len(eachList)-1:
                if text_is_valid(eachList[index-1]) and text_is_valid(eachList[index+1]):
                    new_each_list = new_each_list + ' '

        temp_list.append(new_each_list)

    # filter more space
    for eachList in temp_list:
        word_list.extend(eachList.split(' '))

    # filter empty word & length=2 word & invalid word
    dictionary = enchant.Dict('en_US')
    temp_list = word_list
    word_list = []
    for each_list in temp_list:
        if len(each_list) > 1 and dictionary.check(each_list):
            word_list.append(each_list)
    return word_list


def write_to_file(dict_data, file_name):
    file_obj = open(file_name, 'w')
    file_obj.write(json.dumps(dict_data))
    file_obj.close()


def text_is_valid(text):
    asc = ord(text)
    if 97 <= asc <= 122 or asc == 32 or asc == 39:
        return True
    else:
        return False


def get_remote_word_hdoj(url):
    """
    this rule for HangDian OJ
    """
    r = requests.get(url)
    text = r.text
    soup = BeautifulSoup(text, 'lxml')
    panel = soup.select('.panel_content')

    str_list = []
    # get title
    str_list.append(soup.h1.string)

    # get panel content
    for each in panel:
        for eachContent in each.contents:
            nav_str = eachContent.string
            if nav_str is not None:
                str_list.append(str.lower(nav_str))
    return str_list


def get_remote_word_zjoj(url):
    """
    this rule for ZheJiang OJ
    """
    r = requests.get(url)
    text = r.text
    soup = BeautifulSoup(text, 'lxml')
    content = soup.select('#content_body')[0]
    word_list = []
    for each in content.contents:
        if each.string is not None:
            word_list.append(each.string)
    return word_list


def get_remote_word_poj(url):
    """
    this rule for POJ
    """
    r = requests.get(url)
    text = r.text
    soup = BeautifulSoup(text, 'lxml')
    content = soup.select('.ptx')
    word_list = []
    for each_content in content:
        for each_contents in each_content.contents:
            if each_contents.string is not None:
                word_list.append(each_contents.string)
    return word_list


def get_remote_word_ural(url):
    """
    this rule for http://acm.timus.ru/problemset.aspx
    """
    r = requests.get(url)
    text = r.text
    soup = BeautifulSoup(text, 'lxml')
    content = soup.select('.problem_par_normal')
    word_list = []
    for each_content in content:
        for each_contents in each_content.contents:
            if each_contents.string is not None:
                word_list.append(each_contents.string)
    return word_list


def get_remote_word_dzkj(url):
    """
    http://acm.uestc.edu.cn/#/problem/show/1
    """
    r = requests.get(url)
    text = r.text
    temp_dict = json.loads(text)
    temp_dict = temp_dict['problem']
    str_list = [temp_dict['description'], temp_dict['input'], temp_dict['output']]
    return str_list


def get_remote_word_nbgc(url):
    """
    https://ac.2333.moe/Problem/view.xhtml?id=1000
    """
    r = requests.get(url)
    text = r.text
    soup = BeautifulSoup.select('.contents div')
