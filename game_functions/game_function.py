import sys
import  pygame
from  game_functions.settings import Settings
def check_events():
    #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT():
            sys.exit()
def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings)
    ship.blitme()