import pygame
from dino_runner.utils.constants import FONT_STYLE , SCREEN_HEIGHT ,SCREEN_WIDTH
class Menu:
    hald_screen_width = SCREEN_WIDTH // 2
    hald_screen_height = SCREEN_HEIGHT // 2
    def __init__(self,mensaje, screen):
      screen.fill((255,255,255))
      self.font = pygame.font(FONT_STYLE,0 )
      self.text = self.font.render(mensaje, True,(0,0,0))
      self.text_rect = self.text.get_rect()
      self.text_rect.center = (self.hald_screen_width,self.hald_screen_height)
      
    def update(self):
        pass
    def draw(self, screen ):
        pass