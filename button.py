import pygame.font

class Button():

    def __init__(self,ai_settings,screen,msg1,msg2):

        #定义一些将要用到的变量
        self.screen = screen
        self.screen_rect = screen.get_rect()   #后面结果以screen为参考，也可以不引入来设置
        '''获取Surface对象的矩形区域。返回一个Rect对象表示该Surface对象的矩形区域。矩形对象（Rect）总以
        (0, 0) 为起点，width和height为图像尺寸。可以给该函数传递关键字参数，返回的结果将受参数的影响。'''
        self.width , self.height = 150,50
        self.button_color = (0,255,0)
        self.text_color = (255,0,0)
        self.font = pygame.font.SysFont('方正舒体',30)
        '''从系统字体库中加载并返回一个新的字体对象。该字体将会匹配 bold（加粗）和 italic（斜体）参数的要求。
        若找不到合适的系统字体，该函数将会回退并加载默认pygame字体。尝试搜索name参数可以是一个用逗号隔开的列表。'''

        self.rect1 = pygame.Rect(0,0,self.width,self.height)   #用来储存矩形的坐标和大小
        self.rect1.centerx = self.screen_rect.centerx - 120   #重新设置x坐标（原来为0）
        self.rect1.centery = self.screen_rect.centery   #重新设置y坐标（原来为0）

        self.rect2 = pygame.Rect(0,0,self.width,self.height)
        self.rect2.centerx = self.screen_rect.centerx + 120
        self.rect2.centery = self.screen_rect.centery

        self.prep_msg1(msg1)
        self.prep_msg2(msg2)
                                         
    def prep_msg1(self,msg1):
        
        self.msg1_image = self.font.render(msg1,True,self.text_color,self.button_color)
        '''创建一个新的Surface对象并在其上渲染指定文本。Pygame没有提供直接的方式在一个现有Surface对象上绘制文本，
        取而代之的方法是使用Font.render()函数创建一个渲染了文本的图像（Surface对象），然后将此图像绘至目标Surface上。'''
        
        self.msg1_image_rect = self.msg1_image.get_rect()
        self.msg1_image_rect.centerx = self.rect1.centerx
        self.msg1_image_rect.centery = self.rect1.centery

    def prep_msg2(self,msg2):

        self.msg2_image = self.font.render(msg2,True,self.text_color,self.button_color)
        
        self.msg2_image_rect = self.msg2_image.get_rect()
        self.msg2_image_rect.centerx = self.rect2.centerx
        self.msg2_image_rect.centery = self.rect2.centery

    def draw_button(self):

        self.screen.fill(self.button_color,self.rect1)   #使用纯色填充screen的Surface对象，第二个参数限制填充的矩形范围
        self.screen.fill(self.button_color,self.rect2)

        self.screen.blit(self.msg1_image,self.msg1_image_rect)   #将一个图像（Surface对象）绘制到screen的Surface对象上
        self.screen.blit(self.msg2_image,self.msg2_image_rect) 
