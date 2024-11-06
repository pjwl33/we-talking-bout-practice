# Game Components:

# Board: The game grid where tetrominoes fall.
# Tetrominoes: Different shapes (I, O, T, S, Z, J, L) that fall down the board.
# Game Logic: Handling movement, rotations, line clearing, and collision detection.
# Input Handling: Using arrow keys to control the falling tetromino.

import random
import curses

# Define game dimensions
WIDTH = 10
HEIGHT = 20

# Shapes
SHAPES = [
    [[1, 1, 1, 1]],          # I
    [[1, 1], [1, 1]],        # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
]

# Rotation function
def rotate(shape):
    return [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0]) - 1, -1, -1)]

# Game class
class Tetris:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.board = [[0] * WIDTH for _ in range(HEIGHT)]
        self.current_piece = random.choice(SHAPES)
        self.piece_x, self.piece_y = WIDTH // 2 - len(self.current_piece[0]) // 2, 0
        self.next_piece = random.choice(SHAPES)
        self.score = 0
        self.stdscr.nodelay(True)
        curses.curs_set(0)

    def draw_board(self):
        self.stdscr.clear()
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    self.stdscr.addstr(y, x * 2, "[]")
        
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.stdscr.addstr(self.piece_y + y, (self.piece_x + x) * 2, "[]")

        self.stdscr.addstr(0, WIDTH * 2 + 3, f"Score: {self.score}")
        self.stdscr.refresh()

    def check_collision(self, dx, dy, rotated_piece=None):
        shape = rotated_piece or self.current_piece
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.piece_x + x + dx
                    new_y = self.piece_y + y + dy
                    if new_x < 0 or new_x >= WIDTH or new_y >= HEIGHT:
                        return True
                    if self.board[new_y][new_x]:
                        return True
        return False

    def merge_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.piece_y + y][self.piece_x + x] = cell
        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = random.choice(SHAPES)
        self.piece_x, self.piece_y = WIDTH // 2 - len(self.current_piece[0]) // 2, 0
        if self.check_collision(0, 0):
            self.game_over()

    def clear_lines(self):
        lines_cleared = 0
        new_board = []
        for row in self.board:
            if all(row):
                lines_cleared += 1
            else:
                new_board.append(row)
        self.board = [[0] * WIDTH] * lines_cleared + new_board
        self.score += lines_cleared ** 2

    def game_over(self):
        self.stdscr.clear()
        self.stdscr.addstr(HEIGHT // 2, WIDTH - 4, "Game Over")
        self.stdscr.addstr(HEIGHT // 2 + 1, WIDTH - 7, f"Your Score: {self.score}")
        self.stdscr.refresh()
        curses.napms(2000)
        curses.endwin()
        exit()

    def run(self):
        key = -1
        while True:
            self.draw_board()
            key = self.stdscr.getch()

            if key == curses.KEY_LEFT and not self.check_collision(-1, 0):
                self.piece_x -= 1
            elif key == curses.KEY_RIGHT and not self.check_collision(1, 0):
                self.piece_x += 1
            elif key == curses.KEY_DOWN and not self.check_collision(0, 1):
                self.piece_y += 1
            elif key == curses.KEY_UP:
                rotated_piece = rotate(self.current_piece)
                if not self.check_collision(0, 0, rotated_piece):
                    self.current_piece = rotated_piece

            if not self.check_collision(0, 1):
                self.piece_y += 1
            else:
                self.merge_piece()

            self.draw_board()
            curses.napms(200)

# Main function to initialize curses and run the game
def main(stdscr):
    game = Tetris(stdscr)
    game.run()

# Start the game
curses.wrapper(main)


# How the Code Works
# Grid and Shapes: The Tetris class sets up the game board and randomly generates tetromino shapes using the SHAPES list.
# Piece Movement and Rotation: The check_collision method checks if the piece can move or rotate based on its surroundings.
# Line Clearing: The clear_lines method removes completed lines and updates the score.
# Game Loop: In run, the game loop captures key presses to control the piece and moves it down every tick until it lands.
# Game Over: When a new piece collides immediately, the game ends.
# Controls
# Arrow Keys: Move the tetromino left, right, and down.
# Up Arrow: Rotate the tetromino.
# This simple implementation will run in a terminal and should give you a basic Tetris experience! You can expand this by adding additional features like a preview of the next piece, increasing difficulty, or different scoring methods.