import pygame as pg
import math

class BULLET:
    def __init__(self, direction, x, y, screen):
        self.screen = screen
        self.direction = math.radians(direction)
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.color = (255,255,255)  # White color
        self.speed = 9
        self.remove = False

        self.vx = math.cos(self.direction) * self.speed
        self.vy = math.sin(self.direction) * self.speed

        self.mask_surface = pg.Surface((self.width, self.height), pg.SRCALPHA)
        pg.draw.circle(self.mask_surface, (255, 255, 255), (self.width // 2, self.height // 2), self.width // 2)
        self.mask = pg.mask.from_surface(self.mask_surface)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x >= 900 or self.x <= 0 or self.y >= 900 or self.y <= 0:
            self.remove = True

    def draw(self,planet,score,target_list):
        self.rect = pg.draw.circle(self.screen, self.color, (self.x, self.y), self.width // 2)

        planet_offset = (int(self.x - planet.sprite_rect.x), int(self.y - planet.sprite_rect.y))
        for target in target_list:
            target_offset = (int(self.x - target.sprite_rect.x), int(self.y - target.sprite_rect.y))
            if target.mask.overlap(self.mask, target_offset):
                self.remove = True
                target.delete = True
                score.score += 1

        if planet.mask.overlap(self.mask, planet_offset):
            self.remove = True
            planet.hit = True
            score.score -= 1
        
