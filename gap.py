import pygame

class gap(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.screen_info = pygame.display.Info()
        self.size = (self.width, self.height) = (int(self.screen_info.current_w), int(self.screen_info.current_h))
        self.image = pygame.Surface((1, self.height * 2))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(-8, 0)

    def update(self):
        self.rect.move_ip(self.speed)