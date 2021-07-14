import pygame.font

from saving import Saving
from settings import Settings


class Scoreboard:
    def __init__(self, ai_game):
        """初始化显示得分涉及的属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.score = 0

        # 显示得分信息时所使用的字体设置
        self.text_color = (255, 255, 255)
        self.score_font = pygame.font.SysFont("", 48)
        self.level_font = pygame.font.SysFont("", 24)

        self.savings = Saving()
        self.settings = Settings()

        self.highest_score = self.savings.highest_score_output()
        self.level = self.savings.level_output()

    def prep_score(self):
        """将得分转换为图像"""
        highest_score_str = "Highest Score: " + str(self.highest_score)
        self.highest_score_image = self.score_font.render(highest_score_str, True, self.settings.text_color, None)
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.left = 0
        self.highest_score_rect.top = 20

        score_str = "score: " + str(self.score)
        self.score_image = self.score_font.render(score_str, True, self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = 0
        self.score_rect.top = self.highest_score_rect.top + self.highest_score_rect.height

        bullet_num_str = "Bullet: " + str(self.settings.bullet_num)
        self.bullet_num_image = self.score_font.render(bullet_num_str, True, self.text_color, None)
        self.bullet_num_rect = self.bullet_num_image.get_rect()
        self.bullet_num_rect.top = 20
        self.bullet_num_rect.right = self.screen_rect.right - 20

    def show_score(self):
        """在屏幕上显示得分"""
        self.prep_score()
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        self.screen.blit(self.score_image, self.score_rect)

    def draw_bullet_num(self, bullet_num):
        bullet_num_str = "Bullet: " + str(bullet_num)
        self.bullet_num_image = self.score_font.render(bullet_num_str, True, self.text_color, None)
        self.bullet_num_rect = self.bullet_num_image.get_rect()
        self.bullet_num_rect.top = 20
        self.bullet_num_rect.right = self.screen_rect.right - 20
        self.screen.blit(self.bullet_num_image, self.bullet_num_rect)

    def score_up(self):
        self.score += 233
        if self.score > self.highest_score:
            self.savings.highest_score_input(self.score)
            self.highest_score = self.score


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

    def prep_coin(self, coin, stage):
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
        self.prep_coin(coin, stage)
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
