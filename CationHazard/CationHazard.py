"""

"""

import pygame
import sys
import time
from random import randint

from pictures import Pictures
from music import Musics
from player import Plane
from settings import Settings
from saving import Saving

from titles import Texts
from titles import Buttons
from store import Store
from setting import Setting
from bullet import Ba as Ba_bullet

from scoreboard import Scoreboard
from experience import Experience

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
        self.screen_size = self.screen.get_rect()

        # 创建设置、图片实例
        self.setting = Setting(self)
        self.musics = Musics()

        # 创建文字实例
        self.texts = Texts(self)
        self.buttons = Buttons(self)
        self.store = Store(self)
        self.score_broad = Scoreboard(self)
        self.experience = Experience(self)

        # 创建飞船实例
        self.player = Plane(self)

        self.saving = Saving()

        self.title_display = True
        self.play_game = False
        self.store_display = False
        self.setting_display = False

        self.play_title_music = True
        self.play_music_play = True

        self.cations = pygame.sprite.Group()
        self.anions = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        # 绘制屏幕并显示
        self.screen.blit(self.pictures.background, (0, 0))
        pygame.display.flip()

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
                self.check_mouse_button_down_events(mouse_pos)

    def keydown_events(self, event):
        """响应键盘按下事件"""
        if event.key == pygame.K_q:
            sys.exit()

        # 游戏运行时检测
        if self.play_game:
            if event.type == pygame.KEYDOWN:
                # 用前后左右或wasd控制人物移动
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.player.moving_left = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.moving_right = True
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.player.moving_up = True
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.player.moving_down = True
                # 子弹充足时按下空格发射子弹
                if self.settings.bullet_num > 0 and event.key == pygame.K_SPACE:
                    bullet = Ba_bullet(self, self.player.rect)
                    self.bullets.add(bullet)
                    self.settings.bullet_num -= 1
                # 按下e时回到主界面
                if event.key == pygame.K_e:
                    self._game_over()

    def keyup_events(self, event):
        """键盘抬起时，人物停止移动"""
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

        if self.title_display:
            if play_clicked:
                self.title_display, self.play_game = False, True
            elif setting_clicked:
                self.title_display, self.setting_display = False, True
            elif store_clicked:
                self.title_display, self.store_display = False, True
            elif exit_clicked:
                sys.exit()

        if self.store_display:
            if self.store.return_rect.collidepoint(mouse_pos):
                self.title_display, self.store_display = True, False
                self._title_display()
            if self.store.bullet_up_rect.collidepoint(mouse_pos):
                self.settings.bullet_level += 1
                self.settings.bullet_num += 1
                self.saving.bullet_level_input(self.settings.bullet_level)
            if self.store.blood_up_rect.collidepoint(mouse_pos):
                self.settings.blood_level += 1
                self.settings.blood = 100 + self.settings.blood_level

        if self.setting_display:
            if self.setting.return_rect.collidepoint(mouse_pos):
                self.title_display, self.setting_display = True, False
                self._title_display()
            if self.setting.vol_plus_image_rect.collidepoint(mouse_pos):
                self.settings.vol -= 1.0

    def _title_display(self):
        self.screen.blit(self.pictures.background, (0, 0))
        if self.play_title_music:
            # self.musics.play_title_music()
            self.play_title_music = False
        self.texts.draw_title()
        self.buttons.button()
        pygame.display.flip()

    def _play_game(self):
        """游戏主进程"""

        # 只播放一次音乐
        if self.play_music_play:
            # self.musics.play_play_music()
            self.play_music_play = False

        # 绘制背景、玩家，并开始创建阴阳离子
        self.screen.blit(self.pictures.background, (0, 0))
        self.player.draw_plane()
        self._create_ion()
        self.player.update_ship()

        # 检测玩家和阳离子碰撞，碰撞后增加子弹数
        collided_player_cations = pygame.sprite.spritecollide(self.player, self.cations, True)
        if collided_player_cations:
            self.settings.bullet_num += randint(2, 4)
            self.score_broad.bullet_num = self.settings.bullet_num

        # 绘制发射的子弹
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.bullets.update()
        # 显示得分和等级
        self.score_broad.show_score()
        self.score_broad.draw_bullet_num(self.settings.bullet_num)
        self.experience.show_level_exp()

        # 删除生成时就在一起的离子
        pygame.sprite.groupcollide(self.anions, self.cations, False, True)

        # 检测子弹和阴离子的碰撞，碰撞后得分并增加经验
        collided_bullets_anions = pygame.sprite.groupcollide(self.bullets, self.anions, True, True)
        if collided_bullets_anions:
            self.score_broad.score_up()
            self.experience.now_exp += 1
            self.saving.exp_input(self.experience.now_exp)

        collided_player_anions = pygame.sprite.spritecollide(self.player, self.anions, True)
        if collided_player_anions:
            self.settings.blood -= 20
            if self.settings.blood <= 0:
                self._game_over()

        # 升级
        self.experience.level_up()

        # 删除屏幕外的子弹
        self._delete_ions()

        # 更新画面
        pygame.display.flip()

    def _create_ion(self):
        """创建阴阳离子"""
        now_time = time.time()
        if (now_time - self.start_time) % 5 < 0.01:
            _Ba = Ba(self)
            self.cations.add(_Ba)
        if (now_time - self.start_time) % 2 < 0.01:
            _SO4 = SO4(self)
            self.anions.add(_SO4)
        self.cations.draw(self.screen)
        self.anions.draw(self.screen)
        self.cations.update()
        self.anions.update()

    def _game_over(self):
        self.anions.empty()
        self.cations.empty()
        self.bullets.empty()
        coin = self.saving.golden_coin_output()
        coin += self.score_broad.score // 100
        self.saving.golden_coin_input(coin)
        self.score_broad.score = 0
        self.settings.bullet_num = self.settings.bullet_level
        self.player.rect.midbottom = self.screen.get_rect().midbottom
        self.play_game, self.title_display = False, True
        self.play_title_music, self.play_music_play = True, True

    def _store_display(self):
        self.screen.blit(self.pictures.background, (0, 0))
        self.store.draw()
        self.store.draw_bullet_level(self.settings.bullet_level)
        self.store.draw_blood_level(self.settings.blood_level)

        pygame.display.flip()

    def _setting_display(self):
        self.screen.blit(self.pictures.background, (0, 0))
        self.setting.draw()
        pygame.display.flip()

    def _delete_ions(self):
        for cation in self.cations:
            if cation.rect.top > self.screen_size.bottom:
                self.cations.remove(cation)
        for anion in self.anions:
            if anion.rect.top > self.screen_size.bottom:
                self.cations.remove(anion)
        for bullet in self.bullets:
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ch = CationHazard()
    ch.run_game()
