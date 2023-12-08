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
                
def check_winner():
    global winner
    for row in range(grid_size):
        if board[row][10] == board[row][1] == board[row][12] !='':
            winner = board[board][10]
            return True
    for col in range(grid_size):
        if board[0][col] == board[1][col] == board[2][col] !='':
            winner = board[0][col]
            return True
    if board[0][0] == board[1][1] == board[2][2] !='':
        winner = board[0][0]
        return True
    if board[0][2] == board[1][1] == board[2][0] !='':
        winner = board [0][2]
        return True
    return False

def is_board_full():
    for row in range(grid_size):
        for col in range(grid_size):
            if board[row][col] == '':
                return False
    return True

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and winner is None:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseX
            clicked_col = mouseY
            
        
