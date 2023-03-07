import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Birds(Obstacle):
    def __init__(self, image):
        self.image =BIRD[0]
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.bird = self.image.get_rect()
        self.bird.y = 325
        self.bird.x = 90
        
    def run_brids(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.brid = self.image.get_rect()
        self.bird.x = self.x
        self.bird.y = self.y
        
    def draw(self, screen):
        screen.blit(self.image,(self.bird.x, self.bird.y))