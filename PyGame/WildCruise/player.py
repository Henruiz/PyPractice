# this is the class player file for spawning the player

# Player module, the car.
import os, sys, pygame, math, maps
from pygame.locals import *
from random import randint
from loader import load_image

GRASS_SPEED = 0.715
GRASS_GREEN = 75
CENTER_X = -1
CENTER_Y = -1


# Rotate car.
def rot_center(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image, rot_rect
# finding spawn
def findspawn():
    x = randint(0, 9)
    y = randint(0, 9)
    while maps.map_1[y][x] == 5:
            x = randint(0, 9)
            y = randint(0, 9)
    return x * 1000 + CENTER_X, y * 1000 + CENTER_Y
