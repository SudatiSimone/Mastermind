from numpy import *

# Matrix
# Straight: color (Red=R, Orange=O, Black=B, Purple=P, white=W, yellow=Y)
# Column: the position ( 1, 2, 3, 4)
probability = array([[100, 100, 100, 100, 100, 100],
                     [100, 100, 100, 100, 100, 100],
                     [100, 100, 100, 100, 100, 100],
                     [100, 100, 100, 100, 100, 100]])

# As first iteration the computer choose random the sequence of colour
# TODO random
solution = ["Red", "Red", "Red", "Red"]

print("Choose a sequence of 4 colours (red, orange, yellow, black, purple, white) ")
input("Press Enter to continue...")
print("Round 1: ", solution)

i = 0
numberIterationGame = 10  # numbers of rounds available for computer to guess
gameOver = False

while i < numberIterationGame and gameOver is False:

    # Ask how many colors are in the correct position
    while True:
        print("How many element are correct?")
        value = int(input("0 or 1 or 2 or 3 or 4: "))
        if value == 0 or value == 1 or value == 2 or value == 3 or value == 4:
            break

    if value == 4:
        gameOver = True

    # Update probability's matrix
    position = 0
    while position < 4:
        if solution[position] == "Red":
            straight = 1  # prima riga contiene probabilità del rosso
        elif solution[position] == "Orange":
            straight = 2
        elif solution[position] == "Yellow":
            straight = 3
        elif solution[position] == "Black":
            straight = 4
        elif solution[position] == "Purple":
            straight = 5
        elif solution[position] == "White":
            straight = 6

        if value == 0: # All the colour are in bad position
            probability[position, straight] -= 100  # It's 100% the incorrect position for the select colour
        elif value == 1:
            probability[position, straight] -= 75  # It's 75% the incorrect position for the select colour
        elif value == 2:
            probability[position, straight] += 50  # It's 50% the correct position for the select colour
        elif value == 3:
            probability[position, straight] += 75  # It's 75% the correct position for the select colour


        print(probability)
        position += 1


    i += 1
    print("miao")

    # Choose the new solution
    # TODO funzione random pesata tra i colori a seconda del valore per ogni posizione

if value == 4:
    print()
    print("---------- Computer won the game! :) -----------")
    print("In " + str(i) + " iterations")
elif value < 4:
    print()
    print("---------- You have win the game! :) -----------")
    print("In " + str(i) + " iterations")


