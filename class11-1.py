"""
 Pygame 模板程式
 
"""
# 匯入pygame模組
import pygame
from snake import Snake, Food

# 定義一些會用到的顏色
# 常數使用大寫
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

#class SnakeBody(pygame.sprite.Sprite):
#    SIZE = 20
#    def __init__(self, color, x, y):
#        super().__init__()
#        self.image = pygame.Surface([self.SIZE, self.SIZE])
#        self.image.fill(color)
#        self.rect = self.image.get_rect()
#        self.rect.x = x
#        self.rect.y = y
#        
#class snake():
#    def __init__(self, length):
#        self.group = pygame.sprite.Group()
#        self.queue = []
#        self.x = length * SnakeBody.SIZE
#        self.y = 0
#        self.dir = 0
#        self.eatFood = 0
#        for i in range(length):
#            self.x += 20
#            body = SnakeBody(RED, self.x, self.y)
#            
#            self.group.add(body)
#            self.queue.append(body)
#    def move(self):
#        if self.dir == 0:
#            self.x += SnakeBody.SIZE
#            head = SnakeBody(RED, self.x, self.y)
#        elif self.dir == 1:
#            self.y += SnakeBody.SIZE
#            head = SnakeBody(RED, self.x, self.y)
#        elif self.dir == 2:
#            self.x -= SnakeBody.SIZE
#            head = SnakeBody(RED, self.x, self.y)
#        else:
#            self.y -= SnakeBody.SIZE
#            head = SnakeBody(RED, self.x, self.y)
#        
#        self.group.add(head)
#        self.queue.append(head)
#        
#        if self.eatFood > 0:
#            self.eatFood -= 1
#        tail = self.queue.pop(0)  
#        self.group.remove(tail)
#        
#    def changeDir(self, pressed):
#        if not pressed: return
#    def append(self, num):
#        self.eatFood += num
        
        
        

# 初始化pygame
pygame.init()

# 創造一個pygame視窗並設定大小及標題
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("好棒棒遊戲")

# 設定一個開關供迴圈使用
done = False

clock = pygame.time.Clock()

snake = Snake(5)

g = pygame.sprite.Group()
for i in range(10):
    food = Food(WHITE, 300, 300)
    g.add(food)


# -------- 主要的程式迴圈 -----------
while not done:
    # --- 事件迴圈 event loop
    for event in pygame.event.get(): # 從事件list中抓取事件
        if event.type == pygame.QUIT: # 當使用者按下結束
            done = True # 將done變數設為True-->while迴圈將會結束

    # --- 程式的運算與邏輯
    pressed = pygame.key.get_pressed()
    snake.move(pressed)
    
    snake.是否吃到食物(g)
        
    eatFood = pygame.sprite.groupcollide(snake.group, g, False, True)
    if eatFood:
        snake.eatFood += (len(eatFood.values()))
    
    # --- 繪圖的程式碼
    #       先將畫面塗滿底色(將原有畫面清掉)
    #       繪圖的程式要寫在這行後面，不然會被這行清掉
    screen.fill(BLACK)
    
    snake.group.draw(screen)
    g.draw(screen)
    # --- 更新畫面
    pygame.display.flip()

    # --- 每秒鐘60個frame
    clock.tick(10)

# 關閉式窗並離開程式
pygame.quit()


