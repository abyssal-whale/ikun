import requests, json
import pandas as pd

url = 'https://search.bilibili.com/all?keyword=ikun'
headers = {
    'Host': 'api.bilibili.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
    'Cookie': 'LIVE_BUVID=AUTO4816045004577327; video_page_version=v_old_home; buvid4=2BA5C346-AFE4-A698-46F7-F9C08CAB222D11636-022020319-Gi/v/ckjKgcgTi4cH7teqA%3D%3D; nostalgia_conf=-1; fingerprint3=88ea26d5472f78ee577e9baf50331ad6; PVID=1; is-2022-channel=1; buvid3=A9D8F822-EE77-8D77-1E92-EE1BDB559A7E63508infoc; i-wanna-go-back=-1; CURRENT_BLACKGAP=0; rpdid=|(k|km)mY~Yu0J\'uYRmm|)YYk; buvid_fp_plain=undefined; buvid_fp=A9D8F822-EE77-8D77-1E92-EE1BDB559A7E63508infoc; blackside_state=0; b_ut=5; hit-dyn-v2=1; CURRENT_QUALITY=120; fingerprint=a90eb4c44a2277cac36bb52142ee5bb5; DedeUserID=9591826; DedeUserID__ckMd5=208182aa2f12e081; b_nut=100; bp_video_offset_9591826=717514908782035000; theme_style=light; SESSDATA=3e7a5396%2C1683636520%2C4a730%2Ab1; bili_jct=94dd7acb36f0af8d80c24dc5e7fe334e; sid=83puvjqc; bntyh_content4=2022-11-10; innersign=0; CURRENT_FNVAL=16'
}

title_list, like_list, play_list = [],[],[]

def getdata():
    res = requests.get(url, headers=headers).content.decode('utf-8')
    jsonfile = json.loads(res)
    if (jsonfile['data']):
    		# 爬取内容，根据你想要的内容更改列表和标签
        for content in jsonfile['data']['result']:
            title_list.append(content['title'])
            like_list.append(content['like'])
            play_list.append(content['play'])

getdata()
Data = {
    '标题': title_list,
    '播放量': play_list,
    '点赞量': like_list
}
dataframe = pd.DataFrame(Data=data)
dataframe.to_excel('./数据.xlsx', index=False, encoding='utf-8')
print("end")
