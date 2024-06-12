#there is suddenly a syntax error somewhere, I think because I put my cursor somewhere wrong... find the issue!
boardstring = "hereare19characters" # my teststring, it has no o or x
boardstringo = "ooreare19characters" #testing string with x

def move(board, mark, position):
     return board[:position] + mark + board[position+1:] # that works, yay!

print(move(boardstring, "x", 20))

def player_move(board, mark, position):
    position = int(input("Which position do you want to play? Choose a number from 0-19! "))
    if position > 19:
        print("This is no valid position.")
    elif position <= 19:
        return board[:position] + mark + board[position+1:] # works but doesn't save the string as a copy.
    
print(player_move(boardstring, "o", 5))

def player_move(board, mark, position):
    position = int(input("Which position do you want to play? Choose a number from 0-19! "))
    if position > 19:
        print("This is no valid position.")
    elif position <= 19:
        placing = board[position]
        print(placing) # for testing reasons
        if placing == "x":
            print("This position is occupied.")
        elif placing == "o":
            print("This position is occupied.") #tested with variable boardstringo and it works! Problem: when position is an integer, it won't take 0 (zero)
        else:
            board3 = board.replace(placing, mark) # this works to create the new board, but how to get it to continue in others? Have all the variables at the beginning?
            print("This is", board3)
    
print(player_move(boardstringo, "o", 1)) # The mark can be fixed, the O in position is a random dummy as it is actually never called because the function calls for user input. 
#\n no need for user input at the mark because it's decided from the start what mark the player gets and which the computer.

from random import randrange
pc_move = randrange(0,19) # start and stop of randrange for the computer position

def computer_move(board, mark, position): # mark is x for computer
    position = randrange(0,19)
    placing = board[position]
    if placing == "x":
        print("Occupied by x, try again, computer!")
        position = randrange(0,19)
    elif placing == "o":
        print("Occupied by o, try again, computer!")
        position = randrange(0,19)
    else:
        board4 = board.replace(placing, mark)
        print("The new board is", board4)

print(computer_move(boardstring, "x", 3))