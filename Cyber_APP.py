import pygame as pg
from sys import exit
from menu import main_menu
from Score import SCORE
from level_1 import LevelOne
pg.init()
screen = pg.display.set_mode((1280, 720))
pg.display.set_caption('CYber App')
clock = pg.time.Clock()

game_is_on = True
game_active = False

# Load font once
main_menu_font = pg.font.Font('Font/Main_menu_font/Rajdhani-Bold.ttf', 50)

# Initialize boxes
start_box, exit_box = None, None

# Press timing system
start_pressed_time = 0
exit_pressed_time = 0
PRESS_DURATION = 150  # milliseconds

# Click states
start_clicked = False
exit_clicked = False

border_anim_pos = 0
level = None
s = SCORE()
while game_is_on:
    border_anim_pos += 6  # speed
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_is_on = False
            pg.quit()
            exit()
        # If the game is running, route all events directly to the level
        if game_active:
            level.handle_event(event)
        #Click handling
        if event.type == pg.MOUSEBUTTONDOWN:
            if start_box and start_box.collidepoint(event.pos):
                start_pressed_time = pg.time.get_ticks()
                start_clicked = True

            if exit_box and exit_box.collidepoint(event.pos):
                exit_pressed_time = pg.time.get_ticks()
                exit_clicked = True

    # Handle delayed start
    if start_clicked:
        if pg.time.get_ticks() - start_pressed_time > PRESS_DURATION:
            game_active = True
            level = LevelOne(s)
            start_clicked = False
            start_box,exit_box = None,None

    # Handle delayed exit
    if exit_clicked:
        if pg.time.get_ticks() - exit_pressed_time > PRESS_DURATION:
            pg.quit()
            exit()

    # Draw
    if game_active:

        level.update()# Game screen
        level.draw(screen)
    else:
        s.save()
        start_box, exit_box = main_menu(screen,main_menu_font,border_anim_pos,start_pressed_time,exit_pressed_time,PRESS_DURATION)

    pg.display.update()
    clock.tick(60) #Max Fps