#tic tac toe

#each line is a board game. game ends when all 19 empty spaces "-" are full with X or O, or if 3 X or 3 0 occur next to each other
#somewhere check for everything being read in lower or upper case so that doesn't cause any problems
def evaluate(boardstring):
    xxx = "xxx"
    ooo = "ooo"
    empty_space = " "
    if xxx in boardstring: 
        # this value is boardstring too because it is the input that will change everytime
        return("X won")
    elif ooo in boardstring:
        # this value is boardstring too because it is the input that will change everytime
        return("O won")
    elif empty_space in boardstring: # note to self: default check mode is that an utterance is True.
        return("game not over yet")
    else:
        return("draw")

# use return instead of print to get rid of the "None" at the end
print(evaluate("cheooox ory"))
    