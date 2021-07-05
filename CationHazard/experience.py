import pygame.font

from scoreboard import Scoreboard
from saving import Saving


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
    def _init__(self, ch_game):
        self.screen = ch_game.screen

        self.scoreboard = Scoreboard(ch_game)
        self.saving = Saving()

        self.font = pygame.font.SysFont("", 24)

        self.coin = self.saving.golden_coin_output()


if __name__ == "__main__":
    pass
