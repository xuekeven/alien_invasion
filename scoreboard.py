import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():

    def __init__(self,ai_settings,screen,stats):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.bgb_color = (255,250,205)
        self.text_color1 = (0,205,205)
        self.text_color2 = (180,238,180)
        self.font1 = pygame.font.SysFont('方正粗黑宋简体',20)
        self.font2 = pygame.font.SysFont('方正粗黑宋简体',20)

        '''从系统字体库中加载并返回一个新的字体对象。该字体将会匹配 bold（加粗）和 italic（斜体）参数的要求。
        若找不到合适的系统字体，该函数将会回退并加载默认pygame字体。尝试搜索name参数可以是一个用逗号隔开的列表。'''

        self.background_board()
        self.prep_score()   #得分图像
        self.prep_highest_score()   #最高分图像
        self.prep_level()   #等级图像
        self.prep_ships()

    #下层背景板
    def background_board(self):

        self.bgb_rect = (0,0,self.ai_settings.screen_width,60)

    #得分
    def prep_score(self):

        self.score = int(round(self.stats.score,-1))   #将stats.score的值变最近的10的整数倍并存储结果
        self.score_str = "{:,}".format(self.score)   #字符串格式设置指令，将数值转换为字符串时并在中插入逗号

        self.score_image = self.font1.render('当前得分：' + self.score_str,True,self.text_color1)
        '''创建一个新的Surface对象并在其上渲染指定文本。Pygame没有提供直接的方式在一个现有Surface对象上绘制文本，
        取而代之的方法是使用Font.render()函数创建一个渲染了文本的图像（Surface对象），然后将此图像绘至目标Surface上。'''

        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.centerx = self.screen_rect.centerx - 100   #右边缘与屏幕右边缘相距20像素
        self.score_image_rect.top = 20   #上边缘与屏幕上边缘也相距20像素

    #等级
    def prep_level(self):

        self.level_image = self.font1.render('当前等级：' + str(self.stats.level),True,self.text_color1,self.bgb_color)

        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.centerx = self.screen_rect.centerx + 100
        self.level_image_rect.top = self.score_image_rect.top

    #最高分
    def prep_highest_score(self):

        self.highest_score = int(round(self.stats.highest_score,-1))
        self.highest_score_str = "{:,}".format(self.highest_score)

        self.highest_score_image = self.font2.render('历史最高分：' + self.highest_score_str,True,self.text_color2,self.bgb_color)

        self.highest_score_image_rect = self.highest_score_image.get_rect()
        self.highest_score_image_rect.right = self.screen_rect.right - 20
        self.highest_score_image_rect.top = self.score_image_rect.top

    #飞船
    def prep_ships(self):

        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    #显示分数
    def show_score(self):
        
        self.screen.fill(self.bgb_color,self.bgb_rect)
        self.screen.blit(self.score_image,self.score_image_rect)   #将一个图像（Surface对象）绘制到screen的Surface对象上
        self.screen.blit(self.highest_score_image,self.highest_score_image_rect)
        self.screen.blit(self.level_image,self.level_image_rect)
        self.ships.draw(self.screen)
    

#self.image12 = pygame.image.load('D:/Learn/Python/Improve/pygame/alien_invasioni/mages/asd.gif')   #从文件源中加载图像，Pygame将确定图像类型并创建其为新Surface对象
#self.rect12 = self.image12.get_rect()   
#self.rect12.x = 0
#self.rect12.y = 5

#self.screen.blit(self.image12,self.rect12)
