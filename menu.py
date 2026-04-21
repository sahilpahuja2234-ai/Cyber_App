import pygame as pg

# Color Constants
NEON_CYAN = (0, 238, 255)
DEEP_BLUE = (8, 32, 50)
# MUTED_TEAL = (20, 80, 100)
Charged_Teal =(20, 90, 110)
DARK_VOID = (5, 10, 15)
PURE_WHITE = (255, 255, 255) # Good for highlight text
GREEN = (0, 200, 120)
RED = (220, 50, 50)
MUTED_TEAL = (15, 50, 65)
GLOW_COLOR = (0, 255, 180)       # neon cyan
ALT_GLOW = (180, 0, 255)         # neon purple (optional second pulse)


# Example usage:
# screen.fill(DARK_VOID)
# pygame.draw.rect(screen, MUTED_TEAL, rect_object, width=2)


def draw_multi_animated_border(screen, x, y, w, h, color, glow_color, thickness, anim_pos):
    # Base border
    pg.draw.rect(screen, color, (x, y, w, h), thickness)

    perimeter = 2 * (w + h)

    segment_length = 80
    num_segments = 17        # number of rectangles
    spacing = 240          # distance between them

    for i in range(num_segments):
        pos = (anim_pos - i * spacing) % perimeter

        # TOP
        if pos < w:
            end = min(w, pos + segment_length)
            pg.draw.line(screen, glow_color,
                         (x + pos, y),
                         (x + end, y), thickness)

        # RIGHT
        elif pos < w + h:
            pos -= w
            end = min(h, pos + segment_length)
            pg.draw.line(screen, glow_color,
                         (x + w, y + pos),
                         (x + w, y + end), thickness)

        # BOTTOM
        elif pos < 2*w + h:
            pos -= (w + h)
            end = min(w, pos + segment_length)
            pg.draw.line(screen, glow_color,
                         (x + w - pos, y + h),
                         (x + w - end, y + h), thickness)

        # LEFT
        else:
            pos -= (2*w + h)
            end = min(h, pos + segment_length)
            pg.draw.line(screen, glow_color,
                         (x, y + h - pos),
                         (x, y + h - end), thickness)


def draw_box(screens, color ,rect, text, text_color, font):
     box = pg.draw.rect(screens, color, rect=rect, border_radius=10)
     # box highlights
     pg.draw.rect(screens, GLOW_COLOR, rect=rect, width=10, border_radius=12)

     self_font = font.render(text, False, text_color)
     text_rect = self_font.get_rect(center=box.center)
     screens.blit(self_font, text_rect)
     return box


def main_menu(screen, font, border_anim_pos, start_pressed_time, exit_pressed_time, PRESS_DURATION):
    screen.fill(DARK_VOID)
    text_color = NEON_CYAN

    main_menu_font_local = pg.font.Font('Font/Main_menu_font/Rajdhani-Bold.ttf', 70)
    main_menu_tittle = main_menu_font_local.render('Main Menu', False, text_color)

    screen.blit(main_menu_tittle, (487.5, 10))

    #border
    draw_multi_animated_border(screen,10, 10, 1260, 700,DARK_VOID,NEON_CYAN,10,border_anim_pos)

    #  mouse position
    mouse_pos = pg.mouse.get_pos()

    # Base rects (so we can reuse them)
    start_rect = pg.Rect(500, 300, 300, 100)
    exit_rect = pg.Rect(500, 420, 300, 100)

    # current time (for press effect)
    current_time = pg.time.get_ticks()

    # START BUTTON
    if start_rect.collidepoint(mouse_pos):
        text_color_start = PURE_WHITE

        if current_time - start_pressed_time < PRESS_DURATION:
            start_color = GREEN
        else:
            start_color = Charged_Teal

    else:
        start_color = DEEP_BLUE
        text_color_start = NEON_CYAN

    # EXIT BUTTON
    if exit_rect.collidepoint(mouse_pos):
        text_color_exit = PURE_WHITE

        if current_time - exit_pressed_time < PRESS_DURATION:
            exit_color = RED   # RED when pressed
        else:
            exit_color = Charged_Teal
    else:
        exit_color = DEEP_BLUE
        text_color_exit = NEON_CYAN

    start_box = draw_box(screen, start_color, start_rect, "Start",  text_color_start, font)
    exit_box = draw_box(screen, exit_color, exit_rect, "EXIT", text_color_exit, font)

    return start_box, exit_box   # IMPORTANT