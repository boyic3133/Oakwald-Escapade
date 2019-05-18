import pygame

# import random

pygame.init()

height = 800
width = 600
pygame.display.set_mode((height, width))
# colours
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

close = True


def main():
    while close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()


main()
