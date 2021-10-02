"""
Our Algorithm
1. Pick Empty Square
2. Try all numbers
3. Find one that works
4. Repeat
5. Backtrack
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

def solve(board):
    find = findEmptySquare(board)
    if not find:
        return True
        # Which means we found solution, we're done
    else:
        row, column = find

    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i

            if solve(board):
                return True

            board[row][column] == 0
    return False

def valid(board, number, position):
    # Check row (Soduke Rule)
    """
    We're gonna check through each element of the row
    and we're gonna see if it's equal to the number we
    just added in.
    But if the position we're checking is the position
    we just inserted something into we're not gonna bother
    checking it
    """
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Check Column
    """
    Loops through each column, and check to see if the number 
    is repeated in the column (the number we just inserted)
    """
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check Box
    # Figure out which "box" we're in
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        # multiplying by 3, cause we're getting 0, 1, or 2.
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True

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
                return (i, j)  # return a tuple, (row, colm).
    return None

print("Board Before:")
print_board(board)
print("=============================================")
print("Board After:")
solve(board)
print_board(board)