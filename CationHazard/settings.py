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

        self.blood_level = self.saving.blood_level_output()

        self.blood = 100 + 20 * self.blood_level

        self.bullet_level = self.saving.bullet_level_output()

        # 初始化子弹
        self.bullet_num = self.bullet_level
