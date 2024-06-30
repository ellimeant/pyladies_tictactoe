import random
start_board = "--------------------"
player_user = "x"
player_computer = "o"


def printboard(board):
    print(board)

printboard(start_board) # checks that the board is working

def user_board(board):
    while True:
        mark = player_user
        position = int(input("Which position do you want to play? Choose a number from 0-19! "))
        if position > 19 or board[position] != "-" : # this is a negative positive to get the expected return, see computer move
            print("This is no valid position. Try again.")
        else:
            return position

def computer_board(board):
    position = random.randrange(19) #mistake in the move-file that you need to add random. for this to work
    if board[position] == "-":
        return position


def update_board(board, position, mark):
    return board[:position] + mark + board[position+1:]

while "-" in start_board:
    user_move = user_board(start_board)
    start_board = update_board(start_board, user_move, player_user)
    print(f"Here's the new board: {start_board}")
    computer_move = computer_board(start_board)
    start_board = update_board(start_board, computer_move, player_computer)
    print(f"The computer played. The new board is {start_board}.")
    if "-" not in start_board:
        print("Game over.")
        break
    
     