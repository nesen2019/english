import os
import re
import random
import requests
import playsound
from requests_html import HTMLSession
from urllib.parse import parse_qs, urlparse

"""


"""
__all__ = [
    "get_mp3_url",  # (word, web_name) 获取mp3的网络地址
    "down_mp3",  # (url, path), # 下载url，mp3文件到path
    "play_mp3",  # 网络下载并播放
]


def random_name(n=5):
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return fr"mp3_{''.join(random.sample(H, n))}"


def play_mp3(word="a"):
    url_mp3 = get_mp3_url(word)
    path = down_mp3(url_mp3, path=None)
    playsound.playsound(path)
    os.remove(path=path)
    return True


def down_mp3(url=None, path=None):
    if url is None:
        url = r"https://media.merriam-webster.com/audio/prons/en/us/mp3/a/a0000001.mp3"
    if path is None:
        path = os.path.join(".", f"{random_name(n=4)}_{os.path.basename(url)}")
    res = requests.get(url, stream=True)

    with open(path, "wb") as f:
        for chunk in res.iter_content():
            f.write(chunk)
    return os.path.abspath(path)


def get_mp3_url(word, web_name="webster"):
    if web_name == "webster":  # https://www.merriam-webster.com/dictionary/mother
        url = r"https://www.merriam-webster.com/dictionary" + "/" + word
        session = HTMLSession()
        r = session.get(url)
        # print(url)
        sel = "#left-content > div.row.entry-attr > div > span.prs > a"
        results = r.html.find(sel)
        result = results[0]

        url_mp3 = re.findall(r"href='(.*?)'", str(result))
        if url_mp3:
            url_mp3 = url_mp3[0]
            # https://media.merriam-webster.com/audio/prons/en/us/mp3/a/a0000001.mp3
            mp3_name = parse_qs(urlparse(url_mp3).query).get("file", "")[0]
            pre_url = r"https://media.merriam-webster.com/audio/prons/en/us/mp3"

            url_mp3 = fr"{pre_url}/{mp3_name[0]}/{mp3_name}.mp3"
            return url_mp3
        else:
            raise ValueError("不存在 url_mp3")
