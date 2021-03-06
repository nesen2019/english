import os
import re
import time
import tqdm
import json
from .mp3 import *

__all__ = [
    "update_for_text_mp3",  # 更新list..文件的MP3文件， 及能快速找到MP3文件
]


def update_for_text_mp3(list_name, dir_mp3=None, is_down_delay=0.5):
    import warnings
    warnings.filterwarnings("ignore")
    if dir_mp3 is None:
        dir_mp3 = "."
    with open(list_name, "r") as f:
        data = f.read().strip()
        data_list = re.findall(fr"[-a-zA-Z]+", data)
    new_data_list = list()

    def get_path(word, n_circle=0):
        try:
            url_mp3 = get_mp3_url(word)
            name_1 = os.path.basename(url_mp3)
            name_2 = os.path.basename(os.path.dirname(url_mp3))
            local_dir = os.path.join(dir_mp3, name_2)
            if not os.path.exists(local_dir):
                os.makedirs(local_dir)
            path = down_mp3(url_mp3, path=os.path.join(local_dir, name_1))
        except:
            if n_circle > 2:
                return None
            else:
                time.sleep(2)
                path = get_path(word, n_circle + 1)
        return path

    for word in tqdm.tqdm(data_list):
        if is_down_delay:
            time.sleep(float(is_down_delay))
        path = get_path(word)
        if path is None:
            path = get_path(word="error")
            print(f"error: {word}")
        new_data_list.append(dict(
            word=word,
            path_mp3=path
        ))
    with open(fr"{os.path.dirname(list_name)}/mp3_{os.path.basename(list_name)}", "w") as f:
        f.write(json.dumps(new_data_list, indent=2))
