from numpy import *
import random


# function that calculate in a weighted random way the colours
def calculate_solution(list):
    color = "Red"  # di default
    n0 = list[0] * 100
    n0 = int(n0)
    n1 = list[1] * 100
    n1 = int(n1)
    n2 = list[2] * 100
    n2 = int(n2)
    n3 = list[3] * 100
    n3 = int(n3)
    n4 = list[4] * 100
    n4 = int(n4)
    n5 = list[5] * 100
    n5 = int(n5)

    my_list = ['R'] * n0 + ['O'] * n1 + ['Y'] * n2 + ['B'] * n3 + ['P'] * n4 + ['W'] * n5
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


# function that calculate the solution (the colours) with higher probability
def calculate_solution_max(lista):
    max_list = 0
    col = "Red"
    for y in range(6):
        if y == 0:
            max_list = lista[y]
            col = "Red"
        elif max_list < lista[y]:
            max_list = lista[y]
            if y == 1:
                col = "Orange"
            elif y == 2:
                col = "Yellow"
            elif y == 3:
                col = "Black"
            elif y == 4:
                col = "Purple"
            elif y == 5:
                col = "White"
    return col


# Matrix
# Straight: color (Red=R, Orange=O, Black=B, Purple=P, white=W, yellow=Y)
# Column: the position ( 1, 2, 3, 4)
# todo USE for to complete matrix
probability = array([[0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                     [0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                     [0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                     [0.167, 0.167, 0.167, 0.167, 0.167, 0.167]])

solution = ["Red", "Red", "Red", "Red"]
solution_prec = ["Red", "Red", "Red", "Red"]
solution_prec_prec= ["Red", "Red", "Red", "Red"]
print("Choose a sequence of 4 colours (red, orange, yellow, black, purple, white) ")
input("Press Enter to continue...")

i = 0
numberIterationGame = 12  # numbers of rounds available for computer to guess
gameOver = False
increase_Selected = 0
increase_NotSelected = 0

while i < numberIterationGame and gameOver is False:

    # Ask how many colors are in the correct position
    while True:
        print(" Red  Orange  Yellow  Black  Purple  White")
        print(probability)
        # Choose the new solution
        # In 3, 6 and 9 iterations choose the higher probability
        # In all the other iterations choose a random weighted solution
        if i % 3 == 0 and i!=0 :
                solution = [calculate_solution_max(probability[0, :]), calculate_solution_max(probability[1, :]),
                            calculate_solution_max(probability[2, :]), calculate_solution_max(probability[3, :])]
                if solution == solution_prec or solution == solution_prec_prec:
                    while solution == solution_prec or solution == solution_prec_prec:
                        solution = [calculate_solution(probability[0, :]), calculate_solution(probability[1, :]),
                                    calculate_solution(probability[2, :]), calculate_solution(probability[3, :])]
        else:
            while solution == solution_prec or solution == solution_prec_prec:
                solution = [calculate_solution(probability[0, :]), calculate_solution(probability[1, :]),
                            calculate_solution(probability[2, :]), calculate_solution(probability[3, :])]
        print("Round " + str(i + 1) + " : ", solution)
        print("How many element are correct?")
        value = int(input("0 or 1 or 2 or 3 or 4: "))
        print()
        print()
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
        sum_tot_1 = 0
        if value == 0:  # All the colour are in bad position
            temp = probability[position, colour]
            probability[position, colour] = 0.0  # It's 100% the incorrect position for the select colour
            increase_NotSelected = temp / 5
            # count how many position are zero
            for x in range(6):
                if probability[position, x] == 0.0:
                    count += 1
            # use count to calculate the increase
            if count != 0 and count != 1:
                increase_NotSelected = temp / (6 - count)

            # increase probability of not selected colour
            for x in range(6):
                if probability[position, x] != 0:
                    probability[position, x] += increase_NotSelected

        elif value == 1:  # Only one colour-position is correct: It's the worst case. Information is very low

            if 0.0 < probability[position, colour] < 0.10:
                increase_Selected = probability[position, colour] + 0.020
            elif 0.15 <= probability[position, colour] < 0.30:
                increase_Selected = probability[position, colour] + 0.025
            elif 0.30 <= probability[position, colour] <= 0.75:
                increase_Selected = probability[position, colour] - 0.05
            else:
                increase_Selected = probability[position, colour] - 0.10

            variation = probability[position, colour] - increase_Selected
            increase_NotSelected = variation / 5  # The remaining probability
            # count how many position are not zero
            for x in range(6):
                if probability[position, x] == 0.0:
                    count += 1
            # use count to calculate the increase and decrease
            if count >= 1:
                # increase don't change
                increase_NotSelected += (variation / 5) * count / (5 - count)


        elif value == 2:
            if 0.0 < probability[position, colour] < 0.15:
                increase_Selected = probability[position, colour] + 0.05
            elif 0.15 <= probability[position, colour] < 0.30:
                increase_Selected = probability[position, colour] + 0.10
            elif 0.30 <= probability[position, colour] <= 0.50:
                increase_Selected = 0.50
            else:
                increase_Selected = probability[position, colour] + 0.05

            variation = probability[position, colour] - increase_Selected

            increase_NotSelected = variation / 5  # The remaining probability 0.50/5
            # count how many position are zero
            for x in range(6):
                if probability[position, x] == 0.0:
                    count += 1

            # use count to calculate the increase and decrease
            if count >= 1:
                # increase don't change
                increase_NotSelected += (variation / 5) * count / (5 - count)

        elif value == 3:

            if 0.0 < probability[position, colour] < 0.15:
                increase_Selected = probability[position, colour] + 0.25
            elif 0.15 <= probability[position, colour] < 0.30:
                increase_Selected = probability[position, colour] + 0.20
            elif 0.30 <= probability[position, colour] < 0.45:
                increase_Selected = probability[position, colour] + 0.25
            elif 0.45 <= probability[position, colour] < 0.75:
                increase_Selected = 0.75
            else:
                increase_Selected = probability[position, colour] + 0.05

            variation = probability[position, colour] - increase_Selected
            increase_NotSelected = variation / 5  # The remaining probability
            # count how many position are zero
            for x in range(6):
                if probability[position, x] == 0.0:
                    count += 1

            # use count to calculate the increase
            if count >= 1:
                # increase don't change
                increase_NotSelected += (variation / 5) * count / (5 - count)

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

    if i==0: # first iteration
        solution_prec=solution
    else:
        solution_prec_prec= solution_prec
        solution_prec = solution
    i += 1
    # print(calculate_solution(probability[0, :]))
    # print(calculate_solution(probability[1, :]))
    # print(calculate_solution(probability[2, :]))
    # print(calculate_solution(probability[3, :]))

if value == 4:
    print()
    print("---------- Computer won the game! :) -----------")
    print("---------- In " + str(i) + " iterations---------")
    print("The solution is: " + str(solution))
elif value < 4:
    print()
    print("---------- You have win the game! :) -----------")
    print("---------- In " + str(i) + " iterations---------")
    print("The algorithm tell me that the solution is: ")
    solution = [calculate_solution_max(probability[0, :]), calculate_solution_max(probability[1, :]),
                calculate_solution_max(probability[2, :]), calculate_solution_max(probability[3, :])]
    print(solution)
