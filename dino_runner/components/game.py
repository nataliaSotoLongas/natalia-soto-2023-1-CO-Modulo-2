import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE , RESET , GAMEOVER ,CLOUD, DEFAULT_TYPE, ICON_1
from dino_runner.components.dinosaurio import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu
from dino_runner.components.counter import Counter
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(CLOUD)
        pygame.display.set_icon(RESET)
        pygame.display.set_icon(GAMEOVER)
        self.icon = ICON_1[0]
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu(self.screen)
        self.running = False
        self.score = Counter()
        self.death_count = Counter()
        self.highest_score = Counter()
        self.power_up_manager = PowerUpManager()
        self.stop = 0
        self.colors = 0
        self.step = 0
        
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
        
    #aqui es donde va a correr el juego
    def run(self):
        self.reset_game()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.time.delay(1000)    
    
    #la accion vacica que hace funcionar cualquier juego
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                
    #aqui se hace todas las haciones del juego
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.score.update()
        self.update_game_speed()
    
    #aqui se hace todo lo que se dibuja en la pantalla
    def draw(self):
        self.clock.tick(FPS)
        self.Black_While()
        self.draw_background()
        self.draw_clouds()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen) # se va a mover a la izquierda 
        self.draw_power_up_time()
        self.draw_score()
        pygame.display.update()
        #pygame.display.flip()
        
    # fondo de color
    def Black_While(self):
        if self.score.count == 1:
            self.colors = 0
            self.player.X_POS = 80
            self.player.dino_rect.x = self.player.X_POS
        self.colors += 1
        if self.colors >= 200:
            self.screen.fill((0, 0, 0))
            if self.colors >= 400:
                self.colors = 0
        else:
            self.screen.fill((255,255,255))
            
    #el metodo para mostrar las nubes
    def draw_clouds(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1020, self.y_pos_bg -250))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1070, self.y_pos_bg -250))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2030, self.y_pos_bg -300))
    
    #el metodo para mostrar la carretera
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
        
    def Icon_walk(self):
        if self.step >= 800:
            self.step = 0
        self.icon = ICON_1[0] if self.step < 400 else ICON_1[1]
        self.step += 1
        
    #metodo para mostar el menu
    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        if self.death_count.count == 0:
            self.Icon_walk()
            self.screen.blit(self.icon,(half_screen_width -90, half_screen_height-200))
            self.menu.draw(self.screen, 'Press any key to start ...', half_screen_width +180)
        else:
            self.screen.blit(GAMEOVER, (half_screen_width -380, half_screen_height - 140,))
            self.screen.blit(RESET, (half_screen_width - 50, half_screen_height - 70,))
            self.update_highest_score()
            self.menu.draw(self.screen, 'Game over. Press any key to restart',half_screen_width -30, half_screen_height +50, )
            self.menu.draw(self.screen, f'Your score: {self.score.count}', half_screen_width, 370, )
            self.menu.draw(self.screen, f'Highest score: {self.highest_score.count}', half_screen_width, 390, )
            self.menu.draw(self.screen, f'Total deaths: {self.death_count.count}', half_screen_width, 410, )    
        self.menu.update(self)
    
    #metodo para aumentar la velocidad
    def update_game_speed(self):
        if self.score.count % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5
        if self.score == 0 and self.game_speed > 0:
            self.game_speed = 0
    
    #metodo para defenir el tiempo recor
    def update_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)
            
    #dibujar el tiempo con su color
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE,20)
        if self.colors >= 200:
            text = font.render(f'Score: {self.score.count}' ,True, (255,255,255))
        else:
            text = font.render(f'Score: {self.score.count}' ,True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000,50)
        self.screen.blit(text,text_rect)
        
    #al momento de terminar la partida es lo que se resetea
    def reset_game(self):
        self.obstacle_manager.reset_obstacles() #reseteamos los ostaculos
        self.score.reset() #reseteamos el tiempo
        self.game_speed = self.GAME_SPEED #velocidad
        self.player.reset() #resetea la pocicion del dinosaurio
    
    #el metodo para mostar el poder en la panatalla
    def  draw_power_up_time(self):
        if self.player.has_power_up: #el poder debe estar activado
            self.stop += 1
            if self.stop <= 80: #si le queda tiempo se manda un nuevo mensaje
                self.menu.draw(self.screen, f'{self.player.type.capitalize()} enabled for {self.stop} seconds',500,50 )
            else:
                self.has_power_up = False
                self.player.type =  DEFAULT_TYPE