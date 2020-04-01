import  sys#导入sys包
import  pygame#导入pygame包

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()#初始化背景设置
    #调用pygame.display.set_mode()方法创建一个screen窗口
    screen=pygame.display.set_mode((800,800))
    pygame.display.set_caption('Alien Invasion')
    bg_color=(230,238,230)#设置屏幕 颜色
    #开始游戏的主循环
    while True:
         #监视键盘和鼠标事件
        for event in pygame.event.get():#使用pygame.event.get()方法，检查pygame访问事件
            #检测到退出 使用pgame.QUIT()和sys.exit()方法退出游戏
            if event.type==pygame.QUIT:
                sys.exit()#退出游戏
            screen.fill(bg_color)#调用屏幕颜色
            #让最近绘制的屏幕可见
            pygame.display.flip()
#初始化游戏并开始游戏
run_game()