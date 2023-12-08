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
        pygame.draw.line(screen, line_color, (i * square_size, 0), (i * square_size, height), line_width)
        pygame.draw.line(screen, line_color, (0, i * square_size), (width, i * square_size), line_width)

def draw_XO():
    for row in range(grid_size):
        for col in range(grid_size):
            if board[row][col] == 'X':
                pygame.draw.line(screen, line_color, (col * square_size, row * square_size),
                                 ((col + 1) * square_size, (row + 1) * square_size), line_width)
                pygame.draw.line(screen, line_color, ((col + 1) * square_size, row * square_size),
                                 (col * square_size, (row + 1) * square_size), line_width)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, line_color,
                                   (int(col * square_size + square_size / 2), int(row * square_size + square_size / 2)),
                                   int(square_size / 2), line_width)
