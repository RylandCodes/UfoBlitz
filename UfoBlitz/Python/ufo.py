import pygame as pg
import math

from Python.bullet import BULLET

UFO_SPRITE = pg.image.load("./Assets/Sprites/UFO.png")

class UFO:
     def __init__ (self):
          self.debounce_frame = 0 # 10 is reset
          self.debounce = False
          self.firerate = 100
          self.speed = 0.01
          self.radius = 300
          self.dir_speed = 1.722
          self.x = -1000 # does not matter
          self.y = 0 # does not matter
          self.width = 105
          self.height = 105
          self.sprite = UFO_SPRITE
          self.dir = 270
          self.direction = 1 # 1 is right , - 1 is left
          self.sprite = pg.transform.scale(self.sprite, (self.width, self.height))
          self.mask = pg.mask.from_surface(self.sprite)
          
     def run(self,screen,bullet_list,floating_target_list,gameover):
          if self.debounce:
               self.debounce_frame += 1
               if self.debounce_frame >= 30:
                    self.debounce = False
                    self.debounce_frame = 0

          self.rotated_sprite = pg.transform.rotate(self.sprite, self.dir)

          sprite_rect = self.rotated_sprite.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))

          screen.blit(self.rotated_sprite, sprite_rect.topleft)

          
          if self.direction == 1:
               self.speed -= 0.03
          else:
               self.speed += 0.03

          x_center, y_center = 390, 310
          self.x = x_center + self.radius * math.cos(self.speed) 
          self.y = y_center + self.radius * math.sin(self.speed)

          keys = pg.key.get_pressed()
          if keys[pg.K_RIGHT] or keys[pg.K_d]:
               self.direction = -1
          if keys[pg.K_LEFT] or keys[pg.K_a]:
               self.direction = 1
          
          self.dir += self.direction * self.dir_speed

          if keys[pg.K_SPACE] or keys[pg.K_q]:
               bullet_list = self.fire(screen,bullet_list)

          self.mask = pg.mask.from_surface(self.rotated_sprite)

          # FIX
          for target in floating_target_list:
               target_offset = (int(self.x - target.sprite_rect.x), int(self.y - target.sprite_rect.y))
               if target.mask.overlap(self.mask, target_offset):
                    print("Player died Good Game")
                    gameover = True
                    target.delete = True
                    
          return bullet_list,gameover
          
     def fire(self,screen,bullet_list):
          if not self.debounce:
               SHOOT_SOUND = pg.mixer.Sound("./Assets/Sounds/Laser.mp3")
               SHOOT_SOUND.set_volume(0.5)
               SHOOT_SOUND.play()
               self.debounce = True
               bullet_x = self.x + self.width // 2
               bullet_y = self.y + self.height // 2 + 10 

               
               center_x, center_y = 390, 310

               
               dx = center_x - bullet_x
               dy = center_y - bullet_y
               angle = math.degrees(math.atan2(dy, dx))
               bullet = BULLET(angle, bullet_x - 5, bullet_y, screen)

               bullet_list.append(bullet)
          return bullet_list
