import pygame

from pictures import Pictures


class Settings:
    def __init__(self):
        pictures = Pictures()
        self.screen_size = pygame.Surface.get_size(pictures.background)

        self.vol = 100.0

        self.bullet_num = 0

        self.blood = 100
