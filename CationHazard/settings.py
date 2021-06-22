import pygame

from pictures import Pictures
from saving import Saving


class Settings:
    def __init__(self):
        pictures = Pictures()
        self.screen_size = pygame.Surface.get_size(pictures.background)

        self.saving = Saving()

        self.vol = 100.0
        self.text_color = (255, 255, 255)

        self.init_bullet_num = self.saving.level_output()
        # 初始化子弹
        self.bullet_num = self.init_bullet_num

        self.blood = 100

        self.bullet_level = 0
