import pygame, random, sys
from bird import bird
from pipe import pipe

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

clock = pygame.time.Clock()

background = pygame.image.load('background.png')
background = pygame.transform.smoothscale(background, (width, height))

def main():
    pass

if __name__ == '__main__':
    main()