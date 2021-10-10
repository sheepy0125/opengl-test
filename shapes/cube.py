"""
Cube shape
Created by sheepy0125
07/10/2021
"""

from OpenGL.GL import *
from shapes.colors import colors


class Cube:
    SIZE: int = 2
    POS_HALF_SIZE: int = SIZE / 2
    NEG_HALF_SIZE: int = POS_HALF_SIZE / -1

    verticies: tuple = (
        (NEG_HALF_SIZE, POS_HALF_SIZE, NEG_HALF_SIZE),  # Front top left       0
        (POS_HALF_SIZE, POS_HALF_SIZE, NEG_HALF_SIZE),  # Front top right      1
        (NEG_HALF_SIZE, NEG_HALF_SIZE, NEG_HALF_SIZE),  # Front bottom left    2
        (POS_HALF_SIZE, NEG_HALF_SIZE, NEG_HALF_SIZE),  # Front bottom right   3
        (NEG_HALF_SIZE, POS_HALF_SIZE, POS_HALF_SIZE),  # Back top left        4
        (POS_HALF_SIZE, POS_HALF_SIZE, POS_HALF_SIZE),  # Back top right       5
        (NEG_HALF_SIZE, NEG_HALF_SIZE, POS_HALF_SIZE),  # Back bottom left     6
        (POS_HALF_SIZE, NEG_HALF_SIZE, POS_HALF_SIZE),  # Back bottom right    7
    )

    cube_edges: tuple = (
        # Front face connections
        (0, 1),
        (2, 3),
        (0, 2),
        (1, 3),
        # Back face connections
        (4, 5),
        (6, 7),
        (4, 6),
        (5, 7),
        # Front to back connections
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7),
    )

    surfaces: tuple = (
        # Front
        (1, 0, 2, 3),
        # Back
        (5, 4, 6, 7),
        # Left
        (2, 0, 4, 6),
        # Right
        (3, 1, 5, 7),
        # Top
        (1, 0, 4, 5),
        # Bottom
        (3, 2, 6, 7),
    )

    @staticmethod
    def render():
        # Surfaces
        glBegin(GL_QUADS)
        for surface in Cube.surfaces:
            color_idx: int = 0
            for vertex_idx in surface:
                vertex: tuple = Cube.verticies[vertex_idx]

                # Change color
                color_idx += 1
                glColor3fv(colors[color_idx])

                glVertex3fv(vertex)
        glEnd()

        # Outlines
        glBegin(GL_LINES)
        for edge in Cube.cube_edges:
            for vertex_idx in edge:
                vertex: tuple = Cube.verticies[vertex_idx]
                glVertex3fv(vertex)
        glEnd()
