import pygame
import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.heart import Heart
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class PowerUpManager:
    POWER_SHIELD = 5
    POWER_HEART = 5
    POWER_HOMMER = 5
    def __init__(self):
        self.obstacle = ObstacleManager()
        self.power_ups = []
        self.when_appears =  random.randint(250,300)
        self.duration = random.randint(3,5)
        self.life = 0
    
    def generate_power_ups_shield(self):
        power_up = Shield()
        self.power_ups.append(power_up)

    def generate_power_ups_heart(self):
        power_up = Heart()
        self.power_ups.append(power_up)

    def generate_power_ups_hammer(self):
        power_up = Hammer()
        self.power_ups.append(power_up)
    
    def update (self, game):
        if len(self.power_ups) == 0 and random.randint(0,300) < self.POWER_SHIELD:
            self.generate_power_ups_shield()
        elif len(self.power_ups) == 0 and random.randint(0,100) < self.POWER_HEART:
            self.generate_power_ups_heart()
        elif len(self.power_ups) == 0 and random.randint(0,200) < self.POWER_HOMMER:
            self.generate_power_ups_hammer()
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect) and power_up.type =="shield":
                power_up.start_time = pygame.time.get_ticks() #tiene un power activo
                game.player.type = power_up.type
                game.player.has_power_up = True
                game.player.power_up = power_up.start_time + (self.duration * 1000) # hasta cuando va a durar
                self.power_ups.remove(power_up) #va a desaparecer el obstacle de la pantalla
                
            if game.player.dino_rect.colliderect(power_up.rect) and power_up.type == "heart": # cuando lo toca
                power_up.start_time = pygame.time.get_ticks() #tiene un power activo
                game.player.type = power_up.type
                game.player.has_power_up = True
                game.player.power_up = power_up.start_time + (self.duration * 1000) # hasta cuando va a durar
                self.power_ups.remove(power_up) #va a desaparecer el obstacle de la pantalla
                
            if game.player.dino_rect.colliderect(power_up.rect) and power_up.type == "hammer": # cuando lo toca
                power_up.start_time = pygame.time.get_ticks() #tiene un power activo
                game.player.type = power_up.type
                game.player.has_power_up = True
                game.player.power_up = power_up.start_time + (self.duration * 1000) # hasta cuando va a durar
                self.power_ups.remove(power_up) #va a desaparecer el obstacle de la pantalla
 
            
    def draw (self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200,300)