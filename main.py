"""
Our Algorithm
1. Pick Empty Square
2. Try all numbers
3. Find one that works
4. Repeat
5. Backtracks
"""
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def print_board(board):

    for i in range(len(board)):
        # Everytime we're on 3rd row (except first row), we're going to print horizontal line
        if i % 3 == 0 and i != 0:
            print("------------------------")

        # For each position in the row, if it's the 3rd element, (multiple of 3), and draw the vertical line
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                # The " end="" " means it doesn't print a "\n" so we don't go to next line, when printing out each row
            if j == 8:
                print(board[i][j])
                # just prints the numbers on the 8th row. (So no, " | " is placed )
            else:
                print(str(board[i][j]) + " ", end="")
                # Before printing the numbers, we want some spaces between them, so that's why the ' + " " '

def findEmptySquare(board):
    """
    Just wanna return position of that empty square to try
    different numbers on that square
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j) # return a tuple, (row, colm).

