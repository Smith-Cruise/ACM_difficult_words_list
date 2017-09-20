# ACM_difficult_words_list
### 简易说明 Simple introduce

所有数据全部来源于各大ACM网站，并且已经按照单词出现次数从高到低排序，采集题目总数18317题。data目录为采集到的单词数据，crawler为爬虫源文件。

### 数据来源 Data source

| 来源       | 网址                                       | 对应文件名(data目录) | 题数    |
| -------- | ---------------------------------------- | ------------- | ----- |
| 杭州电子科技大学 | http://acm.hdu.edu.cn/listproblem.php?vol=1 | hzdzkj.json   | 5216  |
| 浙江大学     | http://acm.zju.edu.cn/onlinejudge/       | zj.json       | 2977  |
| 北京大学     | http://poj.org/                          | bj.json       | 3054  |
| 电子科技大学   | http://acm.uestc.edu.cn/#/               | dzkj.json     | 1753  |
| 福州大学     | http://acm.fzu.edu.cn/index.php          | fj.json       | 1283  |
| AcDream  | http://acdream.info/problem/list         | acdream.json  | 773   |
| acm hit  | http://acm.hit.edu.cn/hojx/problem/      | acmhit.json   | 3261  |
| 全部集合     |                                          | all.json      | 18317 |

### 数据说明

| 文件名                           | 说明            |
| ----------------------------- | ------------- |
| all.json                      | 所有单词数据，未处理    |
| all_filter_by_stop_words.json | 所有单词数据，过滤停用词  |
| cet4.json                     | 4级单词词汇        |
| cet6.json                     | 6级单词词汇        |
| stop_words.json               | 停用词列表         |
| words_in_cet4.json            | 在4级词汇表中的ACM词汇 |
| words_in_cet6.json            | 在6级词汇表中的ACM词汇 |



### 数据下载地址

`json`数据请去`data`目录下载

`csv`文件请去`release`下载，`release`中只提供`all_filter_by_stop_words.json`,`words_in_cet4.json`,`words_in_cet6.json`的csv文件，如有需要，请自行写`python`语言，范本在`exporter.py`中