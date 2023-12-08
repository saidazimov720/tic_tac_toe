import pygame
import sys

pygame.init()

width, height = 600, 600
line_color = (0, 0, 0)
background_color = (255, 255, 255)
line_width = 15
grid_size = 3
square_size = width // grid_size

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")

