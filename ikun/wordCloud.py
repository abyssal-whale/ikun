import csv
import os
import random
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as image
import pandas as pd

def wordList(file,filepath):
    #file='/897884618.csv'
    #filepath='./bilibilicomments/897884618.csv'
    pureCommentPath = './pureComment'

    csvfile = open(filepath, 'r')

    reader = csv.reader(csvfile)
    #print("open " + filepath)
    # for row in reader:
    #     if len(row)!=3:
    #         print(len(row))

    commentCol = [row[1] for row in reader]
    csvfile.close()
    filepath = pureCommentPath + "./"+file
    pureCommentF = open(filepath, 'w')
    for line in commentCol:
        pureCommentF.write(line + '\n')
    pureCommentF.close()

    f = open(filepath, 'r', encoding='gbk')
    text = f.read()
    f.close()
    #print("开始分词")
    jieba.add_word('爱坤')
    jieba.add_word('ikun')
    jieba.add_word('IKUN')
    jieba.add_word('只因')
    jieba.add_word('你干嘛')
    jieba.add_word('鸡你太美')
    jieba.add_word('小黑子')
    jieba.add_word('rap')
    jieba.add_word('只因')
    jieba.add_word('坤坤')
    jieba.add_word('蔡徐坤')
    jieba.add_word('cxk')
    jieba.add_word('CXK')
    jieba.add_word('虾头')
    jieba.add_word('蒸虾头')
    jieba.add_word('绿尸寒')
    jieba.add_word('两年半')
    jieba.add_word('哎呦')

    cut_text = jieba.lcut(text)  # 中文分词
    stops_word = open('stopwords1.txt', 'r', encoding='UTF-8').read()
    other_stop = {"哈哈哈", "哈哈", "哈哈哈哈", "\n", "_", " ", "doge", "脱单"}
    stop_list = stops_word.split()
    stop_all = set(stop_list).union(set(stop_list), other_stop)
    word_list = [element for element in cut_text if element not in stop_all]
    #print(word_list)
    return word_list

def wordCloud(word_list):
    # 之后来实现对于词频的统计
    word_dict = {}
    word_lists = []
    for word in word_list:
        if len(word) == 1:
            continue
        else:
            word_lists.append(word)
            word_dict[word] = word_dict.get(word, 0) + 1

    wd = list(word_dict.items())  # 使字典列表化
    wd.sort(key=lambda x: x[1], reverse=True)  # 排序
    #for i in range(50):  # 生成前五十个高频的词
    #    print(wd[i])
    #print(wd)
    word_csv = wd  # 将结果写入到csv文件当中
    #frequencyPath="./frequency"+file[:-4]+".csv"
    pd.DataFrame(data=word_csv[0:50]).to_csv("frequency.csv", encoding='UTF-8')
    print("已经完成词频统计,可在文件夹wordcloud.png中查看词云")
    string = " ".join(word_lists)  # 拼接为字符串
    w = WordCloud(background_color="white", font_path="C:\Windows\Fonts\STXINWEI.TTF",
                  width=1000, height=700, random_state=42)
    w.generate(string)
    #print(string)
    #wordCloudPath="./wordCloud"+file[:-4]+".png"
    w.to_file("wordcloud.png")



path="./bilibilicomments"
word_list=[]
for root,dirs,files in os.walk(path):
    for file in files:
        filepath= path+'/'+file
        #print(file,filepath)
        #print(word_list)
        try:
            word_list.extend(wordList(file,filepath))
        except:
            print("error:"+filepath)
wordCloud(word_list)


#wordCloud('/897884618.csv','./bilibilicomments/897884618.csv')



