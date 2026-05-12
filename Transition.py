
import pygame


class CyberTransition:
    FRAME_WIDTH = 1280
    FRAME_HEIGHT = 720
    FRAME_COUNT = 8

    def __init__(self, spritesheet_path: str, fps: int = 60):
        self.sheet = pygame.image.load(spritesheet_path).convert_alpha()
        self.frames = [
            self.sheet.subsurface(pygame.Rect(i * self.FRAME_WIDTH, 0, self.FRAME_WIDTH, self.FRAME_HEIGHT))
            for i in range(self.FRAME_COUNT)
        ]
        self.fps = fps
        self.frame_index = 0
        self.done = False
        # ~12 ticks per frame at 60 FPS → full transition ≈ 1.1–1.5s
        self.ticks_per_frame = max(1, fps // 5)
        self._tick = 0

    def update(self):
        if self.done:
            return
        self._tick += 1
        if self._tick >= self.ticks_per_frame:
            self._tick = 0
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.frame_index = len(self.frames) - 1
                self.done = True

    def draw(self, surface: pygame.Surface):
        surface.blit(self.frames[self.frame_index], (0, 0))

    def reset(self):
        self.frame_index = 0
        self.done = False
        self._tick = 0


