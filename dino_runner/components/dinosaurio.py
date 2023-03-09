import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING , DEAD , RUNNING_SHIELD , JUMPING_SHIELD ,DUCKING_SHIELD , DEFAULT_TYPE, SHIELD_TYPE

#PARA CORRER CON O SIN PODER 
RUN_IMG = {DEFAULT_TYPE:RUNNING, SHIELD_TYPE:RUNNING_SHIELD}
JUMO_IMG ={DEFAULT_TYPE: JUMPING , SHIELD_TYPE: JUMPING_SHIELD}
DUCK_IMG = {DEFAULT_TYPE: DUCKING , SHIELD_TYPE: DUCKING_SHIELD}

class Dinosaur(Sprite):
  X_POS = 80
  Y_POS = 310
  JUMP_SPEED = 8.5
  Y_POS_DUCK = 340
  
  def __init__(self):
    self.type = DEFAULT_TYPE
    #busca el tipo de imagen , se coloca la posicion de la imagen 
    self.image = RUN_IMG[self.type][0]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS
    self.step_index = 0
    self.dino_run = True
    self.dino_jump = False
    self.dino_duck = False
    self.jump_speed = self.JUMP_SPEED
    self.has_power_up = False
    self.power_time_up = 0
    
  def update(self, user_input):
    if self.dino_run:
      self.run()
    elif self.dino_jump:
      self.jump()
    elif self.dino_duck:
      self.duck()   
      
    if user_input[pygame.K_UP] and not self.dino_jump:
      pygame.mixer.music.load('dino_runner/components/music/jump.mp3')
      pygame.mixer.music.play()
      self.dino_jump = True
      self.dino_run = False
    elif user_input[pygame.K_DOWN] and not self.dino_jump:
      self.dino_jump = False
      self.dino_run = False
      self.dino_duck = True
    elif user_input[pygame.K_DOWN] and self.dino_jump:
      self.dino_rect = self.image.get_rect()
      self.dino_rect.x = self.X_POS
      self.dino_rect.y = self.Y_POS
      self.run()
    elif user_input[pygame.K_LEFT] and self.dino_run:
      self.left()
    elif user_input[pygame.K_RIGHT] and self.dino_run:
      self.right()

    elif not self.dino_jump:
      self.dino_jump = False
      self.dino_duck = False
      self.dino_run = True
      
    if self.step_index >= 10:
      self.step_index = 0

  
  def run(self):
    self.image = RUN_IMG[self.type][self.step_index // 5]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS
    self.step_index += 1
    
  def jump(self):
    self.image = JUMO_IMG[self.type]
    self.dino_rect.y -= self.jump_speed * 4
    self.jump_speed -= 0.8
    
    if self.jump_speed < -self.JUMP_SPEED:
      self.dino_rect.y = self.Y_POS
      self.dino_jump = False
      self.jump_speed = self.JUMP_SPEED
      
  def duck(self):
    self.image = DUCK_IMG[self.type][self.step_index // 5] # para saber que va a traer de imagen 
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS_DUCK
    self.step_index += 1
  
  def draw(self, screen):
    screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
    
  def right(self):
    self.X_POS += 5
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS
    if self.X_POS >= 1010:
      self.X_POS = 1010

  def left(self):
    self.X_POS -= 5
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS
    if self.X_POS <= 0:
      self.X_POS = 0
    
  def reset(self):
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS
    self.step_index = 0
    self.dino_run = True
    self.dino_jump = False
    self.dino_duck = False
    self.jump_speed = self.JUMP_SPEED
    
  def dead(self):
    self.image = DEAD