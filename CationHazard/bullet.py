import pygame

from pygame.sprite import Sprite
from player import Plane


class Bullet(Sprite):
    def __init__(self, ch_game):
        super().__init__()
        self.screen = ch_game.screen
        self.screen_rect = self.screen.get_rect()

        self.up_speed = 3

        self.plane = Plane(ch_game)


class Ba(Bullet, Sprite):
    def __init__(self, ch_game, rect):
        super().__init__(ch_game)
        self.image = pygame.image.load("materials/pictures/ion/Ba.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midtop = rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.up_speed
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
