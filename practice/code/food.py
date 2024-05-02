import pygame
from random import randint
from score import Score
from initialization import Initialization

class Food(Initialization):
    """ Класс для обработки еды в игре"""

    food_place = [[0, 0]]  # координаты еды [0,0] - это костыль
    rand_num = 1 # содержит случайное число, которое меняется, и от него зависит какая еда будет рисоваться
    gold_apple_per = 0 # переменная, которая следит за состоянием золотого яблока 1 - успешно съедено, 0 - другое
    index_gold_apple = 0 # сожержит какой по счету рисунок золотого яблока (от 1 до 15) должен быть
    snake = None

    def __init__(self):
        self.red_apple = pygame.image.load("D:/pycharm/project/snake/practice/image/food/red_apple.png")
        self.gold_apple = [pygame.image.load(f"D:/pycharm/project/snake/practice/image/food/gold_apple/gold_apple{i}.png") for i in range(1, 17)]

    def new_draw(self):
        """ Создание нового лакомства и прибавление счета """
        if self.rand_num:
            Score.add(1)
        elif self.gold_apple:
            Score.add(2)

        self.rand_num = randint(0, 9) # 0 - золотое яблоко
        self.gold_apple_per = 1 if self.rand_num == 0 else 0
        self.index_gold_apple = 0
        self.new_coord()

        if self.rand_num:
            self.screen.blit(self.red_apple, (self.food_place[0][0], self.food_place[0][1]))
        else:
            self.screen.blit(self.gold_apple[0], (self.food_place[0][0], self.food_place[0][1]))


    def draw(self):
        """ Отрисовка еды """
        if self.rand_num:
            self.screen.blit(self.red_apple, (self.food_place[0][0], self.food_place[0][1]))
        elif self.index_gold_apple < 15.6:
            self.index_gold_apple += 0.4
            self.screen.blit(self.gold_apple[int(self.index_gold_apple)], (self.food_place[0][0], self.food_place[0][1]))
        else:
            self.index_gold_apple = 0
            self.gold_apple_per = 0
            self.new_draw()

    def new_coord(self):
        """ Задает координаты новой еды """
        while True:
            x = randint(0, self.width // self.cell - 1) * self.cell
            y = randint(0, self.height // self.cell - 1) * self.cell
            flag = 1
            for massive_coord in self.snake.snake_list:
                if [x,y] == massive_coord[:2]:
                    flag = 0
                    break
            if flag:
                break
        self.food_place[0] = [x, y]
