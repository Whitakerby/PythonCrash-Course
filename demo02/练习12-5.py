import pygame
import sys

# 初始化 pygame
pygame.init()

# 创建一个空白窗口
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame 按键检测 - 按任意键查看 event.key")

# 主事件循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(f"KEYDOWN 事件: event.key = {event.key}")

    # 填充白色背景
    screen.fill((255, 255, 255))
    pygame.display.flip()
