import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_settings,screen,ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.ship_speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -=self.ship_speed_factor   #更新表示子弹位置的小数值
        self.rect.y = self.y   #更新表示子弹位置的rect位置

    def draw_bullut(self):
        pygame.draw.rect(self.screen,self.color,self.rect)   #在Surface对象上绘制一个矩形
