

import os
import glob
import json


if __name__ == '__main__':

    with open("word/3Kwords.md", "w") as f:
        f.write(f"\n\n")
        for i in range(1, 32):
            f.write(f"### [Music_{i:02}](http://download.dogwood.com.cn/online/yaoniming3000/{i:02}.mp3), [text_{i:02}](./word/text/list{i:02}.txt)")
            f.write(f"\n")


