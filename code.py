def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = [input("Enter Player 1's name: "), input("Enter Player 2's name: ")]
    symbols = ['X', 'O']
    current_player = 0

    print_board(board)

    for _ in range(9):
        print(f"{players[current_player]}'s turn ({symbols[current_player]})")
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = symbols[current_player]
            print_board(board)

            if check_winner(board):
                print(f"Congratulations {players[current_player]}! You win!")
                return

            current_player = (current_player + 1) % 2
        else:
            print("That position is already taken. Try again.")

    print("It's a draw!")

tic_tac_toe()