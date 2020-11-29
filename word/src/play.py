import os
import re

import playsound
import ast
import time
from .mp3 import *

def play_list_word(path_txt):
    data = list()
    with open(path_txt, "r") as f:
        data = ast.literal_eval(f.read())

    for d in data:
        print(d["word"])
        time.sleep(0.1)
        playsound.playsound(d["path_mp3"])


def play_list_from_web(path_txt):
    with open(path_txt, "r") as f:
        data = f.read().strip()
        data_list = re.findall(r"[-a-zA-Z]+", data)
    print(data_list)
    for word in data_list:
        print(word)
        time.sleep(0.2)
        try:
            play_mp3(word)
        except:
            print(f'error: word={word}... ')


