import pygame

from pictures import Pictures


class Settings:
    def __init__(self):
        pictures = Pictures()
        self.screen_size = pygame.Surface.get_size(pictures.background)

        self.vol = 100.0


class Setting:
    def __init__(self, ch_game):
        self.screen = ch_game.screen

        self.volume_image = pygame.image.load("../materials/pictures/setting/music_volume.png").convert_alpha()
        self.volume_rect = self.volume_image.get_rect()
        self.volume_rect.x = 70
        self.volume_rect.y = 100

        self.vol_plus_image = pygame.image.load("../materials/pictures/头头.png").convert_alpha()
        self.vol_plus_image_rect = self.vol_plus_image.get_rect()
        self.vol_plus_image_rect.x = self.vol_plus_image_rect.x + 300
        self.vol_plus_image_rect.y = self.volume_rect.y

        self.return_image = pygame.image.load("../materials/pictures/return.png").convert_alpha()
        self.return_rect = self.return_image.get_rect()
        self.return_rect.x = 0
        self.return_rect.y = 0

    def volume(self):
        self.screen.blit(self.volume_image, self.volume_rect)

    def volume_plus(self):
        self.screen.blit(self.vol_plus_image, self.vol_plus_image_rect)

    def sound_effects(self):
        sound_effects_image = pygame.image.load("../materials/pictures/setting/effect_volume.png").convert_alpha()
        sound_effects_rect = sound_effects_image.get_rect()
        sound_effects_rect.x = 70
        sound_effects_rect.y = 250
        self.screen.blit(sound_effects_image, sound_effects_rect)

    def resolving_power(self):
        resolving_power_image = pygame.image.load("../materials/pictures/return.png").convert_alpha()
        resolving_power_rect = resolving_power_image.get_rect()
        resolving_power_rect.x = 70
        resolving_power_rect.y = 400
        self.screen.blit(resolving_power_image, resolving_power_rect)

    def frame_rate(self):
        frame_rate_image = pygame.image.load("../materials/pictures/return.png").convert_alpha()
        frame_rate_rect = frame_rate_image.get_rect()
        frame_rate_rect.x = 70
        frame_rate_rect.y = 550
        self.screen.blit(frame_rate_image, frame_rate_rect)

    def return_button(self):
        self.screen.blit(self.return_image, self.return_rect)

    def draw(self):
        self.volume()
        self.volume_plus()
        self.sound_effects()
        self.resolving_power()
        self.frame_rate()
        self.return_button()


if __name__ == "__main__":
    # settings = Settings()
    pass
