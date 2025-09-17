# 1. Name:
#      Braeden
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      displays a sudoku program from a file, allows the user to edit it, and saves to a file when prompted
# 4. What was the hardest part? Be as specific as possible.
#      It took me a bit to figure out how to check the section of the board for valid input.
# 5. How long did it take for you to complete the assignment?
#      Hour and a half
import json
import string


# Reads the board file and returns the multidimensional array.
def read_board():

    filename = input("What is the name of the file? ")
    try:
        data = open(filename, "r")
        text = data.read()
        board = json.loads(text)
        data.close()

    except FileNotFoundError:
        print("Unable to open file", filename)
    return board["board"]


# Saves the board to a file with the user's file name.
def save_board(board):
    data = json.dumps({"board": board})
    filename = input("What would you like to name the file? ")
    file = open(filename, "w")
    file.write(data)
    file.close()


# Displays the board to the user.
def display_board(board):
    print("\nA B C D E F G H I", end="")
    for row in range(0,9):
        print()
        if row == 3 or row == 6:
            print("-----+-----+-----")
        for col in range(0,8):
            if (board[row][col] == 0):
                print(" ", end="")
            else:
                print(board[row][col], end="")
            if (col == 2 or col == 5):
                print("|", end="")
            else:
                print(" ", end="")
    print()

# Converts the user input into a set of coordinates for the board.
def parse_input(space):
    row = 0
    col = 0
    for letter in space:
        if not letter.isdigit():
            col = ord(letter.upper()) - ord("A")
        else:
            row = int(letter) - 1
    return (row, col)

# Checks to see if the number the user inputted is a valid input
def is_input_legal(board, space, number):
    row = space[0]
    col = space[1]
    if (board[row][col] != 0):
        return False
    for box in board[row]:
        if box == number:
            return False
    for box in range(0,8):
        if board[box][col] == number:
            return False
    big_row = row % 3
    big_col = col % 3
    for x_axis in range(big_row * 3, big_row * 3 + 1):
        for y_axis in range(big_col * 3, big_col * 3 + 3):
            if board[x_axis][y_axis] == number:
                return False
    return True

# Accepts user input and edits the board after it has the input validated.
def play_round(board):

    print("Specify a coordinate to edit or enter 'Q' to save and quit")
    answer = input("> ")
    if (answer.upper() == "Q"):
        return False
    else:
        space = parse_input(answer)
        number = int(input(f"What number goes in {answer}? "))
        if (is_input_legal(board, space, number)):
            board[space[0]][space[1]] = number
        else:
            print("That is not a valid space. Try again.")
    return True

# Main.
play = True
board = read_board()
while play:
    display_board(board)
    if not play_round(board):
        save_board(board)
        play = False