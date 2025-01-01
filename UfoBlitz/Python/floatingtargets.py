import pygame as pg
import math
import random

TARGET_SPRITE = pg.image.load("./Assets/Sprites/Target.png")

class FLOATINGTARGET:
     def __init__ (self):
          self.speed = 5
          self.delete_frame = 0 # 10000 is max
          self.delete = False

          self.y = random.randint(0,700)
          self.width = 100
          self.height = 100
          self.sprite = TARGET_SPRITE
          self.dir = 270
          self.direction = 1
          self.mask = pg.mask.from_surface(self.sprite)
          if random.randint(1,2) == 1:
               self.direction = 1
               self.x = 0
          else:
               self.direction = -1
               self.x = 1200
          

          self.sprite = pg.transform.scale(self.sprite, (self.width, self.height))

          self.rotated_sprite = pg.transform.rotate(self.sprite, self.dir)

          self.sprite_rect = self.rotated_sprite.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))

     def run(self,screen):

          self.delete_frame += 1

          if self.delete_frame >= 400:
               self.delete = True

          self.x += (self.direction * self.speed)

          self.rotated_sprite = pg.transform.rotate(self.sprite, self.dir)
          self.sprite_rect = self.rotated_sprite.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))

          screen.blit(self.rotated_sprite, self.sprite_rect.topleft)

          self.dir += 1
          self.mask = pg.mask.from_surface(self.rotated_sprite)

     