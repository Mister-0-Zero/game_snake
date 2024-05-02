class Initialization:
    """ Класс который содержит основные атрибуты для класса food, snake, separation"""
    @classmethod
    def __init__(cls,screen,width,height,size_cell):
        cls.width = width
        cls.height = height
        cls.cell = size_cell
        cls.screen = screen
