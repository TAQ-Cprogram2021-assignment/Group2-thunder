import pygame.font


class Texts:
    def __init__(self, ch_game):
        self.screen = ch_game.screen
        self.screen_rect = self.screen.get_rect()

    def draw_title(self):
        title_image = pygame.image.load("../materials/pictures/title/title.png").convert_alpha()
        title_rect = title_image.get_rect()
        title_rect.midtop = self.screen_rect.midtop
        title_rect.y = 100
        self.screen.blit(title_image, title_rect)


class Buttons:
    def __init__(self, ch_game):
        self.screen = ch_game.screen
        self.screen_rect = self.screen.get_rect()

        # play button
        self.play_button_image = pygame.image.load("../materials/pictures/title/startgame.png").convert_alpha()
        self.play_button_rect = self.play_button_image.get_rect()
        self.play_button_rect.midbottom = self.screen_rect.midbottom
        self.play_button_rect.y -= 550
        # store button
        self.store_button_image = pygame.image.load("../materials/pictures/title/store.png").convert_alpha()
        self.store_button_rect = self.store_button_image.get_rect()
        self.store_button_rect.midbottom = self.screen_rect.midbottom
        self.store_button_rect.y -= 450
        # setting button
        self.setting_button_image = pygame.image.load("../materials/pictures/title/setting.png").convert_alpha()
        self.setting_button_rect = self.setting_button_image.get_rect()
        self.setting_button_rect.midbottom = self.screen_rect.midbottom
        self.setting_button_rect.y -= 350
        # close button
        self.close_button_image = pygame.image.load("../materials/pictures/title/exitgame.png").convert_alpha()
        self.close_button_rect = self.close_button_image.get_rect()
        self.close_button_rect.midbottom = self.screen_rect.midbottom
        self.close_button_rect.y -= 250

    def play_button(self):
        self.screen.blit(self.play_button_image, self.play_button_rect)

    def setting_button(self):
        self.screen.blit(self.setting_button_image, self.setting_button_rect)

    def store_button(self):
        self.screen.blit(self.store_button_image, self.store_button_rect)

    def close_button(self):
        self.screen.blit(self.close_button_image, self.close_button_rect)

    def button(self):
        self.play_button()
        self.store_button()
        self.close_button()
        self.setting_button()


if __name__ == "__main__":
    pass
