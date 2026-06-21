import pygame as pg
from menu import PURE_WHITE, draw_box


class BaseLevel:
    """
    Shared infrastructure inherited by every level.
    Provides: fonts, score ref, feedback overlay, scrollable instruction screen.
    """

    def __init__(self, score):
        self.score          = score
        self.Instruction_read = False
        self.instructions   = []          # filled by each subclass
        self.feedback_timer = 0
        self.feedback_text  = ""
        self.feedback_color = (0, 0, 0)
        self.level_complete = False

        # ── Scroll state ──────────────────────────────────────────────────
        self.scroll_offset   = 0
        self._content_height = 0          # measured each draw; used for clamping

        # ── Fonts (loaded once, shared by all levels) ─────────────────────
        BOLD  = 'Font/Level_1_font/OpenSans-Bold.ttf'
        COND  = 'Font/Level_1_font/OpenSans_Condensed-Regular.ttf'

        self.level_font        = pg.font.Font(BOLD, 15)
        self.uploader_font     = pg.font.Font(BOLD, 13)

        self.instruction_font  = pg.font.Font(COND, 70)   # kept for any caller
        self.title_font        = pg.font.Font(COND, 34)   # instruction screen title
        self.header_font       = pg.font.Font(COND, 20)   # section headers (──)

        self.open_sender_font  = pg.font.Font(COND, 20)
        self.open_subject_font = pg.font.Font(COND, 28)
        self.open_meta_font    = pg.font.Font(COND, 16)
        self.open_body_font    = pg.font.Font(COND, 17)
        self.open_attach_font  = pg.font.Font(COND, 15)

    # ── Scrollable instruction screen ──────────────────────────────────────
    def draw_instructions(self, surface):
        """
        Renders self.instructions onto surface with correct per-line sizing.
        Supports mouse-wheel + arrow-key scrolling when content > 720px.
        Call this from draw() while not self.Instruction_read.
        """
        surface.fill((10, 10, 20))

        y       = 20 - self.scroll_offset
        total_h = 0

        for idx, line in enumerate(self.instructions):
            # ── Title (first line) ──────────────────────────────────────
            if idx == 0:
                surf = self.title_font.render(line, True, (0, 255, 180))
                h    = 44
            # ── Blank spacer ────────────────────────────────────────────
            elif line == "":
                y       += 10
                total_h += 10
                continue
            # ── Section header  ─────────────────────────────────────────
            elif line.startswith("──"):
                surf = self.header_font.render(line, True, (0, 200, 255))
                h    = 26
            # ── Indented example ────────────────────────────────────────
            elif line.startswith("  "):
                surf = self.level_font.render(line, True, (180, 180, 100))
                h    = 20
            # ── Normal body text ────────────────────────────────────────
            else:
                surf = self.level_font.render(line, True, (200, 200, 200))
                h    = 20

            # Only blit lines that are on screen
            if y + h > 0 and y < 720:
                surface.blit(surf, (200, y))

            y       += h
            total_h += h

        self._content_height = total_h
        max_scroll = max(0, total_h - 680)

        # Scroll indicators
        if max_scroll > 0:
            if self.scroll_offset < max_scroll:
                hint = self.level_font.render("scroll for more  v", True, (70, 70, 70))
                surface.blit(hint, (557, 700))
            if self.scroll_offset > 0:
                up = self.level_font.render("^ scroll up", True, (70, 70, 70))
                surface.blit(up, (579, 4))

    def handle_instruction_event(self, event):
        """
        Routes scroll-wheel / arrow-key events while instructions are showing.
        Returns True if the event was consumed by scrolling (caller must not
        treat it as a 'dismiss' click).
        """
        max_scroll = max(0, self._content_height - 680)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 4:          # wheel up
                self.scroll_offset = max(0, self.scroll_offset - 40)
                return True
            if event.button == 5:          # wheel down
                self.scroll_offset = min(max_scroll, self.scroll_offset + 40)
                return True

        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_UP, pg.K_PAGEUP):
                self.scroll_offset = max(0, self.scroll_offset - 60)
                return True
            if event.key in (pg.K_DOWN, pg.K_PAGEDOWN):
                self.scroll_offset = min(max_scroll, self.scroll_offset + 60)
                return True

        return False