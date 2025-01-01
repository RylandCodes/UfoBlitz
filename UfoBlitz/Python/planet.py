import pygame as pg
import random

PLANET_SPRITE = pg.image.load("./Assets/Sprites/Planet.png")
PLANET_SAD = pg.image.load("./Assets/Sprites/PlanetSad.png")

class PLANET:
     def __init__ (self):
          self.frame = 0 # 10
          self.x = 330
          self.y = 240
          self.width = 250
          self.height = 250
          self.sprite = PLANET_SPRITE
          self.dir = 0
          self.mask = pg.mask.from_surface(self.sprite)
          self.hit = False
          if random.randint(1,2) == 1:
               self.direction = 1.5
          else:
               self.direction = -1.5
          self.sprite = pg.transform.scale(self.sprite, (self.width, self.height))
     def run(self,screen):
          if self.hit:
               self.sprite = PLANET_SAD
               self.frame += 1
               if self.frame >= 40:
                    self.sprite = PLANET_SPRITE
                    self.frame = 0
                    self.hit = False
                    self.width = 250
                    self.height = 250
          self.sprite = pg.transform.scale(self.sprite, (self.width, self.height))
          self.rotated_sprite = pg.transform.rotate(self.sprite, self.dir)
          self.sprite_rect = self.rotated_sprite.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))

          screen.blit(self.rotated_sprite, self.sprite_rect.topleft)

          self.dir -= self.direction

          self.mask = pg.mask.from_surface(self.rotated_sprite)

          
          