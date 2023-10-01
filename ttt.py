def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")

    for _ in range(9):
        display_board(board)
        print(f"Player {players[current_player]}'s turn")

        while True:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))

            if board[row][col] == " ":
                board[row][col] = players[current_player]
                break
            else:
                print("That position is already taken. Try again.")

        if check_win(board, players[current_player]):
            display_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        current_player = 1 - current_player
    else:
        display_board(board)
        print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
