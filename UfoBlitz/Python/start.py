import pygame as pg

TITLE = pg.image.load("./Assets/Sprites/Title.png")

TARGET = pg.image.load("./Assets/Sprites/Target.png")

FSPRITE = pg.image.load("./Assets/Sprites/F.png")

class START:
     def __init__ (self,highscore):
          self.title_x = 150
          self.title_y = 0
          self.title_width = 600
          self.title_height = 400
          self.title_sprite = TITLE

          self.random_target_sprite = TARGET
          self.random_target_x = 150
          self.random_target_y = 400
          self.random_target_height = 100
          self.random_target_width = 100
          self.random_target_dir = 0
          self.random_target_sprite = pg.transform.scale(self.random_target_sprite, (self.random_target_width,self.random_target_height))
          self.random_target_rotated = None

          self.f_sprite = FSPRITE
          self.f_sprite_x = 50
          self.f_sprite_y = 560
          self.f_sprite_width = 200
          self.f_sprite_height = 130

          self.font = pg.font.Font("./Assets/Fonts/ComicNeue-Bold.ttf", 40)
          self.hscore = highscore
          self.color = (255,255,255)
          self.hx = 320
          self.hy = 300
     def draw(self,screen):
          self.title_sprite = pg.transform.scale(self.title_sprite, (self.title_width,self.title_height))
          screen.blit(self.title_sprite,(self.title_x,self.title_y))

          rotated_sprite = pg.transform.rotate(self.random_target_sprite, self.random_target_dir)
          rotated_rect = rotated_sprite.get_rect(center=(self.random_target_x + self.random_target_width // 2, 
                                                            self.random_target_y + self.random_target_height // 2))
          rotated_rect2 = rotated_sprite.get_rect(center=(self.random_target_x + 150 + self.random_target_width // 2, 
                                                            self.random_target_y + 80 + self.random_target_height // 2))
          self.random_target_x += 3
          self.random_target_dir += 1

          screen.blit(rotated_sprite, rotated_rect)

          screen.blit(rotated_sprite, rotated_rect2)

          if self.random_target_x >= 1200:
               self.random_target_x = -200

          self.f_sprite = pg.transform.scale(self.f_sprite, (self.f_sprite_width,self.f_sprite_height))
          screen.blit(self.f_sprite,(self.f_sprite_x,self.f_sprite_y))

          score_text = self.font.render(f"Highscore {self.hscore}", True, self.color)
          screen.blit(score_text, (self.hx,self.hy))