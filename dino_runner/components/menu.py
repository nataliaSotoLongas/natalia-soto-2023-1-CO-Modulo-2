import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH
class Menu:
  half_screen_height = SCREEN_HEIGHT // 2
  half_screen_width = SCREEN_WIDTH // 2
  
  def __init__(self, message, screen):
    screen.fill((255, 255, 255))
    self.font = pygame.font.Font(FONT_STYLE, 30)
    self.text = self.font.render(message, True, (0, 0, 0))
    
    self.text_rect = self.text.get_rect()
    self.text_rect.center = (self.half_screen_width, self.half_screen_height)
    
    self.text_score = self.font.render(message, True, (0, 0, 0))
    self.text_rect_score = self.text_score.get_rect()
    
    self.text_max_deaths = self.font.render(message, True, (0, 0, 0))
    self.text_rect_max_deaths = self.text_max_deaths.get_rect()
    
    self.text_deaths = self.font.render(message, True, (0, 0, 0))
    self.text_rect_deaths = self.text_deaths.get_rect()
    
  
  def update(self,game):
    pygame.display.update()
    self.handle_event_on_menu(game)
  
  def draw(self, screen):
    screen.blit(self.text, self.text_rect)
    screen.blit(self.text_score , self.text_rect_score )
    screen.blit(self.text_max_deaths , self.text_rect_max_deaths )
    screen.blit(self.text_deaths, self.text_rect_deaths)
    
  def reset_screen_color(self, screen):
    screen.fill((255, 255, 255,))
    
  def handle_event_on_menu(self, game):
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        game.running = False
        game.playing = False
      elif event.type == pygame.KEYDOWN:
        game.run()
  
  def update_message(self, message):
    self.text = self.font.render(message, True,(0,0,0))
    self.text_rect = self.text.get_rect()
    self.text_rect.center=(self.half_screen_width , self.half_screen_height)
    
  def update_score(self, message):
    self.text_score = self.font.render(message, True,(0,0,0))
    self.text_rect_score = self.text_score.get_rect()
    self.text_rect_score.center=(self.half_screen_width -20, self.half_screen_height +40)
  
  def update_max_deaths(self, message):
    self.text_max_deaths = self.font.render(message, True,(0,0,0))
    self.text_rect_max_deaths = self.text_max_deaths.get_rect()
    self.text_rect_max_deaths.center=(self.half_screen_width -20, self.half_screen_height +80)
    
  def update_deaths(self, message):
    self.text_deaths = self.font.render(message, True,(0,0,0))
    self.text_rect_deaths = self.text_deaths.get_rect()
    self.text_rect_deaths.center=(self.half_screen_width -20, self.half_screen_height +120)