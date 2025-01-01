import pygame as pg

class SCORE:
     def __init__ (self):
          self.font = pg.font.Font("./Assets/Fonts/ComicNeue-Bold.ttf", 90)
          self.score = 0
          self.color = (255,255,255)

     def draw(self,screen,SCREEN_WIDTH,HIGHSCORE):
          score_text = self.font.render(str(self.score), True, self.color)
          screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2, 40))
          if self.score >= HIGHSCORE:
               HIGHSCORE = self.score
               if self.score > 0:
                    self.color = (255, 255, 0 )
          else:
               self.color = (255, 255, 255)
          
          

          return HIGHSCORE