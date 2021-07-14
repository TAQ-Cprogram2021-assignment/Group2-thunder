import pygame

from saving import Saving


class Settings:
    def __init__(self):
        self.logo = pygame.image.load("materials/pictures/logo/logo.ico")
        self.background = pygame.image.load("materials/pictures/background/bgbg.jpg")

        self.screen_size = pygame.Surface.get_size(self.background)

        self.saving = Saving()

        self.vol = 100.0
        self.text_color = (255, 255, 255)

        self.blood_level = self.saving.blood_level_output()
        self.blood = 100 + 50 * self.blood_level

        self.bullet_level = self.saving.bullet_level_output()

        # 初始化子弹
        self.bullet_num = self.bullet_level


class Musics:
    def __init__(self):
        pygame.mixer.init()  # 初始化

        self.settings = Settings()

        self.title_music = "materials/musics/Babe.mp3"

        self.play_music = "materials/musics/Blu.mp3"

    def play_title_music(self):
        pygame.mixer.music.load(self.title_music)  # 加载音乐
        pygame.mixer.music.play(-1)  # 播放

    def play_play_music(self):
        pygame.mixer.music.load(self.play_music)  # 加载音乐
        pygame.mixer.music.play(-1)  # 播放
