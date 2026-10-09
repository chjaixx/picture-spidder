import requests
import re
import json
index=1
def get_html():
    url="https://www.maoyan.com/board/4?timeStamp=1786962120077&channelId=40011&index=4&signKey=3eee9ca0ff4391fcafc9b8365b736957&sVersion=1&webdriver=false&offset=0"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0",
        "cookie":"__mta=222780964.1789301424925.1789301449915.1789374162600.3; uuid_n_v=v1; uuid=17CF5AF0AF6C11F1A160757706DA47CE224B298821154FBC9DB2022776905CAE; WEBDFPID=z6v54xyx6wxx51z41306593uw4v468368z90zzw991067958498vuuv9-1789387824289-1789301423698AAUWSKIfd79fef3d01d5e9aadc18ccd4d0c95078578; utm_source_rg=AM%25oc5GLGj%25491%25zJYySENEJIEEyizSim7JyVmhISYSJ8mJ8zV7zzIVVi7J9Vy8SV8YhhYV; _ga=GA1.1.1522775682.1789301425; _lxsdk_cuid=1a09aad0284c8-072683be044fde-4c657b58-144000-1a09aad0284c8; _lxsdk=17CF5AF0AF6C11F1A160757706DA47CE224B298821154FBC9DB2022776905CAE; __mta=222780964.1789301424925.1789301424925.1789301424925.1; global-guide-isclose=true; _csrf=e536464007b6b6adcfee46843f03ae52bab188b2075e19479c905cc0a9ac7882; Hm_lvt_e0bacf12e04a7bd88ddbd9c74ef2b533=1789301424,1789374162; Hm_lpvt_e0bacf12e04a7bd88ddbd9c74ef2b533=1789374162; HMACCOUNT=297FA87751647C51; _ga_WN80P4PSY7=GS2.1.s1789374162$o3$g0$t1789374162$j60$l0$h0; _lxsdk_s=1a09f02e51d-30d-dff-976%7C%7C2"

    }
    resp=requests.get(url=url,headers=headers)
    resp.encoding=resp.apparent_encoding
    print(resp.status_code)
    print(resp.text)
    with open('maoya.text','w',encoding='utf-8')as f:
        f.write(resp.text)
        print("html页面文本写入成功！")
def data():
    s=open('maoya.text','r',encoding='utf-8')
    dj=re.compile(r' <div class="movie-item-info">.*?<a href="(.*?)" title="(.*?)".*?<p class="star">'
                  r'.*?主演：(.*?)</p>'
                  r'.*?<p class="releasetime">上映时间：(.*?)</p>'
                  r'.*?<p.*?<i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>',re.S)
    re_get = re.findall(dj,s.read())
    get_list = []
    u='https://www.maoyan.com'
    for i in re_get:
        get_dict = dict()
        global index
        get_dict['排名:'] = index
        get_dict['链接:'] = u+i[0]
        get_dict['名称'] = i[1]
        get_dict['主演：'] = re.sub(' |\n','',i[2])
        get_dict['上映时间：'] = i[3]
        get_dict['评分'] = i[4]+i[5]
        get_list.append(get_dict)
        index += 1
    with open('maoyan.json', 'w', encoding='utf-8') as f:
         f.write(json.dumps(get_list, ensure_ascii=False, indent=2))
    print('写入成功！')
    print(f"电影数量为:{index-1}")
if __name__ == '__main__':
    # get_html()
    data()