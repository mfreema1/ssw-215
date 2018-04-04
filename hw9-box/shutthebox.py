from random import randint

NO_MOVE_FLAG = False

#the board has things appended to it
def takeTurn(board):
    #get a reference to the global flag
    global NO_MOVE_FLAG
    die_1, die_2 = randint(1,6), randint(1,6)
    print("Rolled a " + str(die_1) + " and a " + str(die_2))
    choices = getPossibleFlips(die_1, die_2, board)
    if(len(choices) == 0):
        if(NO_MOVE_FLAG == True):
            print("Two turns with no moves! Start over!")
            raise SystemExit
        else:
            print("Looks like you have no valid moves.  Other player's turn.")
            NO_MOVE_FLAG = True
    elif(len(choices) == 1):
        print("You only have one valid move: " + str(next(iter(choices))))
        board.discard(int(next(iter(choices))))
        NO_MOVE_FLAG = False
    else:
        #print all of their choices
        result = input("Which would you like to flip? Your choices: " + ",".join(map(str, choices)) + '\n')
        while(int(result) not in choices):
            result = input("Sorry, that's not a valid choice.  Try again: " + '\n')
        board.discard(int(result))
        NO_MOVE_FLAG = False

def getPossibleFlips(die_1, die_2, board):
    choices = set([])
    sum = die_1 + die_2
    if(sum in board):
        choices.add(sum)
    if(die_1 in board):
        choices.add(die_1)
    if(die_2 in board):
        choices.add(die_2)
    return choices

def simulateGame():
    empty_board = set([])
    #clear both players boards
    player_1_board = set(range(1,10))
    player_2_board = set(range(1,10))
    while(1):
        #win scenarios
        if(player_1_board == player_2_board == empty_board):
            print("Looks like both players finished, a tie!")
            break
        elif(player_1_board == empty_board):
            print("Player one has an empty board, they win!")
            break
        elif(player_2_board == empty_board):
            print("Player two has an empty board, they win!")
            break
        #otherwise, play the game
        else:
            #play player one's turn
            print("Player 1's turn: ")
            print("Player 1's board: " + ",".join(map(str, player_1_board)))
            takeTurn(player_1_board)
            print('\n')
            #play player two's turn
            print("Player 2's turn: ")
            print("Player 2's board: " + ",".join(map(str, player_2_board)))
            takeTurn(player_2_board)
            print('\n')

if __name__ == '__main__':
    while(1):
        response = input("Would you like to play a game of shut the box? Enter 'y' to play, anything else to quit: ")
        if(response == 'y'):
            simulateGame()
        else:
            print("Bye!")
            break;