import pygame 
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, image, Obstacle_type):
        self.image = image
        self.obstacle_type = Obstacle_type 
        self.rect =  self.image[Obstacle_type].get_rect()
        self.rect.x = SCREEN_WIDTH
        
    def uptade(self, game_speed,obstacles):
       self.rect.x -= game_speed
       
       if self.rect.x <- self.rect.width:
           obstacles.pop()
    
    def draw(self, screen):
        screen.blit(self.image[self.obstacle_type], (self.rect.x, self.rect.y))