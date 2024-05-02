from initialization import Initialization
import pygame

class Snake(Initialization):
    orientation = 'up'  # Направление движения головы
    snake_list = []     # Список, содержащий все модули змейки (под индексом 0 находится голова)
    run = False         # Движется ли змейка
    start_image = 0     # От этой "динамической" переменной зависит анимация змейки (ее движения)
    inflections_list = []  # Массив, который хранит координаты перегибов
    speed = 10

    def __init__(self, food):
        """ Инициализация змейки """
        self.head = [pygame.image.load(f'D:/pycharm/project/snake/practice/image/head/snake_head_{direction}.png').convert_alpha() for direction in['up', 'down', 'right', 'left']]
        self.body_1 = [pygame.image.load(f'D:/pycharm/project/snake/practice/image/body_1/snake_body_{direction}_1.png').convert_alpha() for direction in ['up', 'down', 'right', 'left']]
        self.body_2 = [pygame.image.load(f'D:/pycharm/project/snake/practice/image/body_2/snake_body_{direction}_2.png').convert_alpha() for direction in ['up', 'down', 'right', 'left']]
        self.tail = [pygame.image.load(f'D:/pycharm/project/snake/practice/image/tail/snake_tail_{direction}.png').convert_alpha() for direction in['up', 'down', 'right', 'left']]
        self.inflection = [pygame.image.load(f'D:/pycharm/project/snake/practice/image/inflection/snake_inflection_{direction}.png').convert_alpha() for direction in['up_right', 'left_up', 'left_up', 'up_right', 'left_down', 'down_right', 'down_right','left_down']]
        self.tail_inflection = [pygame.image.load(f'D:/pycharm/project/snake/practice/image/tail_inflection/snake_tail_inflection_{direction}.png').convert_alpha()for direction in['down_left', 'down_right', 'right_down', 'left_down', 'right_up', 'left_up', 'up_left', 'up_right']]
        self.snake_list = [
            [(self.width // 2) // self.cell * self.cell, (self.height // 2) // self.cell * self.cell, self.orientation],
            [(self.width // 2) // self.cell * self.cell, (self.height // 2) // self.cell * self.cell + self.cell, self.orientation]
        ]
        self.food = food

    def draw(self):
        """ Отрисовка змейки """
        #print(self.snake_list)
        for id, main_mas in enumerate(self.snake_list):
            x = main_mas[0]
            y = main_mas[1]
            flag = False
            direction_id = self.condition_2(id, 1)
            # отрисовка поворотов
            if id != 0 and direction_id != -1:
                for ind, mas in enumerate(self.inflections_list):
                    if x == mas[0] and y == mas[1]:
                        if mas[2] == len(self.snake_list):
                            self.screen.blit(self.tail_inflection[direction_id - 4], (x, y))
                            self.inflections_list.pop(ind)
                            flag = True
                        else:
                            self.screen.blit(self.tail_inflection[direction_id - 4], (x, y))
                            self.inflections_list[ind][2] += 1

            if not flag:
                direction_id = self.condition_2(id)
                if id == 0:
                    # отрисовка головы
                    self.screen.blit(self.head[direction_id], (x, y))
                elif id + 1 == len(self.snake_list):
                    # отрисовка хвоста
                    self.screen.blit(self.tail[direction_id], (x, y))
                elif self.start_image == 0:
                    if id % 2 == 1:
                        # отрисовка тела
                        self.screen.blit(self.body_1[direction_id], (x, y))
                    else:
                        self.screen.blit(self.body_2[direction_id], (x, y))
                else:
                    if id % 2 == 1:
                        self.screen.blit(self.body_2[direction_id], (x, y))
                    else:
                        self.screen.blit(self.body_1[direction_id], (x, y))
        if self.start_image == 0:
            self.start_image = 1
        else:
            self.start_image = 0

    def change_coord(self, x_change, y_change):
        """ Изменение координат змейки """
        if self.run:
            self.snake_list.insert(0, [self.snake_list[0][0] + x_change, self.snake_list[0][1] + y_change, self.orientation])
            self.snake_list.pop(-1)

    def growth(self):
        """ Рост змейки, добавление новой ячейки """
        if self.food.food_place[0] == self.snake_list[0][:2]:
            retry = 1
            if self.food.gold_apple_per == 1:
                retry = 2
                self.speed -= 1
            for i in range(retry):
                if len(self.snake_list) == 1:
                    x_change, y_change = self.condition()
                else:
                    x_change = self.snake_list[-2][0] - self.snake_list[-1][0]
                    y_change = self.snake_list[-2][1] - self.snake_list[-1][1]

                x = self.snake_list[-1][0] - x_change
                y = self.snake_list[-1][1] - y_change

                self.snake_list.append([x, y, self.snake_list[-1][2]])
            self.food.new_draw()

    def condition(self):
        """ Ищет в какую сторону смотрит змея и передает на сколько изменились координаты головы змеи """
        if self.orientation == 'up':
            return 0, -self.cell
        elif self.orientation == 'down':
            return 0, +self.cell
        elif self.orientation == 'right':
            return self.cell, 0
        else:
            return -self.cell, 0

    def condition_2(self, id_direc, direc_2=0):
        """ Определяет направление змеи """
        mas_res = ['up', 'down', 'right', 'left', 'upleft', 'upright', 'leftdown', 'rightdown', 'leftup', 'rightup', 'downleft', 'downright']
        if direc_2:
            res = self.snake_list[id_direc][2] + self.snake_list[id_direc - 1][2]
        else:
            res = self.snake_list[id_direc][2]
        try:
            output = mas_res.index(res)
        except:
            output = -1
        return output
