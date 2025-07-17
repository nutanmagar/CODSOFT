import math

# Display the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Check if the game is over
def check_winner(board):
    # Check rows, columns, diagonals
    lines = board + [list(col) for col in zip(*board)]
    lines += [[board[i][i] for i in range(3)]]
    lines += [[board[i][2 - i] for i in range(3)]]
    
    for line in lines:
        if line.count("X") == 3:
            return "X"
        if line.count("O") == 3:
            return "O"
    
    if all(cell != " " for row in board for cell in row):
        return "Draw"
    
    return None

# Get list of empty cells
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    result = check_winner(board)
    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i, j in get_available_moves(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i, j in get_available_moves(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(best_score, score)
        return best_score

# AI makes a move
def ai_move(board):
    best_score = -math.inf
    move = None
    for i, j in get_available_moves(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            move = (i, j)
    if move:
        board[move[0]][move[1]] = "O"

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Game over! Result: {winner}")
            break

        # AI move
        print("AI is making a move...")
        ai_move(board)
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Game over! Result: {winner}")
            break

# Run the game
if __name__ == "__main__":
    play_game()
