# 导入第三方库
import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

# 创建管理游戏资源和行为的类
class AlienInvasion:
    # 初始化游戏并创建游戏资源
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # self.screen = pygame.display.set_mode(
            # (self.settings.screen_width, self.settings.screen_height))
        #设置背景颜色
        self.bg_clock = (230, 230, 230)

        # self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self):
        #创建外星人群
        #创建一个外星人
        alien = Alien(self)
        self.aliens.add(alien)


    def run_game(self):
        # 开始游戏的主循环
        while True:

            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
        # 监视键盘和鼠标事件

     #响应按键和鼠标事件
    def _check_events(self):
            #响应鼠标和键盘事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    #     self.ship.rect.x += 1
    def _check_keydown_events(self, event):
        #响应按键
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        #创建一组子弹并将其加入编组bullet中
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        #更新子弹的位置并删除消失的子弹
        #更新子弹的位置
        self.bullets.update()
        #删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_keyup_events(self, event):
        # 响应松开
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False



    def _update_screen(self):
        # 更新屏幕上的图像
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)

                #让绘制的屏幕看见
            pygame.display.flip()
#创建游戏实例并运行游戏
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()



