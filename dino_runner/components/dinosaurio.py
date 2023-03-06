import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING , JUMPING, DUCKING

class Dinosaurio(Sprite):
    Y_POS = 310
    JUMP_SPEED = 8.5
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.x = 80
        self.dino_rect.x = self.x
        self.dino_rect.y =  self.Y_POS 
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_speed = self.JUMP_SPEED
        
    def update(self, user_input):
        self.step_index +=1
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
            
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_duck = False
            self.dino_run = False
            
        if user_input[pygame.K_DOWN] and not self.dino_duck:
            self.dino_jump = False
            self.dino_duck = True
            self.dino_run = False
            
        if user_input[pygame.K_RIGHT]:
            self.dino_rect = self.image.get_rect()
            self.x += 5
            self.dino_rect.x = self.x
            self.dino_rect.y =  self.Y_POS
            if self.x >= 1010:
                self.x = 1010
            
        if user_input[pygame.K_LEFT]:
            self.dino_rect = self.image.get_rect()
            self.x -= 5
            self.dino_rect.x = self.x
            self.dino_rect.y =  self.Y_POS
            if self.x <= 0:
                self.x = 0
            
        elif not self.dino_duck and not self.dino_jump:
            self.dino_jump = False
            self.dino_duck = False
            self.dino_run = True
            
        
            
        if self.step_index >= 10:
            self.step_index =0
    
    def run(self):
        self.image =  RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x
        self.dino_rect.y = self.Y_POS 
        
    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_speed * 4
        self.jump_speed -= 0.8
        
        if self.jump_speed <-self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED
        
    def draw(self, screen):
        screen.blit(self.image,(self.dino_rect.x, self.dino_rect.y))
        
    def duck(self):
        self.image =  DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.Y_POS = 345
        self.dino_rect.x = self.x
        self.dino_rect.y =  self.Y_POS
        
        if self.step_index >= 10:
            self.Y_POS = 310
            self.dino_duck = False
            self.dino_run = True      