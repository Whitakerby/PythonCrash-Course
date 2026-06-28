import pygame

from ship import Ship

class blue:
    def __init__(self):
        pygame.init()

        # self.screen = pygame.display.set_mode()
        self.bg_color = (0, 0, 255)
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('蓝色背景窗口')
        self.ship = Ship(self)


    def run_game(self):
        while True:

            self.screen.fill(self.bg_color)
            self.ship.blitme()
            pygame.display.flip()
if __name__ == '__main__':
    ai = blue()
    ai.run_game()

