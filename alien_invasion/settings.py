class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕的设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = 230, 230, 230

        # 飞船的设置
        self.ship_speed_factor = 1
        # 外星人的设置
        self.alien_speed_factor = 1

        # 子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人群的设置
        self.fleet_drop_speed = 30
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
        self.ship_limit = 3
