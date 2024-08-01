from .vec2 import Vec2
import pygame

class Obj:
    def __init__(self, pos: Vec2):
        self.pos = pos

class SpriteObject(Obj):
    def __init__(self, pos, spritePath):
        super().__init__(pos)
        self.sprite = pygame.image.load(spritePath)
        self.rect = self.sprite.get_rect(center=(self.pos.x, self.pos.y))

    def draw(self, surface):
        surface.blit(self.sprite, self.rect.topleft)
