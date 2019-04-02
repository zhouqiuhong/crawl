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
    audio_play = page_text['data']
    try:
        if audio_play:
            for audio in audio_play:
                src_url = "https://od.qingting.fm/" + audio['file_path']
                path_name = audio['name']
                path_name = re.sub(r'\d{2}-\d{2}-\d{2}\s+\d{2}:\d{2}', '', path_name)

                album_name = re.findall("【.*】", path_name)[0]
                print("name = " + path_name + " album= " + album_name + " url = " + src_url)
                path = r'D:\RES\蜻蜓电台音频' + "\\" + album_name
                # print(path)
                if not os.path.exists(path):
                    os.mkdir(path)
                urllib.request.urlretrieve(src_url, path + "\\" + path_name + '.m4a')
    except Exception as e:
        print(e)


list_id = ["237492", "237542"]  #专辑id

start_urls = ["https://i.qingting.fm/wapi/channels/"+album_id+"/programs/page/"+str(page) + "/pagesize/10"
              for album_id in list_id for page in range(1, 5)]#目标地址

headers = {
        "Cookie": "_xmLog=xm_1526542504209_jha7zqq95jomel; "
                  "_ga=GA1.2.1966431376.1526542504; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1535003657; "
                  "Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1535003776",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      "Chrome/68.0.3440.106 Safari/537.36"
}
for url in start_urls:
    save_file(url, headers)
