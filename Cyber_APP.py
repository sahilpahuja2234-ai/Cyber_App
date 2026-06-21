import pygame as pg
from sys import exit
from menu import main_menu
from Score import SCORE
from level_1 import LevelOne
from Level_2 import LevelTwo
from Transition import CyberTransition

pg.init()
screen = pg.display.set_mode((1280, 720))
pg.display.set_caption('CyberApp')
clock = pg.time.Clock()

# ── State ─────────────────────────────────────────────────────────────────────
game_active   = False     # False = show menu
current_level = None      # 'level1' | 'level2'
level         = None
s             = SCORE()

# ── Menu ──────────────────────────────────────────────────────────────────────
main_menu_font   = pg.font.Font('Font/Main_menu_font/Rajdhani-Bold.ttf', 50)
start_box, exit_box = None, None
border_anim_pos  = 0

start_pressed_time = 0
exit_pressed_time  = 0
PRESS_DURATION     = 150

start_clicked = False
exit_clicked  = False

# ── Transition ────────────────────────────────────────────────────────────────
transition = CyberTransition(
    "Graphic/Level_1_graphics/cyber_app_transition.png",
    fps=60
)
transitioning = False
pending_level = None      # which level to load at the halfway point

def begin_transition(next_level: str):
    """Start the wipe animation; next_level is loaded at the midpoint."""
    global transitioning, pending_level
    transitioning = True
    pending_level = next_level
    transition.reset()

# ── Main loop ─────────────────────────────────────────────────────────────────
game_is_on = True

while game_is_on:
    border_anim_pos += 6

    # ── Events ────────────────────────────────────────────────────────────
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        # Block game input while transitioning
        if game_active and not transitioning and level:
            level.handle_event(event)

        if event.type == pg.MOUSEBUTTONDOWN:
            if start_box and start_box.collidepoint(event.pos):
                start_pressed_time = pg.time.get_ticks()
                start_clicked = True
            if exit_box and exit_box.collidepoint(event.pos):
                exit_pressed_time = pg.time.get_ticks()
                exit_clicked = True

    # ── Delayed start/exit ────────────────────────────────────────────────
    if start_clicked and pg.time.get_ticks() - start_pressed_time > PRESS_DURATION:
        begin_transition('level1')
        start_clicked = False
        start_box = exit_box = None

    if exit_clicked and pg.time.get_ticks() - exit_pressed_time > PRESS_DURATION:
        pg.quit()
        exit()

    # ── Level-complete → advance ──────────────────────────────────────────
    if game_active and level and not transitioning:
        if current_level == 'level1' and level.level_complete and level.feedback_timer == 0:
            begin_transition('level2')
        # Level 2 end: go back to menu (or add Level 3 here later)
        elif current_level == 'level2' and level.level_complete and level.feedback_timer == 0:
            s.save()
            game_active   = False
            current_level = None
            level         = None

    # ── Draw ──────────────────────────────────────────────────────────────
    if transitioning:
        # Draw background layer first
        if game_active and level:
            level.update()
            level.draw(screen)
        else:
            s.save()
            start_box, exit_box = main_menu(
                screen, main_menu_font, border_anim_pos,
                start_pressed_time, exit_pressed_time, PRESS_DURATION
            )

        transition.update()
        transition.draw(screen)

        # Midpoint — swap in the new level
        if transition.frame_index == transition.FRAME_COUNT // 2 and pending_level:
            if pending_level == 'level1':
                level         = LevelOne(s)
                current_level = 'level1'
                game_active   = True
            elif pending_level == 'level2':
                level         = LevelTwo(s)
                current_level = 'level2'
            pending_level = None

        if transition.done:
            transitioning = False

    elif game_active and level:
        level.update()
        level.draw(screen)

    else:
        s.save()
        start_box, exit_box = main_menu(
            screen, main_menu_font, border_anim_pos,
            start_pressed_time, exit_pressed_time, PRESS_DURATION
        )

    pg.display.update()
    clock.tick(60)