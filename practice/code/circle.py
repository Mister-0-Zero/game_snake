import pygame, sys
from pause import Pause
def Circle(snake):
    """ Один из основных циклов программы отвечающий за поимку событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            if not snake.run:
                snake.run = True
                if event.key == pygame.K_w:
                    break
            if event.key == pygame.K_SPACE:
                Pause(snake.screen,snake.width,snake.height)
                break
            snake.inflections_list.append([snake.snake_list[0][0],snake.snake_list[0][1],2])
            if event.key == pygame.K_w and snake.orientation != 'down':
                snake.orientation = 'up'
                break
            if event.key == pygame.K_d and snake.orientation != 'left':
                snake.orientation = 'right'
                break
            if event.key == pygame.K_a and snake.orientation != 'right':
                snake.orientation = 'left'
                break
            if event.key == pygame.K_s and snake.orientation != 'up':
                snake.orientation = 'down'
                break
