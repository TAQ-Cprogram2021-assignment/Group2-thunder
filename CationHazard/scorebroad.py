import pygame.font


class Scoreboard:
    def __init__(self, ai_game):
        """初始化显示得分涉及的属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.stats
        # 显示得分信息时所使用的字体设置

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont("", 48)
        # 准备初始得分图像

        self.prep_score()

    def prep_score(self):
        """将得分转换为图像"""
        score_str = str(1)
        self.score_image = self.font.render(score_str, True, self.text_color, None)

        # 在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.ringt - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)

