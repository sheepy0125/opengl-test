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
from shapes.cube import Cube

# Setup Pygame
SCREEN_SIZE: tuple = (800, 600)
pygame.display.set_caption("OpenGL test")
window = pygame.display.set_mode(SCREEN_SIZE, pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

# Globals
FPS: int = 30
FOV: int = 45
ASPECT_RATIO: int = SCREEN_SIZE[0] / SCREEN_SIZE[1]
RENDER_DISTANCE_CLIP_PLANE: tuple = (0.1, 50.0)
ROTATE_BY_ANGLE: int = 1
ROTATE_BY_COORDS: tuple = (3, 1, 1)

##############
### Shapes ###
##############


############
### Main ###
############
def main() -> None:
    gluPerspective(
        FOV,
        ASPECT_RATIO,
        *RENDER_DISTANCE_CLIP_PLANE,
    )

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # like window.fill()
        glRotatef(ROTATE_BY_ANGLE, *ROTATE_BY_COORDS)
        Cube.render()
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
