import pygame 
from dino_runner.components.dinosaurio import Dinosaurio
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        #coloca el titulo de la ventana
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        #para colocar altura y ancho
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        #rapides del juego
        self.game_speed = 20
        #posicion de background
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaurio()
        self.obstacle_manager = ObstacleManager()

    #metodo que hacer correr cada metodo del programa
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    #para recorrer un evento 
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                
    #actualizar el evento del juego 
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        

    def draw(self):
        #tick trae lo que se va a mostrar por segundo
        self.clock.tick(FPS)
        #el fill es para traer los colores del juego
        self.screen.fill((255, 255, 255))
        #draw.background es para dibujar la imagen
        self.draw_background()
        #update y flip es para actualizar el display
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        

    def draw_background(self):
        #obtener el ancho de la imagen
        #BG trae la imagen, blit es que dibuje
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
