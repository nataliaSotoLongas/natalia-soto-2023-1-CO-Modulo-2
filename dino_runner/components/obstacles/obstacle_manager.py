import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Birds
from dino_runner.utils.constants import SMALL_CACTUS , LARGE_CACTUS , BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.condicion = 0
    def update(self, game):
        #si no hay obstaculos vamos a crear uno nuevo
        
        if len(self.obstacles) == 0:
            if self.condicion == 0:
                cactus = Cactus(SMALL_CACTUS)
                self.obstacles.append(cactus)
                self.condicion += 1
            
            elif self.condicion == 1:
                birds = Birds(BIRD)
                self.obstacles.append(birds)
                self.condicion += 1
                
            elif self.condicion == 2:
                cactus= Cactus(LARGE_CACTUS)
                self.obstacles.append(cactus)
                self.condicion = 0
           
        for obstacles in self.obstacles: 
            obstacles.update(game.game_speed ,self.obstacles)
            if game.player.dino_rect.colliderect(obstacles.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

           
                      
    def draw(self,screen):
        for obstacle in self.obstacles:
           obstacle.draw(screen)
       