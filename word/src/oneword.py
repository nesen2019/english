import os
import ast
import re
import playsound

from word.src.mp3 import play_mp3



# todo:
class OneWord:
    def __init__(self, word, path_mp3=None):
        self.__word = word
        self.__path_mp3 = path_mp3

    def play(self):
        if self.__word is None:
            return
        if self.__path_mp3 is None:
            play_mp3(word=self.__word)
        playsound.playsound(sound=self.__path_mp3)

    def __str__(self):
        return f"{self.__word}"



