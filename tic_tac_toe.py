import math
import pygame
import sys
import random

pygame.init()


WIDTH, HEIGHT = 600, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


#define variables
line_width = 12
markers = []
clicked = False
pos = []
player = 1

#define colors
green = (0, 255, 0)
red = (255, 0, 0)


def draw_board():
    bg = (255, 255, 200)
    grid = (50,50,50)
    screen.fill(bg)
    
    CELL_SIZE = WIDTH//3 # 3x3 board, 200px per cell
    for x in range(1,3):
        pygame.draw.line(screen, grid, (0, x*CELL_SIZE), (WIDTH, x*CELL_SIZE), line_width)
        pygame.draw.line(screen, grid, (x*CELL_SIZE, 0), (x*CELL_SIZE, HEIGHT), line_width)


#board = 
#[
#[0,0,0]
#[0,0,0]
#[0,0,0]
#]

for x in range(3):
    row = [0]*3
    markers.append(row)
print(markers)

def drawMarkers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos*200+20, y_pos*200+20), (x_pos*200+180, y_pos*200+180), 8)
                pygame.draw.line(screen, green, (x_pos*200+180, y_pos*200+20), (x_pos*200+20, y_pos*200+180), 8)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos*200+100, y_pos*200+100), 80, 8)
            y_pos += 1
        x_pos += 1
        
def check_winner():
    # check rows
    for row in markers:
        if sum(row) == 3:
            return 1  # player 1 wins
        if sum(row) == -3:
            return -1 # player -1 wins

    # check columns
    for col in range(3):
        col_sum = markers[0][col] + markers[1][col] + markers[2][col]
        if col_sum == 3:
            return 1
        if col_sum == -3:
            return -1

    # check diagonals
    diag1 = markers[0][0] + markers[1][1] + markers[2][2]
    diag2 = markers[0][2] + markers[1][1] + markers[2][0]
    if diag1 == 3 or diag2 == 3:
        return 1
    if diag1 == -3 or diag2 == -3:
        return -1

    # check tie
    tie = True
    for row in markers:
        for cell in row:
            if cell == 0:
                tie = False
    if tie:
        return 0  # tie

    return None  # no winner yet
        
        
def reset_board():
    global markers, player
    for x in range(3):
        for y in range(3):
            markers[x][y] = 0
    player = 1  # reset to player 1

run = True
while run:
    
    draw_board()
    drawMarkers()
    #add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            if markers[cell_x//200][cell_y//200] == 0:
                markers[cell_x//200][cell_y//200] = player
                player = player*-1
        winner = check_winner()
        if winner is not None:
            if winner == 1:
                print("Player X wins!")
            elif winner == -1:
                print("Player O wins!")
            else:
                print("Tie!")
            run = False  # stop game (or reset board)
            pygame.time.delay(2000)  # pause to show result
            reset_board()  # reset for new game
            
            





    pygame.display.update()



pygame.quit()
sys.exit()



