import pygame as pg
from sys import exit
from menu import main_menu
from Score import SCORE
from level_1 import LevelOne
from Transition import CyberTransition

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

# ── Transition setup ──────────────────────────────────────────────────────────
transition = CyberTransition("Graphic/cyber_app_transition.png", fps=60)
transitioning = False  # True while the animation is playing
# ─────────────────────────────────────────────────────────────────────────────

while game_is_on:
    border_anim_pos += 6

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_is_on = False
            pg.quit()
            exit()

        # Block game input while transitioning
        if game_active and not transitioning:
            level.handle_event(event)

        if event.type == pg.MOUSEBUTTONDOWN:
            if start_box and start_box.collidepoint(event.pos):
                start_pressed_time = pg.time.get_ticks()
                start_clicked = True

            if exit_box and exit_box.collidepoint(event.pos):
                exit_pressed_time = pg.time.get_ticks()
                exit_clicked = True

    # Handle delayed start → kick off transition instead of jumping straight in
    if start_clicked:
        if pg.time.get_ticks() - start_pressed_time > PRESS_DURATION:
            transitioning = True
            transition.reset()
            start_clicked = False
            start_box, exit_box = None, None

    # Handle delayed exit
    if exit_clicked:
        if pg.time.get_ticks() - exit_pressed_time > PRESS_DURATION:
            pg.quit()
            exit()

    # ── Draw ─────────────────────────────────────────────────────────────────
    if transitioning:
        # Draw whatever is underneath first (menu or game), then overlay
        if game_active:
            level.update()
            level.draw(screen)
        else:
            s.save()
            start_box, exit_box = main_menu(screen, main_menu_font, border_anim_pos,start_pressed_time, exit_pressed_time, PRESS_DURATION)

        transition.update()
        transition.draw(screen)  # draws on top of everything

        # Halfway through → load the level so it's ready when transition ends
        if transition.frame_index == transition.FRAME_COUNT // 2 and not game_active:
            game_active = True
            level = LevelOne(s)

        # Transition finished
        if transition.done:
            transitioning = False

    elif game_active:
        level.update()
        level.draw(screen)

    else:
        s.save()
        start_box, exit_box = main_menu(screen, main_menu_font, border_anim_pos,start_pressed_time, exit_pressed_time, PRESS_DURATION)

    pg.display.update()
    clock.tick(60)