import pygame


class Pictures:
    def __init__(self):
        self.logo = pygame.image.load("materials/pictures/logo/logo.ico")
        self.background = pygame.image.load("materials/pictures/background/bgbg.jpg")

        self.volume_image = pygame.image.load("../materials/pictures/setting/music_volume.png").convert_alpha()
        self.vol_plus_image = pygame.image.load("../materials/pictures/头头.png").convert_alpha()
        self.return_image = pygame.image.load("../materials/pictures/return.png").convert_alpha()
