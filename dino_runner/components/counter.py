import pygame

from dino_runner.utils.constants import FONT_STYLE

class Counter:
  def __init__(self):
    self.count = 0
  
  #vamos a estar contado el tiempo, tiempo recor, y la vida,
  def update(self):
    self.count += 1
      
  #mandamo a reiniciar el timepo. la vida, tiempo recor.
  def reset(self):
    self.count = 0
  
  #para saber el tiempo recor
  def set_count(self, value):
    self.count = value