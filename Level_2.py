import pygame as pg

from level_1 import LevelOne
from menu import NEON_CYAN, PURE_WHITE, GREEN, RED, draw_box


class LevelTwo(LevelOne):
    def __init__(self,score):
        super().__init__(score)
        self.Instruction_read = False

        # ── Level 2 background (1337Y listing page) ──────────────────────
        self.bg = pg.image.load('Graphic/level_2_graphics/level_2_closed_view.png').convert_alpha()
        self.uploader_font = pg.font.Font('Font/Level_1_font/OpenSans-Bold.ttf', 13)

        # ── Row hitboxes — measured against the background art ───────────
        row_tops = [311, 346, 380, 414, 448, 484, 519, 556, 594, 634, 669]
        row_heights = [35, 34, 34, 34, 36, 35, 37, 38, 40, 35, 37]
        TABLE_X = 54
        TABLE_W = 1199 - 54
        self.rows_rect = [
            pg.Rect(TABLE_X, top, TABLE_W, h)
            for top, h in zip(row_tops, row_heights)
        ]

        # Column centers, matched to the header labels in the background art
        self.col_name_x = 64
        self.col_se_cx = 750
        self.col_le_cx = 830
        self.col_time_cx = 925
        self.col_size_cx = 1031
        self.col_uploader_cx = 1141

        # (name, seeders, leechers, time, size, uploader, is_malicious)
        self.torrents = [
            ("Batman.2022.HDCAM.x264-FAKE.exe", "3", "512", "4 hours ago", "1.4 GB", "newuser88234", True),
            ("FREE BATMAN 2022 FULL MOVIE HD!!! NO VIRUS!!!", "145", "12", "1 day ago", "2.1 GB", "MovieKing_2026", True),
            ("Batman.2022.1080p.BluRay.x264-GROUP", "2453", "187", "3 months ago", "11.2 GB", "YTS.MX [Verified]", False),
            ("Batman.2022.1080p.BluRay.x264-GR0UP", "89", "94", "2 months ago", "10.8 GB", "YT5.MX", True),
            ("Batman.2022.2160p.REMUX-FREE", "612", "4", "2 minutes ago", "980 MB", "xXx_d4rkn3t_xXx", True),
            ("Batman.2022.1080p.mkv.exe", "44", "201", "6 hours ago", "9.6 GB", "Anonymous", True),
            ("WORKING 100% Batman 2022 BluRay [PASSWORD INSIDE]", "22", "340", "5 hours ago", "3.2 GB", "seed3r_x99", True),
            ("Batman.2022.1080p.WEB-DL.x264-GROUP", "1850", "1620", "3 weeks ago", "780 MB", "GROUP_Official", True),
            ("Batman.2022.1080p.BluRay.x265-GROUP.zip", "5", "290", "1 month ago", "14.9 GB", "user_38291", True),
            ("[CLICK HERE] Batman 2022 Full Movie + Bonus Codec Pack", "67", "410", "8 hours ago", "650 MB", "codec_helper_01", True),
            ("Batman.2022.1080p.BluRay.DDP5.1.Atmos-GROUP", "3120", "8", "14 hours ago", "11.0 GB", "GROUP", True),
        ]

        self.locked = False
        self.level_complete = False

        self.instructions = [
            "LEVEL 2: TORRENT INSPECTION",# i = 0
            "",
            "You are attempting to download Batman (2022)",
            "from 1337Y. Analyse each listing carefully.",
            "One torrent is safe. The rest are traps.",
            "",
            "── SEEDER / LEECHER RATIO ──",# i = 6
            "A healthy torrent has significantly more",
            "seeders than leechers.",
            "  2000 SE / 150 LE  =  Trustworthy",
            "  2 SE   / 500 LE   =  Dead or malicious",
            "",
            "── UPLOADER REPUTATION ──",# i = 12
            "Verified uploaders carry badges and have",
            "a consistent upload history.",
            "Threat actors use disposable accounts,",
            "random usernames, or impersonate trusted",
            "uploaders with subtle name alterations.",
            "",
            "── COMMENTS SECTION ──",# i = 19
            "Scan for explicit warnings:",
            "  'malware'  'miner'  'stealer'  'fake'",
            "Legitimate comments contain technical",
            "detail: specs, install issues, bug reports.",
            "Treat vague praise as a red flag:",
            "  'WORKING 100%!!!', repeated short posts.",
            "",
            "── TITLE FORMATTING ──",# i = 27
            "Legitimate releases follow a standard:",
            "  Batman.2022.1080p.BluRay.x264-GROUP",
            "Malicious uploads often use urgency",
            "or reassurance in the title itself:",
            "  FREE BATMAN HD FULL NO VIRUS.exe",
            "",
            "── FILE SIZE ──",# i = 34
            "A 1080p film is typically 8 - 15 GB.",
            "Anything significantly smaller is",
            "compressed, fake, or weaponised.",
            "",
            "── FILE LIST ──",# i = 39
            "A legitimate release contains:",
            "  .mkv / .mp4  and subtitle files",
            "Abort if you find:",
            "  .exe  .scr  .bat  .cmd  setup files",
            "  password notes  or browser extensions",
            "",
            "Correct download  =  +Points",
            "Incorrect download  =  System compromised.",
            "",
            "Click anywhere or press SPACE to begin."
        ]
    def validate_choice(self, i):
        name, se, le, time, size, uploader, is_malicious = self.torrents[i]
        if is_malicious:
            self.score.deduct(15)
            self.feedback_text = "-15  SYSTEM COMPROMISED!"
            self.feedback_color = RED
            self.locked = True
        else:
            self.score.add(30)
            self.feedback_text = "+30  SAFE TORRENT VERIFIED!"
            self.feedback_color = GREEN
            self.level_complete = True
        self.feedback_timer = 90

    def handle_event(self, event):
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if not self.Instruction_read:
                        self.Instruction_read = True

            if event.type == pg.MOUSEBUTTONDOWN:
                if not self.Instruction_read:
                    self.Instruction_read = True
                    return
                if self.level_complete or self.locked:
                    return
                for i, rect in enumerate(self.rows_rect):
                    if rect.collidepoint(event.pos):
                        self.validate_choice(i)
                        break

    def update(self):
            if self.feedback_timer > 0:
                self.feedback_timer -= 1
                if self.feedback_timer == 0 and self.locked:
                    self.locked = False  # retry: list reappears, choice not yet made

    def draw_table(self, surface):
            surface.blit(self.bg, (0, 0))
            mouse_pos = pg.mouse.get_pos()

            for i, rect in enumerate(self.rows_rect):
                name, se, le, time, size, uploader, is_malicious = self.torrents[i]
                if rect.collidepoint(mouse_pos) and not self.locked:
                    pg.draw.rect(surface, (200, 230, 250), rect)

                name_surf = self.level_font.render(name, True, (25, 30, 40))
                surface.blit(name_surf, (self.col_name_x, rect.y + rect.height // 2 - 8))

                se_surf = self.level_font.render(se, True, (0, 140, 60))
                surface.blit(se_surf, se_surf.get_rect(center=(self.col_se_cx, rect.centery)))

                le_surf = self.level_font.render(le, True, (190, 60, 30))
                surface.blit(le_surf, le_surf.get_rect(center=(self.col_le_cx, rect.centery)))

                time_surf = self.level_font.render(time, True, (60, 60, 65))
                surface.blit(time_surf, time_surf.get_rect(center=(self.col_time_cx, rect.centery)))

                size_surf = self.level_font.render(size, True, (60, 60, 65))
                surface.blit(size_surf, size_surf.get_rect(center=(self.col_size_cx, rect.centery)))

                uploader_surf = self.uploader_font.render(uploader, True, (60, 60, 65))
                surface.blit(uploader_surf, uploader_surf.get_rect(center=(self.col_uploader_cx, rect.centery)))

            if self.locked and self.feedback_timer > 0:
                tint = pg.Surface((1280, 720), pg.SRCALPHA)
                tint.fill((180, 20, 20, 60))
                surface.blit(tint, (0, 0))

            if self.feedback_timer > 0:
                draw_box(
                    surface,
                    color=self.feedback_color,
                    rect=pg.Rect(380, 300, 520, 90),
                    text=self.feedback_text,
                    text_color=PURE_WHITE,
                    font=self.open_sender_font
                )

    def draw_level_complete(self, surface):
            surface.fill((10, 10, 20))
            title = self.instruction_font.render("LEVEL 2 COMPLETE", True, (0, 255, 180))
            surface.blit(title, (350, 220))
            score_line = self.level_font.render(
                f"Score: {self.score.current_score}", True, PURE_WHITE
            )
            surface.blit(score_line, (350, 320))
            sub = self.level_font.render(
                "Safe torrent identified. Proceeding to Level 3...", True, (180, 180, 180)
            )
            surface.blit(sub, (350, 360))

    def draw(self, surface):
            surface.fill((0, 0, 0))
            if not self.Instruction_read:
                surface.fill((10, 10, 20))
                y = 0
                for line in self.instructions:
                    if line == self.instructions[0]:
                        text_surface = self.instruction_font.render(line, True, (0, 255, 180))
                        surface.blit(text_surface, (200, y))
                        y += 50
                    elif line == "":
                        y += 12
                    elif line.startswith("──"):
                        text_surface = self.instruction_font.render(line, True, (0, 255, 180))
                        surface.blit(text_surface, (200, y))
                        y += 28
                    elif line.startswith("  "):
                        text_surface = self.level_font.render(line, True, (180, 180, 100))
                        surface.blit(text_surface, (220, y))  # extra indent
                        y += 18
                    else:
                        text_surface = self.level_font.render(line, True, (200, 200, 200))
                        surface.blit(text_surface, (200, y))
                        y += 18

                return

            if self.level_complete and self.feedback_timer == 0:
                self.draw_level_complete(surface)
                return

            self.draw_table(surface)