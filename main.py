import numpy as np
import pygame
from glfw import KEY_F1
from pygame import KEYDOWN

RED = (255,0,0)
BLUE = (0,0,255)
purple = (128,0,128)
def computer_cross_product(x,y):
    a = np.array(x)
    b = np.array(y)
    z = np.cross(a,b)
    return z

computer_cross_product([1,2,3], [1,2,5])

def reconstruct_matrix(u,s,v):
    B_remake = (u @ np.diag(s) @ v)

    return B_remake

def main():
    pygame.init()  # initialize the game
    # CREATING CANVAS
    canvas = pygame.display.set_mode((500, 400))  # define screen size
    # TITLE OF CANVAS
    pygame.display.set_caption("My Board")  # set the title of the window
    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == KEYDOWN:
                if event.key == KEY_F1:
                     canvas.fill((255, 255, 255))
        pygame.draw.line(canvas,RED, (50, 50), (250, 50), 3)
        pygame.draw.polygon(canvas, BLUE, [(100, 300), (200, 150), (300, 0),
                                            (200, 0), (0, 0)], 5)
        pygame.draw.circle(canvas, purple, (250, 200), 5)

        pygame.display.update()
    pygame.quit()  # Quit pygame

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = [
    (-1, -1, 0),  # Bottom-left corner
    (1, -1, 0),  # Bottom-right corner
    (0, 1, 0)  # Top corner
]
# Define the surface (triangle)
surfaces = [
    (0, 1, 2)  # Single triangle using the 3 vertices
]
colors = [
    purple,  # Red
    purple,  # Green
    purple  # Blue
]


def draw_triangle():
    glBegin(GL_TRIANGLES)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv(colors[vertex])  # Assign colors to each vertex
            glVertex3fv(vertices[vertex])
    glEnd()
