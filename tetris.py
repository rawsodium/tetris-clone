import pygame
import random

# TO-DO
# screen size is 10 x 20 block
# function to draw each of seven (7) Tetrominos
# left arrow - move piece left
# right arrow - move piece right
# up arrow - rotate 90 deg. ccw
# down arrow - rotate 90 deg. cw

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

# constants

# i will make these colors accurate i promise
# blue ricky (J)
blue = (1, 0, 231)
# orange ricky (L)
orange = (229, 164, 57)
# whatever the o thing is (O)
yellow = (241, 240, 79)
# Rhode Island Z (S)
green = (110, 236, 71)
# T (T)
purple = (149, 28, 231)
# Cleveland Z (Z)
red = (222, 47, 33)
# I block (I)
cyan = (110, 236, 238)

# array of colors
colors = [blue, orange, yellow, green, purple, red, cyan]

# shapes
rhode_island_z = [['.....',
                   '.....',
                   '..00.',
                   '.00..',
                   '.....'],
                  ['.....',
                   '..0..',
                   '..00.',
                   '...0.']]

cleveland_z = [['.....',
                '.....',
                '.00..',
                '..00.',
                '.....'],
               ['.....',
                '..0..',
                '.00..',
                '.0...',
                '.....']]

i_block = [['..0..',
            '..0..',
            '..0..',
            '..0..',
            '.....'],
           ['.....',
            '0000.',
            '.....',
            '.....',
            '.....']]

o_block = ['.....',
           '.....',
           '.00..',
           '.00..',
           '.....']

tetris_t = [['.....',
             '..0..',
             '.000.',
             '.....',
             '.....'],
            ['.....',
             '..0..',
             '.00..',
             '..0..',
             '.....'],
            ['.....',
             '.....',
             '.000.',
             '..0..',
             '.....'],
            ['.....',
             '..0..',
             '..00.',
             '..0..',
             '.....']]

# Represents a single tetromino
class Tetromino:
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.rotation = 0
