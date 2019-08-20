import os, sys, pygame, random, array
from pygame.locals import *

# link used https://www.pygame.org/docs/tut/tom_games2.html

# variables

TRAFFIC_COUNT = 45
CENTER_WIDTH = -1
CENTER_HEIGHT = -1

# main method

def main():
    pygame.init()
    # initializing objects
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 24)

    # creating sprite groups
    map_sprite = pygame.sprite.Group()
    player_sprite = pygame.sprite.Group()
    traffic_sprite = pygame.sprite.Group()
    track_sprite = pygame.sprite.Group()
    target_sprite = pygame.sprite.Group()
    pointer_sprite = pygame.sprite.Group()

    # initializing game
    pygame.init()
    screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), 0, 32)

    pygame.display.set_caption("Testing")
    pygame.mouse.set_visible(True)

    CENTER_WIDTH = int(pygame.display.Info().current_w/2)
    CENTER_HEIGHT = int(pygame.display.Info().current_h/2)

    # new background surface
    background = pygame.Surface(screen.get_size())
    # background = background.convert_alpha()

    background.fill((26, 26, 26))




main()

pygame.quit()
sys.exit(0)
