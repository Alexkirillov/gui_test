import pygame
import pygame_gui


class Button_clicker:
    def __init__(self):
        self.manager = pygame_gui.UIManager((1000, 1000))
        self.button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(400,400,100,100), text="press button", manager=self.manager)
        pygame.mixer.music.load("backround_music.mp3")
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.play(-1)
    
    def click_counter(self):
        if self.button.check_pressed():
            print("button pressed")
    def update(self, time_delta):
        self.manager.update(time_delta)
        self.click_counter()

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("click button")
running =True
time = pygame.time.Clock()

button_clicker = Button_clicker()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    button_clicker.update(1.0/60.0)
    screen.fill((255, 255, 255))
    button_clicker.manager.draw_ui(screen)
    
    pygame.display.flip()
    time.tick(60)
pygame.quit()

