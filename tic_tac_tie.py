import random

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board):
    # Check all possible winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]  # returns the winning player (X or O)
    
    if " " not in board:
        return "Tie"
    
    return None

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def computer_move(board):
    # Simple AI: first checks for winning move, then blocks player, then random
    empty_spots = [i for i, spot in enumerate(board) if spot == " "]
    
    # Check for winning move
    for spot in empty_spots:
        board_copy = board.copy()
        board_copy[spot] = "O"
        if check_winner(board_copy) == "O":
            return spot
    
    # Block player's winning move
    for spot in empty_spots:
        board_copy = board.copy()
        board_copy[spot] = "X"
        if check_winner(board_copy) == "X":
            return spot
    
    # Choose center if available
    if 4 in empty_spots:
        return 4
    
    # Choose a corner if available
    corners = [0, 2, 6, 8]
    available_corners = [c for c in corners if c in empty_spots]
    if available_corners:
        return random.choice(available_corners)
    
    # Choose a random spot
    return random.choice(empty_spots)

def play_game():
    board = [" "] * 9
    current_player = "X"  # Player is X, computer is O
    
    print("Welcome to Tic-Tac-Toe!")
    print("Enter numbers 1-9 to make your move:")
    print_board(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    
    while True:
        if current_player == "X":
            move = player_move(board)
            board[move] = "X"
        else:
            print("Computer's turn...")
            move = computer_move(board)
            board[move] = "O"
            print(f"Computer chooses position {move + 1}")
        
        print_board(board)
        result = check_winner(board)
        
        if result:
            if result == "Tie":
                print("It's a tie!")
            elif result == "X":
                print("Congratulations! You win!")
            else:
                print("Computer wins!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break