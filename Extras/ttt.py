#!/usr/bin/env python3
import platform
import sys
import time
import os
from math import inf as infinity
from os import system
from random import choice

import pygame as pg
from pygame.locals import *

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
License: GNU GENERAL PUBLIC LICENSE (GPL)
"""

HUMAN = -1
COMP = +1
# setting up a 3 * 3 board in canvas
board = [[0] * 3, [0] * 3, [0] * 3]

# declaring the global variables

# for storing the 'x' or 'o'
# value as character
XO = "X"

# storing the winner's value at
# any instant of code
winner = None

# to check if the game is a draw
draw = False

# to set width of the game window
width = 400

# to set height of the game window
height = 400

# to set background color of the
# game window
white = (255, 255, 255)

# color of the straightlines on that
# white game board, dividing board
# into 9 parts
line_color = (0, 0, 0)

# initializing the pygame window
pg.init()

# setting fps manually
fps = 30

# this is used to track time
CLOCK = pg.time.Clock()

# this method is used to build the
# infrastructure of the display
screen = pg.display.set_mode((width, height + 100), 0, 32)

# setting up a nametag for the
# game window
pg.display.set_caption("Tic Tac Toe")

# loading the images as python object
bundle_dir = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
bundle_dir2 = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
bundle_dir3 = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))

# loading the images
path_to_opening = os.path.abspath(os.path.join(bundle_dir, "tic tac opening.png"))
opening = pg.image.load(path_to_opening)
path_to_x = os.path.abspath(os.path.join(bundle_dir2, "x.png"))
x_img = pg.image.load(path_to_x)
path_to_o = os.path.abspath(os.path.join(bundle_dir3, "o.png"))
o_img = pg.image.load(path_to_o)

# resizing images
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))
opening = pg.transform.scale(opening, (width, height + 100))


def game_initiating_window():

    # displaying over the screen
    screen.blit(opening, (0, 0))

    # updating the display
    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    # drawing vertical lines
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

    # drawing horizontal lines
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    draw_status()


def draw_status():

    # getting the global variable draw
    # into action
    global draw, XO

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " Won !"
    if draw:
        message = "Game Draw !"

    # setting a font object
    font = pg.font.Font(None, 30)

    # setting the font properties like
    # color and width of the text
    text = font.render(message, 1, (255, 255, 255))

    # copy the rendered message onto the board
    # creating a small block at the bottom of the main display
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()


def user_click():
    # get coordinates of mouse click
    x, y = pg.mouse.get_pos()

    # get column of mouse click (1-3)
    if x < width / 3:
        col = 1

    elif x < width / 3 * 2:
        col = 2

    elif x < width:
        col = 3

    else:
        col = None

    # get row of mouse click (1-3)
    if y < height / 3:
        row = 1

    elif y < height / 3 * 2:
        row = 2

    elif y < height:
        row = 3

    else:
        row = None

    # after getting the row and col,
    # we need to draw the images at
    # the desired positions
    if row and col and board[row - 1][col - 1] is None:
        global XO
        drawXO(row, col)
        can_move = set_move(row - 1, col - 1, HUMAN)
        check_win()


def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    XO = "X"
    draw = False
    game_initiating_window()
    winner = None
    board = [[0] * 3, [0] * 3, [0] * 3]


def check_win():
    global board, winner, draw

    # checking for winning rows
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2]) and (
            board[row][0] is not None
        ):
            winner = board[row][0]
            pg.draw.line(
                screen,
                (250, 0, 0),
                (0, (row + 1) * height / 3 - height / 6),
                (width, (row + 1) * height / 3 - height / 6),
                4,
            )
            break

    # checking for winning columns
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and (
            board[0][col] is not None
        ):
            winner = board[0][col]
            pg.draw.line(
                screen,
                (250, 0, 0),
                ((col + 1) * width / 3 - width / 6, 0),
                ((col + 1) * width / 3 - width / 6, height),
                4,
            )
            break

    # check for diagonal winners
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):

        # game won diagonally left to right
        winner = board[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):

        # game won diagonally right to left
        winner = board[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)

    if all([all(row) for row in board]) and winner is None:
        draw = True
    draw_status()


def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if "windows" in os_name:
        system("cls")
    else:
        system("clear")


def render(state, c_choice, h_choice):
    """
    Print the board on console
    :param state: current state of the board
    """

    chars = {-1: h_choice, +1: c_choice, 0: " "}
    str_line = "---------------"

    print("\n" + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f"| {symbol} |", end="")
        print("\n" + str_line)


def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    XO = "O"
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f"Computer turn [{c_choice}]")
    render(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)


def drawXO(row, col):
    global board, XO

    # for the first row, the image
    # should be pasted at a x coordinate
    # of 30 from the left margin
    if row == 1:
        posx = 30

    # for the second row, the image
    # should be pasted at a x coordinate
    # of 30 from the game line
    if row == 2:

        # margin or width / 3 + 30 from
        # the left margin of the window
        posx = width / 3 + 30

    if row == 3:
        posx = width / 3 * 2 + 30

    if col == 1:
        posy = 30

    if col == 2:
        posy = height / 3 + 30

    if col == 3:
        posy = height / 3 * 2 + 30

    # setting up the required board
    # value to display
    board[row - 1][col - 1] = XO

    if XO == "X":

        # pasting x_img over the screen
        # at a coordinate position of
        # (pos_y, posx) defined in the
        # above code
        screen.blit(x_img, (posy, posx))
        XO = "O"

    else:
        screen.blit(o_img, (posy, posx))
        XO = "X"
    pg.display.update()


h_choice = "X"
c_choice = "O"

# Main loop of this game

game_initiating_window()

while empty_cells(board) != 0:
    print(1)
    for event in pg.event.get():
        print(event)
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            print(3)
            user_click()
            check_win()
            ai_turn(c_choice, h_choice)
            check_win()
            if winner or draw:
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)
