import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ch_game, sprite):
        super().__init__()
        self.screen = ch_game.screen
        self.rect = sprite.get_rect()
        self.y = float(self.rect.y)

        self.up_speed = 0.3

    def update(self):
        self.y -= self.up_speed
        self.rect.y = self.y
