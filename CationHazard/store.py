import pygame


class Store:
    def __init__(self, ch_game):
        self.screen = ch_game.screen
        self.screen_rect = self.screen.get_rect()

        self.return_image = pygame.image.load("materials/pictures/return.png").convert_alpha()
        self.return_rect = self.return_image.get_rect()
        self.return_rect.x = 0
        self.return_rect.y = 0

    def draw_attract_area_level(self):
        attract_area_level_image = pygame.image.load("materials/pictures/store/magnet.png").convert_alpha()
        attract_area_level_rect = attract_area_level_image.get_rect()
        attract_area_level_rect.x = 70
        attract_area_level_rect.y = 130
        self.screen.blit(attract_area_level_image, attract_area_level_rect)

    def draw_speed_level(self):
        speed_level_image = pygame.image.load("materials/pictures/store/speed_up.png").convert_alpha()
        speed_level_rect = speed_level_image.get_rect()
        speed_level_rect.x = 70
        speed_level_rect.y = 300
        self.screen.blit(speed_level_image, speed_level_rect)

    def draw_pere(self):
        title_image = pygame.image.load("materials/pictures/store/头头.png").convert_alpha()
        title_rect = title_image.get_rect()
        title_rect.x = 70
        title_rect.y = 450
        self.screen.blit(title_image, title_rect)

    def draw_timer(self):
        title_image = pygame.image.load("materials/pictures/store/头头.png").convert_alpha()
        title_rect = title_image.get_rect()
        title_rect.x = 300
        title_rect.y = 450
        self.screen.blit(title_image, title_rect)

    def draw_larger_tem(self):
        title_image = pygame.image.load("materials/pictures/store/头头.png").convert_alpha()
        title_rect = title_image.get_rect()
        title_rect.x = 300
        title_rect.y = 130
        self.screen.blit(title_image, title_rect)

    def draw_speed_tem(self):
        title_image = pygame.image.load("materials/pictures/store/头头.png").convert_alpha()
        title_rect = title_image.get_rect()
        title_rect.x = 300
        title_rect.y = 300
        self.screen.blit(title_image, title_rect)

    def draw_clear_tem(self):
        title_image = pygame.image.load("materials/pictures/store/头头.png").convert_alpha()
        title_rect = title_image.get_rect()
        title_rect.y = 300
        title_rect.x = 540
        self.screen.blit(title_image, title_rect)

    def draw_wushuang(self):
        title_image = pygame.image.load("materials/pictures/store/头头.png").convert_alpha()
        title_rect = title_image.get_rect()
        title_rect.x = 540
        title_rect.y = 130
        self.screen.blit(title_image, title_rect)

    def draw_yuzhi(self):
        title_image = pygame.image.load("materials/pictures/store/头头.png").convert_alpha()
        title_rect = title_image.get_rect()
        title_rect.x = 540
        title_rect.y = 450
        self.screen.blit(title_image, title_rect)

    def draw_return_button(self):
        self.screen.blit(self.return_image, self.return_rect)

    def draw(self):
        self.draw_attract_area_level()
        self.draw_speed_level()
        self.draw_pere()
        self.draw_timer()
        self.draw_larger_tem()
        self.draw_speed_tem()
        self.draw_clear_tem()
        self.draw_wushuang()
        self.draw_yuzhi()
        self.draw_return_button()

    def return_title(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.return_rect.collidepoint(mouse_pos):
            pass
