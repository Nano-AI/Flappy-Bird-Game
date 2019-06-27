import pygame, random, sys
from bird import bird
from pygame.locals import QUIT
from pipe import pipe

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

background = pygame.image.load('background.png')
background = pygame.transform.smoothscale(background, (width, height))

startPos = (width/8, height/2)
pipes = pygame.sprite.Group()
player = bird(startPos)
gapSize = random.randint(150,250)
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
                    player.reset(startPos)
                    pipes.empty()
                    return

def main():
    global loopCount
    while True:
        gapSize = random.randint(10, 50)
        if loopCount % 90 == 0:
            topPos = random.randint(0, height/2) - 400
            pipes.add(pipe((width + 100, topPos + gapSize + 800)))
            pipes.add(pipe((width + 100, topPos), True))

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.speed[1] = -10

        player.update()
        pipes.update()
        gets_hit = pygame.sprite.spritecollide(player, pipes, False) \
            or player.rect.center[1] > height

        screen.blit(background, [0,0])
        pipes.draw(screen)
        screen.blit(player.image, player.rect)
        pygame.display.flip()
        loopCount += 1

        if gets_hit:
            lose()

if __name__ == '__main__':
    main()