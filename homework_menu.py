"""ДЗ. Основываясь на  написанной программе внести изменение в свою menu.py,  по заданному условию 
предыдущего урока (продолжая свой стиль программы) и добавить 2 кнопки: Изменить цвет фона меню, Включить/выключить музыку. Соответственно добавить фоновую  музыку."""


from random import randint
import pygame
import pygame_gui
import sys


class Button_clicker:
    def __init__(self):
        pygame.init()

        self.window_width = 400
        self.window_height = 400
        self.window = pygame.display.set_mode((self.window_width, self.window_height),pygame.RESIZABLE) 
        pygame.display.set_caption("button clicker")
        pygame.mixer.music.load("backround_music.mp3")
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.play(-1)

        self.manager = pygame_gui.UIManager((self.window_width, self.window_height))

        self.value = 0
        self.step = 1

        self.settings_window = None
        self.step_input = None
        self.apply_button = None
        self.close_settings_button = None

        self.create_main_interface()

        self.clock = pygame.time.Clock()
        self.is_running = True
        self.new_color = (50,50,50)

    def create_main_interface(self):
        self.value_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(150, 30, 120, 50), text=f"value: {self.value}", manager=self.manager, object_id="#value_label")
        self.increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(120, 100, 160, 40), text="Increase", manager=self.manager, object_id="#increase_button")
        self.settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(120, 160, 160, 40), text="Settings", manager=self.manager, object_id="#settings_button")
        self.close_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(120, 220, 160, 40), text="Close", manager=self.manager, object_id="#close_button")
        self.game_music = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(120, 280, 160, 40), text="Music On/Off", manager=self.manager, object_id="#music_button")
        self.change_color = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(120, 340, 160, 40), text="Change Color", manager=self.manager, object_id="#color_button")
    
    def create_settings_window(self):
        if self.settings_window is not None:
            return

        self.settings_window = pygame_gui.elements.UIWindow(rect=pygame.Rect(50, 50, 300, 180), manager=self.manager, window_display_title="Settings", object_id="#settings_window")
        step_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(20, 30, 120, 30), text="Step:", manager=self.manager, container=self.settings_window)
        self.step_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(150, 30, 100, 30), manager=self.manager, container=self.settings_window)
        self.step_input.set_text(str(self.step))
        self.apply_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(50, 90, 80, 30), text="Apply", manager=self.manager, container=self.settings_window)
        self.close_settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(150, 90, 80, 30), text="Close", manager=self.manager, container=self.settings_window)

    def update_value_label(self):
        self.value_label.set_text(f"value: {self.value}")
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.is_running = False
                return
            
            self.manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.increase_button:
                    self.value += self.step
                    self.update_value_label()
                elif event.ui_element == self.settings_button:
                    self.create_settings_window()
                elif event.ui_element == self.close_button:
                    self.is_running = False
                elif event.ui_element == self.game_music:
                    self.toggle_music()
                elif event.ui_element == self.change_color:
                    self.change_bg_color()
                elif self.settings_window is not None:
                    if event.ui_element == self.apply_button:
                        try:
                            new_step = int(self.step_input.get_text())
                            if new_step > 0:
                                self.step = new_step
                            else:
                                self.step = 1
                            self.step_input.set_text(str(self.step))
                        except ValueError:
                            self.step_input.set_text(str(self.step))
                    elif event.ui_element == self.close_settings_button:
                        self.settings_window.kill()
                        self.settings_window = None
                        self.step_input = None
                        self.apply_button = None
                        self.close_settings_button = None

            if event.type == pygame_gui.UI_WINDOW_CLOSE:
                if event.ui_element == self.settings_window:
                    self.settings_window.kill()
                    self.settings_window = None
                    self.step_input = None
                    self.apply_button = None
                    self.close_settings_button = None

            if event.type == pygame.VIDEORESIZE:
                self.window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.manager.set_window.set_window_resolution((event.w, event.h))

    def toggle_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    
    def change_bg_color(self):
        current_color = self.window.get_at((0, 0))
        color_1 = randint(0, 255)
        color_2 = randint(0, 255)
        color_3 = randint(0, 255)
        self.new_color = (color_1, color_2, color_3)
        


    def run(self):
        while self.is_running:
            self.handle_events()
            time_delta = self.clock.tick(60) / 1000.0
            self.manager.update(time_delta)
            self.window.fill(self.new_color)
            self.manager.draw_ui(self.window)
            pygame.display.update()

        pygame.quit()
        sys.exit()
if __name__ == "__main__":
    app = Button_clicker()
    app.run()