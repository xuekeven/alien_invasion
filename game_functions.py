import sys
import pygame
import datetime
from bullet import Bullet
from alien import Alien
from time import sleep

#检查鼠标和键盘事件
def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):

    for event in pygame.event.get():   #检测所有的鼠标与键盘事件

        if event.type == pygame.QUIT:   #判断是否点击关闭
            sys.exit()   #退出游戏
        elif event.type == pygame.KEYDOWN:
            check_keydowm_events(event,ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            sound_button = pygame.mixer.Sound(ai_settings.music_button) 
            sound_button.play()
            mouse_x,mouse_y = pygame.mouse.get_pos()   #获取鼠标光标的位置
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

#检查按下键盘事件
def check_keydowm_events(event,ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_b:
        begin_game(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

#检查抬起键盘事件
def check_keyup_events(event,ship):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

#单击开始游戏
def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    button_clicked1 = play_button.rect1.collidepoint(mouse_x,mouse_y)   #测试一个点是否在矩形内
    button_clicked2 = play_button.rect2.collidepoint(mouse_x,mouse_y)

    if button_clicked2:
        sys.exit()

    if button_clicked1 and not stats.game_active:   #防止在游戏进行中点击Play重启游戏
        begin_game(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

#开始游戏
def begin_game(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):

        ai_settings.initialize_dynamic_settings()   #重置游戏设置
        pygame.mouse.set_visible(False)   #隐藏或显示鼠标光标,若为True则鼠标光标将会是可视的
        
        #重置游戏统计信息
        stats.rest_stats()
        stats.game_active = True

        #重置记分牌
        sb.prep_score()
        sb.prep_highest_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings,screen,ship,aliens)
        ship.location_ship()

#发出子弹
def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

#更新子弹
def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    bullets.update()   #更新子弹的位置
    for bullet in bullets.copy():   #创建一个包含与原始Sprites相同的Sprit的新组
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

#计算能放几列外星人
def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    if number_aliens_x >= 10:
        number_aliens_x = 10
    return number_aliens_x

#计算能放几行外星人
def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y/(2 * alien_height))
    if number_rows >= 3:
       number_rows = 3
    return number_rows

#创建一个外星人
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

#创建外星人群
def create_fleet(ai_settings,screen,ship,aliens):
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

#删除发生碰撞的子弹和外星人
def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    '''这将在两组中找到所有精灵之间的碰撞。通过比较每个Sprite的Sprite.rect属性或使用
    碰撞函数（如果它不是None）来确定碰撞。group1中的每个Sprite都被添加到返回字典中。
    每个项的值是group2中相交的Sprite列表。如果dokill参数为True，则将从各自的组中删除碰撞的。'''
    if collisions:
        
        sound_win = pygame.mixer.Sound(ai_settings.music_win) 
        sound_win.play()

        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        record_highest_score(stats,sb)

    if len(aliens) == 0:
        bullets.empty()   #删除所有Sprite
        ai_settings.increase_speed()

        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings,screen,ship,aliens)

#检查外星人是否到达边缘
def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

#外星人下移并改变方向
def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

#响应相撞
def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):

    sound_lose = pygame.mixer.Sound(ai_settings.music_lose) 
    sound_lose.play()

    if stats.ships_left > 0:
        stats.ships_left -= 1

        sb.prep_ships()   #更新飞船

        aliens.empty()   #清空列表
        bullets.empty()

        create_fleet(ai_settings,screen,ship,aliens)   #建立一群新外星人
        ship.location_ship()

        sleep(1)   #暂停
    else:
        record_score(stats,sb)
        stats.game_active = False
        pygame.mouse.set_visible(True)

#检查是否有外星人到底端
def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():   #遍历返回此组包含的所有Sprite的列表
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break

#更新外星人
def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship,aliens):   #如果精灵与组中的任何一个精灵发生碰撞，则返回该组中的一个精灵。 无碰撞时返回None。

        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)

#记录游戏
def record_score(stats,sb):
    if stats.ships_left == 0:
        dt = datetime.datetime.now()
        with open(r'.\record\game_record.txt','a') as files:
            files.write('\n' + str(dt) + '     ' + 'The score :' + str(sb.score))

#读取最高分
def get_highest_score(stats,sb):
    with open(r'.\record\highest_score.txt','r') as file :
        contents = file.readlines()   #方法读取整个文件并且保存在变量中
        stats.highest_score = int(contents[0])

#记录最高分
def record_highest_score(stats,sb):

    if stats.score > stats.highest_score:

        stats.highest_score = stats.score
        sb.prep_highest_score()

        dt = datetime.datetime.now()
        with open(r'.\record\highest_score.txt','w') as files:
            files.write(str(sb.highest_score))
            files.write('\n')
            files.write(str(dt))

#更新屏幕
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):

    get_highest_score(stats,sb)

    screen.fill(ai_settings.bg_color)   #使用纯色填充Surface对象设置屏幕背景色
    for bullet in bullets.sprites():   #返回此组包含的所有Sprite的列表
        bullet.draw_bullut()
    ship.blitme()   #让飞船出现在屏幕，注意飞船必须在背景之后在出现
    aliens.draw(screen)
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()   #将完整显示Surface更新到屏幕（刷新屏幕并擦去旧屏幕，以便更新实时位置）
