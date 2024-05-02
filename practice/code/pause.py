import sys

import pygame


def Pause(screen, width, height):
    pause_image = pygame.image.load("D:\\pycharm\\project\\snake\\practice\\image\\pause2.png").convert_alpha()
    pause_rect = pause_image.get_rect()
    pause_rect.center = (width // 2, height // 2 - 25)
    screen.blit(pause_image, pause_rect)  # Используйте метод blit с изображением и прямоугольником
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
