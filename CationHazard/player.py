import pygame

from pygame.sprite import Sprite


class Plane(Sprite):
    def __init__(self, ch_game):
        # 屏幕设置
        super().__init__()
        self.screen = ch_game.screen
        self.screen_rect = self.screen.get_rect()

        self.plane = pygame.image.load("materials/pictures/头头.png").convert_alpha()
        self.rect = self.plane.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.speed = 3
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def draw_plane(self):
        self.screen.blit(self.plane, self.rect)

    def update_ship(self):
        # 根据移动标志调整飞船位置
        # 更新飞船而不是rect对象的 x 值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.rect.x > 0:
            self.x -= self.speed
        if self.moving_up and self.rect.y > 0:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        # 根据 self.x 更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y
