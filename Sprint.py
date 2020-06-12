import random                                               #imports random package that allow use of random functions

game_run = True                                             #Game Loop Condition
dice1 = 0                                                   #Dice 1
dice2 = 0                                                   #Dice 2

while game_run:                                             #Game Loop
    game = input('Do you wanna roll a dice? type y/n')
    if game[0].lower() == 'y':                              #sets first letter of game lowercase vor easy validation
        dice1 = random.randint(1, 6)                        #generates a random number between 1 and 6 for dice 1
        dice2 = random.randint(1, 6)                        #generates a random number between 1 and 6 for dice 2
        print('Dice 1: ' + str(dice1))
        print('Dice 2: ' + str(dice2))
        totTuple = ('Total: ', str(dice1 + dice2))          #Gets the sum of the 2 dices and add the 2 strings in a tuple

        total = ''.join(totTuple)                           #Joins all the strings in the tuple into var 'total'

        print(total)                                        #prints total

    else:                                                   #if any key other than 'y' is pressed
        print('Thank you for playing, come back soon.')
        game_run = False                                    #ends the game loop which ends the program
