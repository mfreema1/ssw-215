from random import randint

#TODO: CONVERT THE BOARD TO ONE THAT YOU REMOVE FROM
#THIS WAY, WE CAN USE THE SET REMOVE FUNCTION TO ELIMINATE THINGS

#the board has things appended to it
def takeTurn(board):
    die_1, die_2 = randint(1,6), randint(1,6)
    choices = getPossibleFlips(die_1, die_2, board)
    if(choices == []):
        print("Looks like you have no valid moves.  Other player's turn.")
    elif(len(choices) == 1):
        print("You only have one valid move: " + str(choices[0]))
        board.add(int(choices[0]))
    else:
        #print all of their choices
        result = input("Which would you like to flip? Your choices: " + ",".join(map(str, choices)) + '\n')
        while(int(result) not in choices):
            result = input("Sorry, that's not a valid choice.  Try again: " + '\n')
        board.add(int(result))

def getPossibleFlips(die_1, die_2, board):
    choices = []
    sum = die_1 + die_2
    if((sum < 9) and (sum not in board)):
        choices.append(sum)
    if(die_1 not in board):
        choices.append(die_1)
    if(die_2 not in board):
        choices.append(die_2)
    return choices

def simulateGame():
    full_board = set(range(1,10))
    #clear both players boards
    player_1_board = set()
    player_2_board = set()
    while(1):
        #win scenarios
        if(player_1_board == player_2_board == full_board):
            print("Looks like both players finished, a tie!")
            break
        elif(player_1_board == full_board):
            print("Player one has an empty board, they win!")
            break
        elif(player_2_board == full_board):
            print("Player two has an empty board, they win!")
            break
        #otherwise, play the game
        else:
            #play player one's turn
            print("Player 1's turn: ")
            takeTurn(player_1_board)
            print('\n')
            print("Player 2's turn: ")
            takeTurn(player_2_board)
            print('\n')

if __name__ == '__main__':
    while(1):
        response = input("Would you like to play a game of shut the box? Enter 'y' to play, anything else to quit: ")
        if(response == 'y'):
            simulateGame()
        else:
            print("Bye!")