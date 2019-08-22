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
def rotate_center(image, rect, angle):
        """rotate an image while keeping its center"""
        rotate_image = pygame.transform.rotate(image, angle)
        rotate_rect = rotate_image.get_rect(center=rect.center)
        return rotate_image, rotate_rect

# finding spawn
def find_spawn():
    x = randint(0, 9)
    y = randint(0, 9)
    while maps.map_1[y][x] == 5:
            x = randint(0, 9)
            y = randint(0, 9)
    return x * 1000 + CENTER_X, y * 1000 + CENTER_Y

# define car as Player.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('car_player.png')
        self.rect = self.image.get_rect()
        self.image_orig = self.image
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        CENTER_X =  int(pygame.display.Info().current_w /2)
        CENTER_Y =  int(pygame.display.Info().current_h /2)
        self.x = CENTER_X
        self.y = CENTER_Y
        self.rect.topleft = self.x, self.y
        self.x, self.y = find_spawn()
        self.dir = 0
        self.speed = 0.0
        self.maxspeed = 11.5
        self.minspeed = -1.85
        self.acceleration = 0.095
        self.deacceleration = 0.12
        self.softening = 0.04
        self.steering = 1.60
        self.tracks = False

    # Reset the car. takes in the car/player object
    def reset(self):
        self.x =  int(pygame.display.Info().current_w /2)
        self.y =  int(pygame.display.Info().current_h /2)
        self.speed = 0.0 # resets speed
        self.dir = 0 # resets direction
        self.image, self.rect = rotate_center(self.image_orig, self.rect, self.dir)
        self.rect.topleft = self.x, self.y
        self.x, self.y = find_spawn()

    # Emit tracks..
    def emit_tracks(self):
        self.tracks = True

    # Don't emit tracks..
    def reset_tracks(self):
        self.tracks = False
