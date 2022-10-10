class TTTBoard:
    """A tic tac toe board
    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X',
        'O's represent moves by player 'O' and '*'s are spots no one has yet
        played on
    """
    def __init__(self):
        self.board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
    def __str__(self):
        output = " ".join(self.board[0]) + "\n" + " ".join(self.board[1]) + "\n" + 
" ".join(self.board[2])
        return output
    def make_move(self, player:str, position:int):
        #print("make_move" , player , position)
        if position < 0:
            return False
        elif position < 3:
            new_position = position
            if self.board[0][new_position] != "*":
                return False
            self.board[0][new_position] = player
            return True
        elif position < 6:
            new_position = position - 3
            #print("new_position" , new_position)
            if self.board[1][new_position] != "*":
                return False
            self.board[1][new_position] = player
            return True
            
        elif position < 9:
            #print("third row move")
            new_position = position - 6
            if self.board[2][new_position] != "*":
                return False
            self.board[2][new_position] = player
            return True
        
        else:
            return False
    def has_won(self, player:str):
        #the case where its in a row
        if self.board[0][0] == player and self.board[0][1] == player and 
self.board[0][2] == player:
            #print("row 1")
            return True
        elif self.board[1][0] == player and self.board[1][1] == player and 
self.board[1][2] == player:
            #print("row 2")
            return True
        elif self.board[2][0] == player and self.board[2][1] == player and 
self.board[2][2] == player:
            #print("row 3")
            return True
        #the case where its a column
        elif self.board[0][0] == player and self.board[1][0] == player and 
self.board[2][0] == player:
            #print("col 1")
            return True
        elif self.board[0][1] == player and self.board[1][1] == player and 
self.board[2][1] == player:
            #print("col 2")
            return True
        elif self.board[0][2] == player and self.board[1][2] == player and 
self.board[2][2] == player:
            #print("col 3")
            return True
        #diagonal case
        elif self.board[0][0] == player and self.board[1][1] == player and 
self.board[2][2] == player:
            #print("diag 1")
            return True
        elif self.board[0][2] == player and self.board[1][1] == player and 
self.board[2][0] == player:
            #print("diag 2")
            return True
        else:
            return False
    def game_over(self):
        #checking for if X or O won or if Full
        if self.has_won("X"):
            #print("X.has_won")
            return True
        elif self.has_won("O"):
            #print("O.has_won")
            return True
        elif self.board[0][0] != "*" and self.board[0][1] != "*" and self.board[0]
[2] != "*" and self.board[1][0] != "*" and self.board[1][1] != "*" and 
self.board[1][2] != "*" and self.board[2][0] != "*" and self.board[2][1] != "*" and
self.board[2][2] != "*":
            #print("full")
            return True
        else:
            return False
    def clear(self):
        self.board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
#print(TTTBoard())
def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""
    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise
        Args:
            maybe_int - string to check if it's an int
        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False
    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0
    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")
        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, "
                "position must be integer between 0 and 8 inclusive"
            )
        if brd.make_move(players[turn], int(move)):
            turn = not turn
    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, that's game!")
if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will
    # DEFINITELY need to write some more tests to make sure that your TTTBoard 
class
    # is behaving properly.
##    brd = TTTBoard()
##    brd.make_move("X", 8)
##    brd.make_move("O", 7)
##    print(brd)
##    assert brd.game_over() == False
##
##    brd.make_move("X", 5)
##    brd.make_move("O", 6)
##    brd.make_move("X", 2)
##
##    assert brd.has_won("X") == True
##    assert brd.has_won("O") == False
##    assert brd.game_over() == True
##
##    brd.clear()
##
##    assert brd.game_over() == False
##
##    brd.make_move("O", 3)
##    brd.make_move("O", 4)
##    brd.make_move("O", 5)
##
##    assert brd.has_won("X") == False
##    assert brd.has_won("O") == True
##    assert brd.game_over() == True
##    brd.make_move("X", 2)
##    brd.make_move("X", 3)
##    brd.make_move("X", 4)
##    brd.make_move("X", 7)
##    brd.make_move("X", 8)
##    brd.make_move("O", 0)
##    brd.make_move("O", 1)
##    brd.make_move("O", 5)
##    brd.make_move("O", 6)
##    print(brd)
##    print(brd.game_over())
##    print("All tests passed!")
##
##    # uncomment to play!
    play_tic_tac_toe()
    pass
