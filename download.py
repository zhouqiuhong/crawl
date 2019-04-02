# -*- coding:utf-8 -*-
import urllib.request
import requests
import re
import os
import json
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def save_file(urls, header):
    page_source = requests.get(urls, headers=header, verify=False)
    page_text = json.loads(page_source.text)
    audio_play = page_text['data']['tracksAudioPlay']
    try:
        if audio_play:
            for audio in audio_play:
                src_url = audio['src']
                path_name = audio['trackName']
                path_name = re.sub(r'\d{2}-\d{2}-\d{2}\s+\d{2}:\d{2}', '', path_name)

                album_name = audio['albumName']
                print("name = " + path_name + " album= " + album_name + " url = " + src_url)
                path = r'D:\RES\喜马拉雅音频' + "\\" + album_name
                # print(path)
                if not os.path.exists(path):
                    os.mkdir(path)
                urllib.request.urlretrieve(src_url, path + "\\" + path_name + '.m4a')
    except Exception as e:
        print(e)


list_id = ["6526615", "15143530", "6719079", "10237799", "6106909"]
# "https://www.ximalaya.com/revision/play/album?albumId=6719079&pageNum=1&sort=-1&pageSize=30"
start_urls = ["https://www.ximalaya.com/revision/play/album?albumId="+album_id+"&pageNum="+str(page)+
              "&sort=-1&pageSize=30" for album_id in list_id for page in range(1, 3)]

headers = {
        "Cookie": "_xmLog=xm_1526542504209_jha7zqq95jomel; "
                  "_ga=GA1.2.1966431376.1526542504; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1535003657; "
                  "Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1535003776",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      "Chrome/68.0.3440.106 Safari/537.36"
}
for url in start_urls:
    save_file(url, headers)
