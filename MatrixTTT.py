from typing import Optional, List, Tuple                    # Typing
import numpy as np                                          # Numerical utilities
from random import randint                                  # Random integers

class Player:
    """Abstract class that encompasses the two possible types of players: human and computer"""
    def __init__(self, symbol: int) -> None:
        """Instantiates an object of the Player class

        Args:
            symbol (str): Number used by the player to fill the matrix. Can be 0 or 1. 
        """
        self.symbol = symbol

class HumanPlayer(Player):
    """Class representing a human player, specialization of the Player class."""
    def __init__(self, symbol: int):
        super().__init__(symbol)
        self.symbol = symbol

    def make_move(self) -> Tuple[int, int]:
        """Allows the human player to make a move on the board

        Returns:
            pos (Tuple[int, int]): Tuple containing the position on the board where the move will be made
        """
        # Move interface
        print(f"Player: {self.symbol}")
        move_input = input("> Position: ")

        # Selects the tuple representing a position on the board according to the player's choice
        if move_input == 'a':
            pos = (0, 0)
        elif move_input == 'b':
            pos = (0, 1)
        elif move_input == 'c':
            pos = (0, 2)
        elif move_input == 'd':
            pos = (1, 0)
        elif move_input == 'e':
            pos = (1, 1)
        elif move_input == 'f':
            pos = (1, 2)
        elif move_input == 'g':
            pos = (2, 0)
        elif move_input == 'h':
            pos = (2, 1)
        else:
            pos = (2, 2)

        return pos

class ComputerPlayer(Player):
    """Class representing a computer player, specialization of the Player class"""
    def __init__(self, symbol : int) -> None:
        super().__init__(symbol)
        self.symbol = symbol

    def make_move(self) -> Tuple[int, int]:
        """Allows the computer to make a move on the board

        Returns:
            Tuple[int, int]: Tuple containing the position on the board where the move will be made
        """
        # Randomly choose a row
        random_row = randint(0, 2)
        # Randomly choose a column
        random_col = randint(0, 2)
        # Generate the "position" tuple
        pos = (random_row, random_col)
        return pos

class Board:
    """Simulates the game board"""
    # Available letters for the board squares
    square_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    def __init__(self) -> None:
        self.squares = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]

    def is_square_empty(self, pos: Tuple[int, int]) -> bool:
        """Checks if a given square on the board is empty

        Args:
            pos (Tuple[int, int]): Tuple containing the board position to be checked

        Returns:
            bool: Boolean indicating if the square is empty (True) or not (False)
        """
        if self.get_board()[pos[0]][pos[1]] not in Board.square_letters:
            return False
        else:
            return True

    def mark_square(self, pos : Tuple[int, int], symbol : str) -> bool:
        """Marks a specific square on the board with the player's symbol

        Args:
            pos (Tuple[int, int]): Position to be marked
            symbol (str): Symbol of the player making the move
        """
        # Marks a square with the player's symbol.
        self.squares[pos[0]][pos[1]] = symbol

    def get_board(self) -> List[List[str]]:
        """Returns the board as a list of lists, with each sub-list being a row of the board

        Ex.:

        [
            [1, 0, 1],
            [1, 0, 0],
            [0, 1, 0]
        ]

        Returns:
            board_list (List[List[str]]): Board in the desired format
        """
        board_list = self.squares
        return board_list

    def print_board(self) -> None:
        """Prints the board on the screen for the player, in an organized way"""
        print(
            f"""

              |      |
          {self.get_board()[0][0]}   |   {self.get_board()[0][1]}  |   {self.get_board()[0][2]}
              |      |
        ---------------------
              |      |
          {self.get_board()[1][0]}   |   {self.get_board()[1][1]}  |   {self.get_board()[1][2]}
              |      |
        ---------------------
              |      |
           {self.get_board()[2][0]}  |   {self.get_board()[2][1]}  |   {self.get_board()[2][2]}
              |      |

            """)

    def is_board_full(self) -> bool:
        """Checks if the board is completely filled, a necessary condition to determine if the game is a draw

        Returns:
            bool: Boolean indicating if the board is completely filled or not (True if yes, False otherwise)
        """
        # Boolean variables to check if each row is filled
        row1_full = not self.is_square_empty((0, 0)) and not self.is_square_empty((0, 1)) and not self.is_square_empty((0, 2))
        row2_full = not self.is_square_empty((1, 0)) and not self.is_square_empty((1, 1)) and not self.is_square_empty((1, 2))
        row3_full = not self.is_square_empty((2, 0)) and not self.is_square_empty((2, 1)) and not self.is_square_empty((2, 2))

        # if the entire board is filled (all variables true), mark the board as full
        if row1_full and row2_full and row3_full:
            return True
        else:
            return False

class MatrixTTT:
    """Main class. Applies all other classes to make the game run."""
    def __init__(self, p1 : Player, p2 : Player) -> None:
        """Instantiates a tic-tac-toe game between two players

        Args:
            p1 (Player): 'Player 1', the first player
            p2 (Player): 'Player 2', the second player
        """
        # list that stores the two players
        self.players = [p1, p2]
        # Board object: the game does not exist without the board
        self.board = Board()
        # variable to mark whose turn it is: 0 if it's player one, 1 if it's player two; -1 is the initial case
        self.turn = -1

    def current_player(self) -> Player:
        """Returns the player who should play now

        Returns:
            Player: "Player" object, who should play now
        """
        if self.turn == -1:
            # At the start of the game, player 1 always goes first
            self.turn = 0
            return self.players[0]
        elif self.turn == 0:
            # if it was player 1's turn, now it's player 2's turn
            self.turn = 1
            return self.players[1]
        else:
            # if it was player 2's turn, now it's player 1's turn
            self.turn = 0
            return self.players[0]

    def play(self) -> None:
        """Simulates the actual game."""
        while True:
            # Select the current player
            curr_player = self.current_player()
            while True:
                # Print the board on the screen
                self.board.print_board()
                # Ask the current player for a move using the Player class (make_move)
                current_move = curr_player.make_move()
                # Mark the move on the board, if the chosen square is empty
                if self.board.is_square_empty(current_move):
                    self.board.mark_square(current_move, curr_player.symbol)
                    break
                # Otherwise (square filled), the user will be notified and must choose another move
                else:
                    print("This square is already filled!")
                    print()

            # If the win conditions for player 1 have been met, announce their victory
            if self.check_game_end() == "p1":
                print("GAME OVER!")
                print(f"VICTORY FOR {self.players[0].symbol}!")
                print()
                self.board.print_board()
                break

            # If the win conditions for player 2 have been met, announce their victory
            elif self.check_game_end() == "p2":
                print("GAME OVER!")
                print(f"VICTORY FOR {self.players[1].symbol}!")
                print()
                self.board.print_board()
                break

    def check_game_end(self) -> Optional[str]:
        """Checks if the game is over, also returning the result if true.

        Returns:
            victory (Optional[str]): Marks the victory or draw of the current game: "p1" or "p2"
        """
        # Variable to mark the result of the game, default "None"
        victory = None

        if self.board.is_board_full() == True:
            board_matrix = np.array(self.board.get_board())
            print(board_matrix)
            if np.linalg.det(board_matrix) == 0:
                victory = "p1"
            else:
                victory = "p2"

        return victory