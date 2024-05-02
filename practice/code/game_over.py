import pygame,sys
from colour import Colour

def Game_over(screen,width,height):
    while True:

        screen.fill(Colour.black)
        font_style = pygame.font.SysFont("Miama Nueva", 50)

        text_surface = font_style.render('Game over', False, Colour.game_over)
        text_rect = text_surface.get_rect()
        text_rect.center = (width // 2, height // 2 - 50)
        screen.blit(text_surface, text_rect)

        font_style = pygame.font.SysFont("Miama Nueva", 25)

        text_surface_2 = font_style.render('C - start new game, Q - Quit', False, Colour.massage)
        text_rect_2 = text_surface_2.get_rect()
        text_rect_2.center = (width // 2, height // 2 + 100)
        screen.blit(text_surface_2, text_rect_2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return 1