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

font = pygame.font.Font(None, 74)

board = [['' for _ in range(grid_size)] for _ in range(grid_size)]
player_turn = 'X'
winner = None
game_over = False

def draw_grid():
    for i in range(1, grid_size):
        pygame.draw.line(screen, line_color, (i * square_size, 0 ), (i * square_size, height) line_width)
        pygame.draw.line(screen, line_color, (0, i * square_size), (width i * square_size) line_width)