
class Settings():

    #存储游戏的所有设置
    def __init__(self):

        #屏幕设置
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (230,230,230)   #用RGB设置背景颜色

        #音乐设置
        self.music_bgm = ('./music/bgm.mp3')
        self.music_button = ('./music/button.mp3')
        self.music_win = ('./music/win.mp3')
        self.music_lose = ('./music/lose.mp3')

        #飞船设置
        self.ship_file = ('./images/ship.bmp')   #飞船图片位置
        self.ship_file2 = ('./images/ship2.bmp')
        self.ship_limit = 3   #飞船数量

        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3   #子弹数量

        #外星人设置
        self.alien_file = ('./images/alien.bmp')   #外星人图片位置
        self.fleet_drop_speed = 20   #外星人上下移速

        #升级设置
        self.speedup_scale = 1.1   #加快游戏速度
        self.score_scale = 1.5   #外星人点数提高速度

        self.initialize_dynamic_settings()
    
    #初始化游戏
    def initialize_dynamic_settings(self):

        self.ship_speed_factor = 1.5   #飞船速度
        self.bullet_speed_factor = 2   #子弹速度
        self.alien_speed_factor = 2   #外星人左右移速
        self.fleet_direction = 1   #1表示左移，-1表示右移
        self.alien_points = 50   #外星人点数

    #游戏升级
    def increase_speed(self):

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)        