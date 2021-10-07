"""
PyOpenGL test
Created by sheepy0125
07/10/2021
"""

#############
### Setup ###
#############
# Import
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

# Setup Pygame
SCREEN_SIZE: tuple = (800, 600)
pygame.display.set_caption("OpenGL test")
window = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

############
### Main ###
############
def main() -> None:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        window.fill("black")
        pygame.display.flip()
        clock.tick(10)


if __name__ == "__main__":
    main()
