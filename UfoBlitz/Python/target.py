import pygame as pg
import math
import random

TARGET_SPRITE = pg.image.load("./Assets/Sprites/Target.png")

class TARGET:
     def __init__ (self):
          self.run_speed = 0.03
          self.delete_frame = 0 # 10000 is max
          self.delete = False
          self.speed = 0.01
          self.radius = 160
          self.dir_speed = 1.722
          self.x = -1000 # does not matter
          self.y = 0 # does not matter
          self.width = 100
          self.height = 100
          self.sprite = TARGET_SPRITE
          self.dir = 270
          self.direction = 1
          self.mask = pg.mask.from_surface(self.sprite)
          if random.randint(1,2) == 1:
               self.direction = 1
          else:
               self.direction = -1

          self.sprite = pg.transform.scale(self.sprite, (self.width, self.height))

          self.rotated_sprite = pg.transform.rotate(self.sprite, self.dir)

          self.sprite_rect = self.rotated_sprite.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))

     def run(self,screen):


          self.delete_frame += 1

          if self.delete_frame >= 8500:
               self.delete = True

          self.rotated_sprite = pg.transform.rotate(self.sprite, self.dir)

          self.sprite_rect = self.rotated_sprite.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))

          screen.blit(self.rotated_sprite, self.sprite_rect.topleft)

          if self.direction == 1:
               self.speed -= self.run_speed
          else:
               self.speed += self.run_speed

          x_center, y_center = 406, 320
          self.x = x_center + self.radius * math.cos(self.speed) 
          self.y = y_center + self.radius * math.sin(self.speed)

          if random.randint(1,400) == 1:
               if self.direction == 1:
                    self.direction = -1
               else:
                    self.direction = 1

          
          self.dir += self.direction * self.dir_speed
          self.mask = pg.mask.from_surface(self.rotated_sprite)

     