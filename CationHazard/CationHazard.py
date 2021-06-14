"""

"""

import pygame
import sys
import time

from pictures import Pictures
from music import Musics
from player import Plane
from settings import Settings

from titles import Texts
from titles import Buttons
from store import Store
from setting import Setting
import scorebroad

from cation import Ba
from anion import SO4


class CationHazard:
    def __init__(self):
        # 初始化背景设置
        pygame.init()
        self.start_time = time.time()

        self.settings = Settings()
        self.pictures = Pictures()

        # 创建显示窗口
        pygame.display.set_icon(self.pictures.logo)
        pygame.display.set_caption("Cation Hazard")
        self.screen = pygame.display.set_mode(self.settings.screen_size)

        # 创建设置、图片实例
        self.setting = Setting(self)
        self.musics = Musics()

        # 创建文字实例
        self.texts = Texts(self)
        self.buttons = Buttons(self)
        self.store = Store(self)
        self.score_broad = scorebroad.Scoreboard(self)

        # 创建飞船实例
        self.player = Plane(self)

        self.title_display = True
        self.play_game = False
        self.store_display = False
        self.setting_display = False

        self.cations_in = pygame.sprite.Group()
        self.anions_in = pygame.sprite.Group()
        self.cations_shoot = pygame.sprite.Group()

    def run_game(self):
        # 绘制屏幕并显示
        self.screen.blit(self.pictures.background, (0, 0))
        pygame.display.flip()
        self.musics.play_music()

        while True:
            self.check_events()

            if self.title_display:
                # 如果绘制标题flag为True则绘制
                self._title_display()
            if self.play_game:
                self._play_game()
            if self.store_display:
                self._store_display()
            if self.setting_display:
                self._setting_display()

            pygame.mixer.music.set_volume(self.settings.vol)
        # pygame.display.flip()

    def _title_display(self):
        self.screen.blit(self.pictures.background, (0, 0))
        self.texts.draw_title()
        self.buttons.button()
        pygame.display.flip()

    def check_events(self):
        # 响应键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.title_display:
                    self.check_mouse_button_down_events(mouse_pos)

    def keydown_events(self, event):
        # 响应键盘按下事件
        # keys = pygame.key.get_pressed()
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_s:
            self.title_display = False

        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.player.moving_left = True
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.player.moving_up = True
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.player.moving_down = True

    def keyup_events(self, event):
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.player.moving_left = False
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.player.moving_up = False
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.player.moving_down = False

    def check_mouse_button_down_events(self, mouse_pos):
        play_clicked = self.buttons.play_button_rect.collidepoint(mouse_pos)
        setting_clicked = self.buttons.setting_button_rect.collidepoint(mouse_pos)
        store_clicked = self.buttons.store_button_rect.collidepoint(mouse_pos)
        exit_clicked = self.buttons.close_button_rect.collidepoint(mouse_pos)

        if play_clicked:
            self.title_display, self.play_game = False, True
        elif setting_clicked:
            self.title_display, self.setting_display = False, True
        elif store_clicked:
            self.title_display, self.store_display = False, True
        elif exit_clicked:
            sys.exit()

    def _play_game(self):
        pygame.mixer.music.stop()
        self.screen.blit(self.pictures.background, (0, 0))
        self.player.draw_plane()
        self._create_ion()
        self.player.update_ship()
        self._check_player_cation_collide()
        self.score_broad.show_score()
        pygame.display.flip()

    def _create_cation(self):
        _Ba = Ba(self)
        self.cations_in.add(_Ba)

    def _create_anion(self):
        _SO4 = SO4(self)
        self.anions_in.add(_SO4)

    def _create_ion(self):
        now_time = time.time()
        if (now_time - self.start_time) % 5 < 0.01:
            self._create_cation()
        if (now_time - self.start_time) % 5 < 0.01:
            self._create_anion()
        self.cations_in.draw(self.screen)
        self.anions_in.draw(self.screen)
        self.cations_in.update()
        self.anions_in.update()

    def _check_player_cation_collide(self):
        collided_cation = pygame.sprite.spritecollide(self.player, self.cations_in, True)
        if collided_cation:
            bullet = collided_cation[0]
            self.cations_shoot.add(bullet)

    def _store_display(self):
        self.screen.blit(self.pictures.background, (0, 0))
        self.store.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.store.return_rect.collidepoint(mouse_pos):
                    self.title_display, self.store_display = True, False
                    self._title_display()

    def _setting_display(self):
        self.screen.blit(self.pictures.background, (0, 0))
        self.setting.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.setting.return_rect.collidepoint(mouse_pos):
                    self.title_display, self.setting_display = True, False
                    self._title_display()
                if self.setting.vol_plus_image_rect.collidepoint(mouse_pos):
                    self.settings.vol -= 1.0


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ch = CationHazard()
    ch.run_game()
