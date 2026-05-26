import pygame as pg

from level_1 import LevelOne


class LevelTwo(LevelOne):
    def __init__(self,score):
        super().__init__(score)
        self.Instruction_read = False
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
        def handle_event(self, event):
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if not self.Instruction_read:
                        self.Instruction_read = True

            if event.type == pg.MOUSEBUTTONDOWN:
                if not self.Instruction_read:
                    self.Instruction_read = True
                    return
            pass
        def update(self):
            pass
        def draw(self, surface):
            surface.fill((0, 0, 0))
            if not self.Instruction_read:
                surface.fill((10, 10, 20))

                y = 10
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
            pass
