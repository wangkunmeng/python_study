import pygame


class Ship:

    def __init___(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载飞船头像并设置其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将没搜新飞船放在屏幕底部中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)