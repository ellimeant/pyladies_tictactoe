start_board = "--------------------"
player_user = "x"
player_computer = "o"
game_is_player = True

def printboard(board):
    print(board)

printboard(start_board) # checks that the board is working

def move(board):
     mark = player_user
     position = int(input("Which position do you want to play? Choose a number from 0-19! "))
     placing = board[position]
     print(board[:position] + mark + board[position+1:])

def update_board(board, mark, position):
    mark = player_user
    position = int(input("Which position do you want to play? Choose a number from 0-19! "))
    return board[:position] + mark + board[position+1:]

while game_is_player:
     printboard(start_board)
     move(start_board)