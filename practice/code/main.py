import pygame
import sys
from circle import Circle
from colour import Colour
from score import Score
from check_game_over import Check_game_over
from initialization import Initialization
from food import Food
from separation import Separation
from snake import Snake
from menu import Menu


def Main():
    """ Основная функция программы """
    __version__ = '1.1'

    pygame.init()
    width, height, size_cell = 704, 512, 16
    game_over = False

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake 1.0')

    icon = pygame.image.load('D:/pycharm/project/snake/practice/image/icon.png').convert_alpha()
    pygame.display.set_icon(icon)



    """ Инициализация основных объектов """
    Initialization(screen, width, height, size_cell)
    food = Food()
    snake = Snake(food)
    food.snake = snake
    food.new_coord()
    separation = Separation()
    score = Score(screen, height)
    clock = pygame.time.Clock()

    Menu(screen)


    screen.fill(Colour.background[0])
    screen.fill(Colour.background[0])
    separation.draw()
    snake.draw()
    score.draw()
    food.draw()
    pygame.display.update()

    while not game_over:
        """ Основной цикл программы """
        Circle(snake)
        x_change, y_change = snake.condition()
        game_over = Check_game_over(snake, x_change, y_change)
        snake.change_coord(x_change, y_change)
        snake.growth()

        screen.fill(Colour.background[0])
        separation.draw()
        snake.draw()
        score.draw()
        food.draw()

        pygame.display.update()

        snake.speed += 0.005
        clock.tick(snake.speed)

        if game_over == 2:
            Main()
        if game_over:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    Main()
else:
    print("Это не основной файл, запустите основной")
