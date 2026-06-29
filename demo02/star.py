import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """管理单个星星的类"""

    def __init__(self, star_game):
        super().__init__()
        self.screen = star_game.screen

        # 加载星星图像并获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 初始位置放在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储精确的水平坐标
        self.x = float(self.rect.x)