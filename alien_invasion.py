import sys   #使用sys模块退出游戏
import pygame   #pygame模块含有开发游戏的功能
from pygame.sprite import Group   #引入编组以便存储和管理子弹

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():

    #初始化游戏并创建屏幕对象
    pygame.init()   #初始化所有导入的pygame模块
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))   
    '''创建名为screen的显示窗口。对象screen是一个Surface。在Pygame中，Surface是屏幕的一部分，用于显示游戏元素。
    在此游戏中，每个元素（如外星人或飞船）都是一个Surface。display.set_mode()返回的Surface表示整个游戏窗口。'''
    pygame.display.set_caption("Alien Invasion")   #设置当前窗口标题

    #播放音乐
    pygame.mixer.music.load(ai_settings.music_bgm) 
    pygame.mixer.music.play(9999)

    #创建开始按钮
    play_button = Button(ai_settings,screen,'''开始游戏''','结束游戏')

    #创建存储游戏统计信息
    stats = GameStats(ai_settings)

    #创建记分牌
    sb = Scoreboard(ai_settings,screen,stats)

    #创建一艘飞船、一个用于存储子弹的编组、一个外星人编组
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #开始游戏主循环
    while True:

        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
            
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()