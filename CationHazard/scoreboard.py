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

        self.bullet_num = self.settings.bullet_num

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
        self.screen.blit(self.bullet_num_image, self.bullet_num_rect)

    def score_up(self):
        self.score += 233
        if self.score > self.highest_score:
            self.savings.highest_score_input(self.score)
            self.highest_score = self.score
