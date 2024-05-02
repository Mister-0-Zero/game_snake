import pygame
from colour import Colour
from initialization import Initialization

class Separation(Initialization):
    """Рисует сетку"""

    def __init__(self):
        self.kol_line_x = self.width// self.cell + 1
        self.kol_line_y = self.height// self.cell + 1

    def draw(self):
        for x in range(self.kol_line_x):
            pygame.draw.line(self.screen, Colour.line, (x * self.cell, 0), (x * self.cell, self.height), 1)
        for y in range(self.kol_line_y):
            pygame.draw.line(self.screen, Colour.line, (0, y * self.cell), (self.width, y * self.cell), 1)



