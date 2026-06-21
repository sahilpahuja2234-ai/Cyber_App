"""
Level 1 — Torrent Inspection
Player identifies the one safe torrent among 11 fakes on a mock 1337Y page.
"""
import pygame as pg

from base_level import BaseLevel
from menu import PURE_WHITE, GREEN, RED, draw_box


class LevelOne(BaseLevel):

    def __init__(self, score):
        super().__init__(score)

        # ── Background art (1337Y listing page, 1280×720) ────────────────
        self.bg = pg.image.load(
            'Graphic/level_1_graphics/level_1_closed_view.png'
        ).convert_alpha()

        # ── Row hit-boxes (pixel-measured from the background art) ────────
        row_tops    = [311, 346, 380, 414, 448, 484, 519, 556, 594, 634, 669]
        row_heights = [ 35,  34,  34,  34,  36,  35,  37,  38,  40,  35,  37]
        TABLE_X, TABLE_W = 54, 1199 - 54
        self.rows_rect = [
            pg.Rect(TABLE_X, top, TABLE_W, h)
            for top, h in zip(row_tops, row_heights)
        ]

        # Column x-centres (aligned to header art)
        self.col_name_x      =   64
        self.col_se_cx       =  750
        self.col_le_cx       =  830
        self.col_time_cx     =  925
        self.col_size_cx     = 1031
        self.col_uploader_cx = 1141

        # (name, seeders, leechers, time, size, uploader, is_malicious)
        self.torrents = [
            ("Batman.2022.HDCAM.x264-FAKE.exe",                    "3",    "512", "4 hours ago",   "1.4 GB",  "newuser88234",      True),
            ("FREE BATMAN 2022 FULL MOVIE HD!!! NO VIRUS!!!",      "145",  "12",  "1 day ago",     "2.1 GB",  "MovieKing_2026",    True),
            ("Batman.2022.1080p.BluRay.x264-GROUP",                "2453", "187", "3 months ago",  "11.2 GB", "YTS.MX ", False),
            ("Batman.2022.1080p.BluRay.x264-GR0UP",                "89",   "94",  "2 months ago",  "10.8 GB", "YT5.MX",            True),
            ("Batman.2022.2160p.REMUX-FREE",                       "612",  "4",   "2 minutes ago", "980 MB",  "xXx_d4rkn3t_xXx",  True),
            ("Batman.2022.1080p.mkv.exe",                          "44",   "201", "6 hours ago",   "9.6 GB",  "Anonymous",         True),
            ("WORKING 100% Batman 2022 BluRay [PASSWORD INSIDE]",  "22",   "340", "5 hours ago",   "3.2 GB",  "seed3r_x99",        True),
            ("Batman.2022.1080p.WEB-DL.x264-GROUP",               "1850", "1620","3 weeks ago",   "780 MB",  "GROUP_Official",    True),
            ("Batman.2022.1080p.BluRay.x265-GROUP.zip",            "5",    "290", "1 month ago",   "14.9 GB", "user_38291",        True),
            ("[CLICK HERE] Batman 2022 Full Movie + Bonus Codec Pack","67", "410", "8 hours ago",  "650 MB",  "codec_helper_01",   True),
            ("Batman.2022.1080p.BluRay.DDP5.1.Atmos-GROUP",       "3120", "8",   "14 hours ago",  "11.0 GB", "GROUP",             True),
        ]

        self.locked = False

        # ── Instructions (scrollable) ──────────────────────────────────────
        self.instructions = [
            "LEVEL 1: TORRENT INSPECTION",
            "",
            "You are attempting to download Batman (2022)",
            "from 1337Y. Analyse each listing carefully.",
            "One torrent is safe. The rest are traps.",
            "",
            "── SEEDER / LEECHER RATIO ──",
            "A healthy torrent has significantly more",
            "seeders than leechers.",
            "  2000 SE / 150 LE  =  Trustworthy",
            "  2 SE   / 500 LE   =  Dead or malicious",
            "",
            "── UPLOADER REPUTATION ──",
            "Verified uploaders carry badges and have",
            "a consistent upload history.",
            "Threat actors use disposable accounts,",
            "random usernames, or impersonate trusted",
            "uploaders with subtle name alterations.",
            "",
            "── TITLE FORMATTING ──",
            "Legitimate releases follow a standard:",
            "  Batman.2022.1080p.BluRay.x264-GROUP",
            "Malicious uploads often use urgency",
            "or reassurance in the title itself:",
            "  FREE BATMAN HD FULL NO PASSWORD.exe",
            "",
            "── FILE SIZE ──",
            "A 1080p film is typically 8 - 15 GB.",
            "Anything significantly smaller is",
            "compressed, fake, or weaponised.",
            "",
            "── FILE LIST ──",
            "A legitimate release contains:",
            "  .mkv / .mp4  and subtitle files",
            "Abort if you find:",
            "  .exe  .scr  .bat  .cmd  setup files",
            "  password notes  or browser extensions",
            "",
            "Correct download  =  +30 Points",
            "Wrong download    =  -15 Points  (retry)",
            "",
            "Scroll to read all, then click or press SPACE.",
        ]

    # ── Game logic ─────────────────────────────────────────────────────────
    def validate_choice(self, i):
        *_, is_malicious = self.torrents[i]
        if is_malicious:
            self.score.deduct(15)
            self.feedback_text  = "-15  SYSTEM COMPROMISED!"
            self.feedback_color = RED
            self.locked = True
        else:
            self.score.add(30)
            self.feedback_text  = "+30  SAFE TORRENT VERIFIED!"
            self.feedback_color = GREEN
            self.level_complete = True
        self.feedback_timer = 90

    def handle_event(self, event):
        # ── Instruction screen ───────────────────────────────────────────
        if not self.Instruction_read:
            if self.handle_instruction_event(event):
                return                          # scroll consumed — don't dismiss
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.Instruction_read = True
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.Instruction_read = True
            return

        # ── Gameplay ─────────────────────────────────────────────────────
        if self.level_complete or self.locked:
            return
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            for i, rect in enumerate(self.rows_rect):
                if rect.collidepoint(event.pos):
                    self.validate_choice(i)
                    break

    def update(self):
        if self.feedback_timer > 0:
            self.feedback_timer -= 1
            if self.feedback_timer == 0 and self.locked:
                self.locked = False          # unlock for retry

    # ── Drawing ────────────────────────────────────────────────────────────
    def draw_table(self, surface):
        surface.blit(self.bg, (0, 0))
        mouse_pos = pg.mouse.get_pos()

        for i, rect in enumerate(self.rows_rect):
            name, se, le, t, size, uploader, _ = self.torrents[i]

            if rect.collidepoint(mouse_pos) and not self.locked:
                pg.draw.rect(surface, (200, 230, 250), rect)

            def blit_center(font, text, color, cx, cy):
                s = font.render(text, True, color)
                surface.blit(s, s.get_rect(center=(cx, cy)))

            surface.blit(
                self.level_font.render(name, True, (25, 30, 40)),
                (self.col_name_x, rect.y + rect.height // 2 - 8)
            )
            blit_center(self.level_font,    se,       (0, 140, 60),   self.col_se_cx,       rect.centery)
            blit_center(self.level_font,    le,       (190, 60, 30),  self.col_le_cx,       rect.centery)
            blit_center(self.level_font,    t,        (60, 60, 65),   self.col_time_cx,     rect.centery)
            blit_center(self.level_font,    size,     (60, 60, 65),   self.col_size_cx,     rect.centery)
            blit_center(self.uploader_font, uploader, (60, 60, 65),   self.col_uploader_cx, rect.centery)

        # Red tint while locked
        if self.locked and self.feedback_timer > 0:
            tint = pg.Surface((1280, 720), pg.SRCALPHA)
            tint.fill((180, 20, 20, 60))
            surface.blit(tint, (0, 0))

        # Feedback box
        if self.feedback_timer > 0:
            draw_box(surface,
                     color=self.feedback_color,
                     rect=pg.Rect(380, 300, 520, 90),
                     text=self.feedback_text,
                     text_color=PURE_WHITE,
                     font=self.open_sender_font)

    def draw_level_complete(self, surface):
        surface.fill((10, 10, 20))
        surface.blit(
            self.title_font.render("LEVEL 1 COMPLETE", True, (0, 255, 180)),
            (420, 240)
        )
        surface.blit(
            self.level_font.render(f"Score: {self.score.current_score}", True, PURE_WHITE),
            (420, 300)
        )
        surface.blit(
            self.level_font.render("Safe torrent identified. Proceeding to Level 2...", True, (160, 160, 160)),
            (420, 335)
        )

    def draw(self, surface):
        surface.fill((0, 0, 0))

        if not self.Instruction_read:
            self.draw_instructions(surface)
            return

        if self.level_complete and self.feedback_timer == 0:
            self.draw_level_complete(surface)
            return

        self.draw_table(surface)