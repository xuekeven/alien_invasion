import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    #初始化飞船设置
    def __init__(self,ai_settings,screen):

        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load(self.ai_settings.ship_file)   #从文件源中加载图像，Pygame将确定图像类型并创建其为新Surface对象
        self.rect = self.image.get_rect()   
        self.screen_rect = self.screen.get_rect()
        '''获取Surface对象的属性Rect对象，Rect是pygame用来储存矩形坐标的对象。返回一个Rect对象表示该Surface对象的矩形区域。
        该矩形对象的Rect总是以 (0, 0) 为起点，width 和 height 为图像的尺寸。'''
        
        #设置飞船的位置
        self.rect.centerx = self.screen_rect.centerx   #飞船的横坐标为中心，与屏幕的中心相同
        self.rect.bottom = self.screen_rect.bottom  #飞船的纵坐标为底部，与屏幕的底部相同
        '''Pygame使用Rect对象来存储和操作矩形区域。可以从left，top，width和height值的组合创建Rect对象。
        也可以从已经是Rect对象或具有名为“rect”的属性的python对象创建Rect对象。Rect对象有几个虚拟属性，可用于移动和对齐Rect。
        如x,y,top, left, bottom, right,topleft, bottomleft, topright, bottomright,midtop, midleft, midbottom, midright,
        center, centerx, centery,size, width, height,w,等。'''

        #飞船的属性中存储小数值
        self.center = float(self.rect.centerx)
        self.bottoma = float(self.rect.bottom)

        #设置飞船的移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    #根据移动标志调整飞船位置
    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.bottoma -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottoma += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center   #根据self.center更新rect对象
        self.rect.bottom = self.bottoma
    
    #将飞船移至屏幕中央
    def location_ship(self):

        self.center = self.screen_rect.centerx
        self.bottoma = self.screen_rect.bottom

    #传递飞船信息
    def blitme(self):

        self.screen.blit(self.image,self.rect)   #将一个图像（Surface 对象）绘制到另一个图像上方（将飞船图片和飞船坐标传入，以在屏幕上显示）