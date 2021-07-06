import pygame
import pygame.font

from settings import Settings


class Store:
    def __init__(self, ch_game):
        self.screen = ch_game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = Settings()

        self.font = pygame.font.SysFont("", 24)

        self.return_image = pygame.image.load("materials/pictures/return.png").convert_alpha()
        self.return_rect = self.return_image.get_rect()
        self.return_rect.x = 0
        self.return_rect.y = 0

        self.attract_area_level_image = pygame.image.load("materials/pictures/store/magnet.png").convert_alpha()
        self.attract_area_level_rect = self.attract_area_level_image.get_rect()
        self.attract_area_level_rect.x = 70
        self.attract_area_level_rect.y = 130

        self.speed_level_image = pygame.image.load("materials/pictures/store/speed_up.png").convert_alpha()
        self.speed_level_rect = self.speed_level_image.get_rect()
        self.speed_level_rect.x = 70
        self.speed_level_rect.y = 300

        self.bullet_up_image = pygame.image.load("materials/pictures/store/bullet_up.png").convert_alpha()
        self.bullet_up_rect = self.bullet_up_image.get_rect()
        self.bullet_up_rect.x = 70
        self.bullet_up_rect.y = 450

        self.blood_up_image = pygame.image.load("materials/pictures/store/blood.png").convert_alpha()
        self.blood_up_rect = self.blood_up_image.get_rect()
        self.blood_up_rect.x = 300
        self.blood_up_rect.y = 450

    def draw_bullet_level(self, bullet_level):
        bullet_level_str = "Bullet Level: " + str(bullet_level)
        self.bullet_level_image = self.font.render(bullet_level_str, True, self.settings.text_color, None)
        self.bullet_level_rect = self.bullet_level_image.get_rect()
        self.bullet_level_rect.midtop = self.bullet_up_rect.midbottom
        self.screen.blit(self.bullet_level_image, self.bullet_level_rect)

        bullet_up_need_str = "NEED: " + str(20 + 5 * (bullet_level ** 2))
        self.bullet_up_need_image = self.font.render(bullet_up_need_str, True, self.settings.text_color, None)
        self.bullet_up_need_rect = self.bullet_up_need_image.get_rect()
        self.bullet_up_need_rect.midtop = self.bullet_level_rect.midbottom
        self.screen.blit(self.bullet_up_need_image, self.bullet_up_need_rect)

    def draw_blood_level(self, blood_level):
        blood_level_str = "Blood Level: " + str(blood_level)
        self.blood_level_image = self.font.render(blood_level_str, True, self.settings.text_color, None)
        self.blood_level_rect = self.blood_level_image.get_rect()
        self.blood_level_rect.midtop = self.blood_up_rect.midbottom
        self.screen.blit(self.blood_level_image, self.blood_level_rect)

        self.blood_up_need_str = "NEED: " + str(20 + 5 * (blood_level ** 2))
        self.blood_up_need_image = self.font.render(self.blood_up_need_str, True, self.settings.text_color, None)
        self.blood_up_need_rect = self.blood_up_need_image.get_rect()
        self.blood_up_need_rect.midtop = self.blood_level_rect.midbottom
        self.screen.blit(self.blood_up_need_image, self.blood_up_need_rect)

    def draw(self):
        self.screen.blit(self.attract_area_level_image, self.attract_area_level_rect)
        self.screen.blit(self.speed_level_image, self.speed_level_rect)
        self.screen.blit(self.bullet_up_image, self.bullet_up_rect)
        self.screen.blit(self.blood_up_image, self.blood_up_rect)
        self.screen.blit(self.return_image, self.return_rect)


if __name__ == "__main__":
    pass
