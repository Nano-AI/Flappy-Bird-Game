import pygame

class pipe(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.image = pygame.image.load('pipe.png')
        self.image = pygame.transform.smoothscale(self.image, (40, 40))

        self.rect = pygame.image.get_rect()
