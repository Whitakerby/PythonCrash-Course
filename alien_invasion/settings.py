#存储游戏中的所有类
class Settings:
    def __init__(self):
        #初始化游戏设置
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        #飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3
        #外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction为 1 表示向右移动 -1 左
        self.fleet_direction = 1