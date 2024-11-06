
# Designing a Tic Tac Toe game in Python can be a fun and straightforward project! Here's a basic breakdown of how you can structure it.

# Step 1: Define the Game Board
# We can represent the Tic Tac Toe board as a 3x3 grid. Using a list of lists will make it easy to reference each cell by its row and column indices.

# Step 2: Create Functions for the Game
# The main components will be:

# Display Board: A function to print the board.
# Player Move: A function to handle player moves and check if a cell is free.
# Check Win: A function to check for a win or a tie.
# Play Game: A function to coordinate game flow, alternating between players and checking for game end conditions.
# Step 3: Implement the Game
# Here’s a basic implementation:

# python
# Copy code
# Step 1: Define the board
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Step 2: Display the board
def display_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

# Step 3: Check for a win or tie
def check_win(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def check_tie(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Step 4: Handle player moves
def player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter col (0, 1, or 2): "))
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("This cell is already occupied. Try again.")
        except (IndexError, ValueError):
            print("Invalid input. Please enter row and column numbers between 0 and 2.")

# Step 5: Game loop
def play_game():
    board = create_board()
    current_player = 'X'

    while True:
        display_board(board)
        player_move(board, current_player)

        if check_win(board):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
# Explanation of the Code
# create_board: Initializes the 3x3 board with empty spaces.
# display_board: Prints the current state of the board after each turn.
# check_win: Checks for winning conditions by checking rows, columns, and diagonals.
# check_tie: Checks if the board is full without any winning conditions.
# player_move: Prompts the player for their move, validates it, and updates the board.
# play_game: Contains the main game loop that alternates turns between players, checks for a win/tie, and switches players.
# This should provide a solid foundation for a simple Tic Tac Toe game in Python!