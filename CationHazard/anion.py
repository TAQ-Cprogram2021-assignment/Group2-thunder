import pygame
import random

from pygame.sprite import Sprite


class Anion(Sprite):
    def __init__(self, ch_game):
        super().__init__()
        self.screen = ch_game.screen
        self.screen_rect = self.screen.get_rect()

        self.down_speed = 0.7


class SO4(Anion, Sprite):
    def __init__(self, ch_game):
        super().__init__(ch_game)
        self.image = pygame.image.load("materials/pictures/ion/SO4.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = \
            random.randint(0, self.screen_rect.width - self.rect.width), random.randint(-5 * self.rect.height, 0)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.down_speed
        self.rect.y = self.y
