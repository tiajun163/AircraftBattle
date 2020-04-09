import  pygame
class Ship():
    def __init__(self,screen):
        #初始化飞机并设置初始位置
        self.screen=screen
        #使用pygame.image.load()方法加载图片
        self.image=pygame.image.load('images/ship')
        self.screen_rect=screen.get_rect()
        self.rect=screen.image.get_rect()
        
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
    
    
    def blitme( self ):
        self.screen.blit(self.image,self.rect)