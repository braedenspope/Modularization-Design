# 1. Name:
#      Braeden Pope
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was getting the game to exit the loop when I quit the game, while
#      also looping more than just once. I eventually got it thanks to the hint in the
#      template comments. I forgot about using the function returns as boolean values.
# 5. How long did it take for you to complete the assignment?
#      2 and a half hours

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    try:
        data = open(filename, "r")
        text = data.read()

    except FileNotFoundError:
        print(f"Unable to open file {filename}.")
        return blank_board["board"];

    list = json.loads(text)
    return list["board"]

def save_board(filename, board):
    '''Save the current game to a file.'''
    # Put file writing code here.
    with open(filename, 'w') as file_write:
        new_board = {"board": board}
        json_board = json.dumps(new_board)
        file_write.write(json.dumps(new_board))
        file_write.close()

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Put display code here.
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    # Put code here determining if it is X's turn.
    x_spaces = 0
    o_spaces = 0
    for item in board:
        if (item == X):
            x_spaces += 1
        elif (item == O):
            o_spaces += 1
    if (x_spaces <= o_spaces):
        return True
    else:
        return False

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.
    if (is_x_turn(board)):
        spot = input("X> ")
    else:
        spot = input("O> ")
    if (spot == "q"):
        save_board("board.json",board)
        return False
        
    elif (board[int(spot)-1] == BLANK):
        spot = int(spot) - 1
        if (is_x_turn(board)):
            board[spot] = X
        else:
            board[int(spot)] = O
        display_board(board)
        if(game_done(board, True)):
            return True
    else:
        print("That spot is currently filled.")
    return True


def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# The file read code, game loop code, and file close code goes here.
board = read_board("board.json")
display_board(board)
play = True
while (game_done(board, False) == False and play):
    play = play_game(board)
if (game_done(board, False) == True):
    save_board("board.json", blank_board["board"])