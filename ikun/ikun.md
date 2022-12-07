# IKUN修炼手册

首先使用getBVbykeyword获得ikun视频的bv号

然后使用bv2av函数获得av号

使用getcommentbyav利用av号和b站api接口获得评论

然后对获取的评论进行分析

* 词云分析
* 词语分析
* 更多分析



需要完成的任务

* [ ] getBVbykeyword中似乎不是按播放数排序
* [ ] getcommentbyav 写成函数，输入为av号，输出为av号.txt
* [ ] wordcloud
