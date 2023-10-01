import random

def create_board(rows, cols, num_mines):
    board = [[" " for _ in range(cols)] for _ in range(rows)]
    mines = random.sample(range(rows * cols), num_mines)

    for mine in mines:
        row = mine // cols
        col = mine % cols
        board[row][col] = "M"

    return board

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (4 * len(row) - 1))

def count_adjacent_mines(board, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "M":
            count += 1

    return count

def uncover(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == " ":
        mines = count_adjacent_mines(board, row, col)
        if mines > 0:
            board[row][col] = str(mines)
        else:
            board[row][col] = "0"
            uncover(board, row - 1, col - 1)
            uncover(board, row - 1, col)
            uncover(board, row - 1, col + 1)
            uncover(board, row, col - 1)
            uncover(board, row, col + 1)
            uncover(board, row + 1, col - 1)
            uncover(board, row + 1, col)
            uncover(board, row + 1, col + 1)

def play_minesweeper(rows, cols, num_mines):
    board = create_board(rows, cols, num_mines)
    uncovered = [[" " for _ in range(cols)] for _ in range(rows)]
    game_over = False

    while not game_over:
        print_board(uncovered)
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))

        if (row < 0 or row >= rows) or (col < 0 or col >= cols):
            print("Invalid coordinates. Try again.")
            continue

        if board[row][col] == "M":
            print("Game over! You hit a mine.")
            game_over = True
        else:
            uncover(uncovered, row, col)
            if all(cell != " " for row in uncovered for cell in row):
                print("Congratulations! You win!")
                game_over = True
