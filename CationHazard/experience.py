import pygame.font

from scoreboard import Scoreboard
from saving import Saving
from settings import Settings


class Experience:
    def __init__(self, ch_game):
        self.screen = ch_game.screen

        self.scoreboard = Scoreboard(ch_game)
        self.saving = Saving()

        self.exp = [0, 20, 50, 100, 200, 500]
        self.level = self.saving.level_output()
        self.now_exp = self.saving.exp_output()

        self.font = pygame.font.SysFont("", 24)

    def prep_level(self):
        self.scoreboard.prep_score()
        level_str = "Level: " + str(self.level)
        self.level_image = self.font.render(level_str, True, self.scoreboard.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.midbottom = self.scoreboard.score_rect.midbottom
        self.level_rect.top = self.scoreboard.highest_score_rect.bottom + self.level_rect.height * 5

    def prep_exp(self):
        exp_str = str(self.now_exp) + " / " + str(self.exp[self.level])
        self.exp_image = self.font.render(exp_str, True, self.scoreboard.text_color, None)
        self.exp_rect = self.exp_image.get_rect()
        self.exp_rect.midtop = self.level_rect.midbottom

    def show_level_exp(self):
        self.prep_level()
        self.prep_exp()
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.exp_image, self.exp_rect)

    def level_up(self):
        if self.now_exp == self.exp[self.level]:
            self.level += 1
            self.now_exp = 0
            self.saving.level_input(self.level)


class Coin:
    def __init__(self, ch_game):
        self.screen = ch_game.screen

        self.exp = Experience(ch_game)
        self.exp.prep_level()
        self.exp.prep_exp()
        self.scoreboard = Scoreboard(ch_game)
        self.saving = Saving()

        self.font = pygame.font.SysFont("", 24)

        self.coin = self.saving.golden_coin_output()

    def prep_coin_play(self, coin, stage):
        coin_str = ": " + str(coin)
        self.coin_num_image = self.font.render(coin_str, True, self.scoreboard.text_color, None)
        self.coin_num_rect = self.coin_num_image.get_rect()

        if stage == "play":
            self.coin_num_rect.midtop = self.exp.exp_rect.midbottom
            self.coin_num_rect.y += 20

        self.coin_image = pygame.image.load("materials/pictures/store/coin.png")

        if stage == "store":
            self.coin_num_rect.midtop = self.screen.get_rect().midtop
            self.coin_num_rect.y += 20

        self.coin_rect = self.coin_image.get_rect()
        self.coin_rect.midright = self.coin_num_rect.midleft


    def show_coin(self, coin, stage):
        self.prep_coin_play(coin, stage)
        self.screen.blit(self.coin_num_image, self.coin_num_rect)
        self.screen.blit(self.coin_image, self.coin_rect)


class Blood:
    def __init__(self, ch_game):
        self.screen = ch_game.screen

        self.scoreboard = Scoreboard(ch_game)
        self.settings = Settings()

        self.font = pygame.font.SysFont("", 24)

    def prep_blood(self, blood, max_blood):
        blood_str = "Blood: " + str(blood) + " / " + str(max_blood)
        self.blood_image = self.font.render(blood_str, True, self.scoreboard.text_color, None)
        self.blood_rect = self.blood_image.get_rect()
        self.blood_rect.x = self.screen.get_rect().width - self.blood_rect.width
        self.blood_rect.y = self.screen.get_rect().height // 2

    def show_blood(self, blood, max_blood):
        self.prep_blood(blood, max_blood)
        self.screen.blit(self.blood_image, self.blood_rect)



if __name__ == "__main__":
    pass
