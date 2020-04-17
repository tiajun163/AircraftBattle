import sys
import pygame

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    screen=pygame.display.set_mode((1200,800))#创建屏幕大小、
    pygame.display.set_caption("飞机大战")
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        #绘制最近的屏幕可见
        pygame.display.flip()
run_game()