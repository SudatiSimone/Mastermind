from numpy import *
import random

# Matrix
# Straight: color (Red=R, Orange=O, Black=B, Purple=P, white=W, yellow=Y)
# Column: the position ( 1, 2, 3, 4)
probability = array([[0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                     [0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                     [0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                     [0.167, 0.167, 0.167, 0.167, 0.167, 0.167]])

# As first iteration the computer choose random the sequence of colour
# TODO weighted random

solution = ["Red", "White", "Black", "Red"]

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
            colour = 0  # prima colonna contiene probabilità del rosso
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
            probability[position, colour] = 0.0  # It's 100% the incorrect position for the select colour
            increase_NotSelected = 1/5
            # count how many position are zero
            for x in range(6):
                if probability[position, x] == 0.0:
                    count += 1
            # use count to calculate the increase
            if count != 0 and count != 1:
                increase_NotSelected = 1 / (6 - count)

            # increase probability of not selected colour
            for x in range(6):
                if probability[position, x] != 0:
                    probability[position, x] += increase_NotSelected

        elif value == 1:  # Only one colour-position is correct
            increase_Selected = 0.25  # It's 25% the correct position for the selected colour
            increase_NotSelected = 0.75 / 5  # The remaining probability
            # count how many position are not zero
            for x in range(6):
                if probability[position, x] == 0.0:
                    count += 1
            # use count to calculate the increase and decrease
            if count >= 1:
                # increase don't change
                increase_NotSelected += (0.75 / 5) * count / (5 - count)


        elif value == 2:
            increase_Selected = 0.50  # It's 50% the correct position for the selected colour
            increase_NotSelected = 0.1  # The remaining probability 0.50/5
            # count how many position are zero
            for x in range(6):
                if probability[position, x] == 0.0:
                    count += 1
            # use count to calculate the increase and decrease
            if count >= 1:
                # increase don't change
                increase_NotSelected += (0.50 / 5) * count / (5 - count)

        elif value == 3:
            increase_Selected = 0.75  # It's 75% the correct position for the selected colour
            increase_NotSelected = 0.25 / 5  # The remaining probability
            # count how many position are zero
            for x in range(6):
                if probability[position, x] == 0.0:
                    count += 1

            # use count to calculate the increase
            if count >= 1:
                # increase don't change
                increase_NotSelected += (0.25 / 5) * count / (5 - count)
        if value != 0:
            if probability[position, colour] != 0.0:
                probability[position, colour] = increase_Selected
            for x in range(6):
                if probability[position, x] != increase_Selected and probability[position, x] != 0.0:
                    probability[position, x] += increase_NotSelected
        position += 1

    # Control all the position in matrix, if there are negative value set it to zero
    # If one position is 1 all the other correlated colours are set to zero
    for x in range(6):
        for y in range(4):
            if probability[y, x] < 0.0:
                probability[y, x] = 0.0
            elif probability[y, x] >= 1.0:
                probability[y, x] = 1.0
                for t in range(6):
                    if probability[y, t] != 1.0:
                        probability[y, t] = 0.0


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


calculate_solution :
my_list = ['A'] * 5 + ['B'] * 5 + ['C'] * 90


def calculate_solution( list ):

   color = "Red"  # di default
   my_list = ['R'] * list[0] + ['O'] * list[1] + ['Y'] * list[2] +['B'] * list[3] + ['Y'] * list[4] +['W'] * list[5]
   name = random.choice(my_list)
   if name == 'R':
       color = "Red"
   elif name == 'O':
       color = "Orange"
   elif name == 'Y':
       color = "Yellow"
   elif name == 'B':
       color = "Black"
   elif name == 'P':
       color = "Purple"
   elif name == 'W':
       color = "White"
   return color