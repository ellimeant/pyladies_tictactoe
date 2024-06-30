start_board = "--------------------"
player_user = "x"
player_computer = "o"
index = 0
game_is_player = True

def printboard(board):
    print(board)

printboard(start_board) # checks that the board is working

def user_board(board):
    while True:
        mark = player_user
        position = int(input("Which position do you want to play? Choose a number from 0-19! "))
        if position > 19 or board[position] != "-" :
            print("This is no valid position. Try again.")
        else:
            return position

def update_board(board, position, mark):
    return board[:position] + mark + board[position+1:]

while "-" in start_board:
    user_move = user_board(start_board)
    start_board = update_board(start_board, user_move, player_user)
    print(f"Here's the new board: {start_board}")

#while game_is_player:
     #printboard(start_board)
     #update_board(start_board)


#while index < len(start_board):
     