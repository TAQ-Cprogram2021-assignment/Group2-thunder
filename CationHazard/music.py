# import pygame.mixer
#
#
# class Musics:
#     def __init__(self):
#         pygame.mixer.init()
#         self.title_music = "materials/musics/NightTheater.ogg"
#
#
# if __name__ == "__main__":
#     musics = Musics()
#     pygame.mixer.music.load(musics.title_music)
#     pygame.mixer.music.play(start=0.0)

import pygame
import time

from settings import Settings


class Musics:
    def __init__(self):
        pygame.mixer.init()  # 初始化

        self.settings = Settings()

        self.title_music = "materials/musics/Babe.mp3"

        self.play_music = "materials/musics/NightTheater.ogg"

    def play_title_music(self):
        pygame.mixer.music.load(self.title_music)  # 加载音乐
        pygame.mixer.music.play(-1)  # 播放

    def play_play_music(self):
        pygame.mixer.music.load(self.play_music)  # 加载音乐
        pygame.mixer.music.play(-1)  # 播放


if __name__ == "__main__":
    musics = Musics()
    musics.play_title_music()
    pygame.mixer.music.set_volume(1)
    while True:
        userIn = input()  # 输入空格暂停
        if userIn == ' ':
            pygame.mixer.music.pause()
            break
        else:
            time.sleep(207)  # 表示音频的长度
    pygame.mixer.music.stop()
