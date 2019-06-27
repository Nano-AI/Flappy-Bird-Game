import pygame, random, sys
from bird import bird
from pipe import pipe

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

background = pygame.image.load('background.png')
background = pygame.transform.smoothscale(background, (width, height))

startPos = (width/8, height/2)
pipes = pygame.sprite.Group
player = bird(startPos)
gapSize = random.randint(200,300)
loopCount = 0
color = (0,0,0)
screen = pygame.display.set_mode(size)

def lose():
    font = pygame.font.SysFont(None, 70)
    text = font.render("You Failed", True, (0,0,255))
    text_rect = text.get_rect()
    text_rect.center = (width/2, height/2)
    while True:
        screen.fill(color)
        screen.blit(text, text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.reset()
                    pipes.empty()
                    return

def main():
    pass

lose()

if __name__ == '__main__':
    main()