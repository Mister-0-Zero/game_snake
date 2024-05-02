import pygame
import sys
from colour import Colour

def Menu(screen):
    """Отображает главное меню и обрабатывает события мыши и клавиатуры."""

    screen.fill(Colour.menu)

    menu = pygame.image.load('D:/pycharm/project/snake/practice/image/menu/menu.png')
    controls = pygame.image.load('D:/pycharm/project/snake/practice/image/menu/controls.png')

    button_start = pygame.Rect(164, 305, 383, 74)
    button_controls = pygame.Rect(163, 406, 383, 74)
    button_back = pygame.Rect(198, 402, 272, 55)

    screen.blit(menu, (0, 0))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_start.collidepoint(mouse_pos):
                    return True
                if button_controls.collidepoint(mouse_pos):
                    show_controls(screen, controls, button_back)
                    screen.blit(menu, (0, 0))
                    pygame.display.update()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    return True

def show_controls(screen, controls, button_back):
    """Отображает экран с инструкциями управления и обрабатывает события мыши для выхода."""

    flag = True

    screen.blit(controls, (0, 0))
    pygame.display.update()
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_back.collidepoint(mouse_pos):
                    flag = False

