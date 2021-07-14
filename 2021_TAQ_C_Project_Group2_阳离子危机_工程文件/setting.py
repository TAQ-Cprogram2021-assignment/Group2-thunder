import pygame


class Setting:
    def __init__(self, ch_game):
        self.screen = ch_game.screen

        self.volume_image = pygame.image.load("materials/pictures/setting/music_volume.png").convert_alpha()
        self.vol_plus_image = pygame.image.load("materials/pictures/头头.png").convert_alpha()
        self.return_image = pygame.image.load("materials/pictures/return.png").convert_alpha()

        self.volume_rect = self.volume_image.get_rect()
        self.volume_rect.x = 70
        self.volume_rect.y = 100

        self.vol_plus_image_rect = self.vol_plus_image.get_rect()
        self.vol_plus_image_rect.x = self.vol_plus_image_rect.x + 300
        self.vol_plus_image_rect.y = self.volume_rect.y

        self.sound_effects_image = pygame.image.load("materials/pictures/setting/effect_volume.png").convert_alpha()
        self.sound_effects_rect = self.sound_effects_image.get_rect()
        self.sound_effects_rect.x = 70
        self.sound_effects_rect.y = 250

        self.resolving_power_image = pygame.image.load("materials/pictures/return.png").convert_alpha()
        self.resolving_power_rect = self.resolving_power_image.get_rect()
        self.resolving_power_rect.x = 70
        self.resolving_power_rect.y = 400

        self.frame_rate_image = pygame.image.load("materials/pictures/return.png").convert_alpha()
        self.frame_rate_rect = self.frame_rate_image.get_rect()
        self.frame_rate_rect.x = 70
        self.frame_rate_rect.y = 550

        self.return_rect = self.return_image.get_rect()
        self.return_rect.x = 0
        self.return_rect.y = 0

    def draw(self):
        self.screen.blit(self.volume_image, self.volume_rect)
        self.screen.blit(self.vol_plus_image, self.vol_plus_image_rect)
        self.screen.blit(self.sound_effects_image, self.sound_effects_rect)
        self.screen.blit(self.resolving_power_image, self.resolving_power_rect)
        self.screen.blit(self.frame_rate_image, self.frame_rate_rect)
        self.screen.blit(self.return_image, self.return_rect)


if __name__ == "__main__":
    pass
