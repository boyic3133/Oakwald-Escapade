import pygame
#sowad
# import random

pygame.init()

height = 800
width = 600
pygame.display.set_mode((height, width))
# colours
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

close = True

def word(text, size, color, x, y):
    size = pygame.font.SysFont('Arial', size)
    word_2 = size.render(text, True, color)
    end = (word_2, (x, y))
    return end


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


    screen.blit(word('this', 70, BLACK, 0, 0))

main()
