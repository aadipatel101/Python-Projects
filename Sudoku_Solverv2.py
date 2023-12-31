def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def is_valid(board, row, col, num):
    # Check if the number is not present in the current row and column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False
    
    # Check if the number is not present in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    # Find the first empty cell (cell with 0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    # Find an empty location
    empty_location = find_empty_location(board)

    # If there is no empty location, the Sudoku is solved
    if not empty_location:
        return True

    row, col = empty_location

    # Try placing a number from 1 to 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # If placing the number is valid, try to solve the remaining Sudoku
            board[row][col] = num
            if solve_sudoku(board):
                return True

            # If placing the number leads to an invalid solution, backtrack
            board[row][col] = 0

    # No valid number was found, backtrack
    return False

# Example Sudoku board (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    print("Sudoku Solved:")
    print_board(sudoku_board)
else:
    print("No solution exists.")
