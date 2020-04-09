import  pygame
from game_functions import game_function as gf
from  game_functions.settings import Settings
from  game_functions.ship import Ship

def run_game():
    pygame.init()
    ai_settings=Settings()
    scrren=pygame.display.set_mode((ai_settings.screen_height
                                    ,ai_settings.screen_width))
    pygame.display.set_caption("飞机大战")
    ship=Ship(scrren)
    while True:
        gf.check_events()
        pygame.display.flip()
        

run_game()