import sys
import random
import pygame
from settings import Settings
from star import Star


class StarsGame:
    """管理游戏资源和主循环的类"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # 初始化游戏窗口
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("随机星空")

        # 创建星星编组
        self.stars = pygame.sprite.Group()
        self._create_stars()

    def _create_stars(self):
        """创建铺满屏幕的带随机偏移的星星网格"""
        # 用单颗星星获取基准尺寸
        star = Star(self)
        star_width, star_height = star.rect.size

        # 计算单行可容纳的星星数量
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # 计算可容纳的星星行数
        available_space_y = self.settings.screen_height - (2 * star_height)
        number_rows = available_space_y // (2 * star_height)

        # 双层循环：逐行逐列生成星星
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """创建单个星星，在网格坐标基础上叠加随机偏移"""
        star = Star(self)
        star_width, star_height = star.rect.size

        # 网格基准坐标
        base_x = star_width + 2 * star_width * star_number
        base_y = star_height + 2 * star_height * row_number

        # 随机偏移：范围 ±半个星星尺寸，保证整体整齐又自然错落
        offset_x = random.randint(-star_width // 2, star_width // 2)
        offset_y = random.randint(-star_height // 2, star_height // 2)

        # 应用最终坐标
        star.x = base_x + offset_x
        star.rect.x = star.x
        star.rect.y = base_y + offset_y

        self.stars.add(star)

    def _check_events(self):
        """响应退出事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """刷新屏幕画面"""
        self.screen.fill((0, 0, 0))  # 黑色背景模拟夜空
        self.stars.draw(self.screen)
        pygame.display.flip()

    def run_game(self):
        """启动游戏主循环"""
        while True:
            self._check_events()
            self._update_screen()


if __name__ == '__main__':
    sg = StarsGame()
    sg.run_game()