from numpy import *

# Matrix
# Straight: color (Red=R, Orange=O, Black=B, Purple=P, white=W, yellow=Y)
# Column: the position ( 1, 2, 3, 4)
probability = array([[0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                     [0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                     [0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                     [0.167, 0.167, 0.167, 0.167, 0.167, 0.167]])

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
        print(probability)
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
            colour = 0  # prima riga contiene probabilità del rosso
        elif solution[position] == "Orange":
            colour = 1
        elif solution[position] == "Yellow":
            colour = 2
        elif solution[position] == "Black":
            colour = 3
        elif solution[position] == "Purple":
            colour = 4
        elif solution[position] == "White":
            colour = 5

        count = 0  # default : no colour-position with 0% probability
        if value == 0:  # All the colour are in bad position
            probability[position, colour] = 0  # It's 100% the incorrect position for the select colour
            increase = 0.20
            # count how many position are not zero
            for x in range(6):
                if probability[position, x] == 0:
                    count += 1
            # use count to calculate the increase
            if count != 0 and count != 1:
                increase = 1 / (6 - count)

            # increase probability of not selected colour
            for x in range(6):
                # if not zero increase probability of +0.20
                if probability[position, x] != 0:
                    probability[position, x] += increase

        elif value == 1:  # Only one colour-position is correct
            # count how many position are not zero
            for x in range(6):
                if probability[position, x] == 0.0:
                    count += 1
            probability[position, colour] -= 75  # It's 75% the incorrect position for the selected colour

        elif value == 2:
            increase = 0.50  # It's 50% the correct position for the selected colour
            # count how many position are not zero
            for x in range(6):
                if probability[position, x] == 0.0:
                    count += 1
            # use count to calculate the increase
            if count != 0 and count != 1:
                increase = 1 / (6 - count)
            probability[position, colour] += increase
        elif value == 3:
            increase = 0.75  # It's 75% the correct position for the selected colour
            decrease = 0.25/5  # The others colour in that position
            # count how many position are not zero
            for x in range(6):
                if probability[position, x] == 0.0:
                    count += 1
            # use count to calculate the increase
            # NB: if three colour are correct and there is a zero
            # ==> all the 3 colour are correct
            if count != 0:
                increase = 1
                decrease = 1

            if probability[position, x] != 0.0:
                probability[position, colour] = increase

            for x in range(6):
                if probability[position, x] != 0.75 and probability[position, x] != 1:
                    probability[position, x] -= decrease

        position += 1

    # Control all the position in matrix, if there are negative value set it to zero
    for x in range(6):
        for y in range(4):
            if probability[y, x] < 0.0:
                probability[y, x] = 0.0

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
