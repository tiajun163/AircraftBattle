import pygame
''''加载图片'''
class Ship():
    def __init__(self,screen):
        #初始化飞机并设置其初始位置
        self.screen=screen
        #加载飞机图片并获取外接矩形
        self.image=pygame.image.load('images/ship.bmp')#使用了pygame.image.load()加载图片
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        
        #将每艘飞机放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx#放在中央位置
        self.rect.bottom=self.screen_rect.bottom#放在底部
    def blitme( self ):
        """在指定的位置绘制飞机"""
        self.screen.blit(self.image,self.rect)