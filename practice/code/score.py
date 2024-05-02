import pygame
from colour import Colour

class Score:
    """ Класс, который ведет счет длины змеи и выводит этот счет на экран """
    @classmethod
    def __init__(cls,screen,height):
        cls.screen = screen
        cls.height = height
        cls.score = 0
    
    @classmethod
    def draw(cls):
        font_style = pygame.font.SysFont("Grafita", 30)
        text_surface = font_style.render(f'Your score: {cls.score}', False, Colour.score)
        cls.screen.blit(text_surface, [0,0])

    @classmethod
    def add(cls,num = 1):
        cls.score += num