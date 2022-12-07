import requests
import re
import copy

KEY_WORD = 'ikun'

## https://search.bilibili.com/all?vt=51487352&keyword=ikun&order=click
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

# https:%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F&from_source=webtop_search&spm_id_from=333.1007&search_source=3
# https://www.bilibili.com/video/BV11e4y1p7EY/?spm_id_from=333.1007.tianma.2-1-3.click
# https://www.bilibili.com/video/BV1hD4y1b7Aq/?spm_id_from=333.1007.tianma.3-1-5.click
# 获取BV号
def getBvByKey(key_word):
    url = 'https://search.bilibili.com/all?keyword=' + key_word + '&order=click'
    # url = 'https://search.bilibili.com/all?keyword=' + key_word + '&order=click'
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    html = r.text
    # print(html)

    #print(html)
    bv1=[]
    bv2=[]
    num = []
    #pattern方法
    pattern = re.compile(r'bvid:"BV(.*?)"')
    pattern2= re.compile(r'play:"[0-9]"')

    bv1 = re.findall(pattern, html)
    # num = re.findall(pattern2,html)
    # print(num)
    # 保存html
    with open('myhtml.txt', 'w', encoding='utf-8') as f:
        f.write(html)
    print(bv1)
    print(len(bv1))
    #正则表达式求得bv号
    bv2 = re.findall(r'BV[0-9a-zA-Z]+', html)
    num = re.findall(',play:[0-9]*',html)
    print('*****')
    print(num)
    print(len(num))
    print('*****')
    for i in range(0,len(num)):
        num[i] = int(num[i][6:-1])
    print(num)
    print(type(num))
    num2 = copy.deepcopy(num)
    num2.sort(reverse=True)
    print(num2)
    print(type(num2))
    bv_sort = []
    for i in range(0,len(num2)):
        index = num.index(num2[i])
        bv_sort.append(bv1[index])
    print("看这里")
    print(bv_sort)     #按播放量排序的BV号
    #print(type(bv_sort))
    #print(bv_sort)


    #print(len(bv2))
    #print(bv2)
    return bv_sort





if __name__ == '__main__':
    bv = getBvByKey(KEY_WORD)
    #print(bv)
