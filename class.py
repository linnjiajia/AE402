"""
 Pygame 模板程式
 
"""
# 匯入pygame模組
import pygame

# 定義一些會用到的顏色
# 常數使用大寫
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

# 初始化pygame
pygame.init()

# 創造一個pygame視窗並設定大小及標題
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("好棒棒遊戲")

# 設定一個開關供迴圈使用
done = False

# 創造一個clock控制畫面更新速度
clock = pygame.time.Clock()


player = pygame.image.load("images.jpg")
sound = pygame.mixer.Sound("laser5.ogg")
x = 0
y = 0


# -------- 主要的程式迴圈 -----------
while not done:
    # --- 事件迴圈 event loop
    for event in pygame.event.get(): # 從事件list中抓取事件
        if event.type == pygame.QUIT: # 當使用者按下結束
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            sound.play()

            
        
            
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= 1
    if keys[pygame.K_d]:
        x += 1
            # 將done變數設為True-->while迴圈將會結束
    # --- 繪圖的程式碼
    #       先將畫面塗滿底色(將原有畫面清掉)
    #       繪圖的程式要寫在這行後面，不然會被這行清掉
    
    
    
    screen.fill(BLACK)
    screen.blit(player, [x,y])
        
    # --- 更新畫面
    pygame.display.flip()

    # --- 每秒鐘60個frame
    clock.tick(80)

# 關閉式窗並離開程式
pygame.quit()

