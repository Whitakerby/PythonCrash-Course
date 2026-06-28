# 导入第三方库
import sys
import pygame

from settings import Settings
from ship import Ship

# 创建管理游戏资源和行为的类
class AlienInvasion:
    # 初始化游戏并创建游戏资源
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

    def run_game(self):
        # 开始游戏的主循环
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    # 响应按键和鼠标事件
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # 响应按键
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def _check_keyup_events(self, event):
        # 响应松开
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        # 更新屏幕上的图像
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # 让绘制的屏幕可见
        pygame.display.flip()


# 创建游戏实例并运行游戏
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
