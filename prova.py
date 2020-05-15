import random
from numpy import *

# This file is to know if the single function works well
# NB: It isn't formal (test) but It is use to test during coding!
# I will delete this file when program works well


color = "Red"  # di default
list = [0 , 0.23, 1, 0.876, 0.3]
list[0]*= 100
list[1]*= 100
list[2]*= 100
list[3]*= 100
list[4]*= 100

for k in range (5):
    list[k] = int(list[k])

my_list = ['R'] * 2 + ['O'] * 2 + ['Y'] * 2 + ['B'] * 2 + ['Y'] * 2 + ['W'] * 2
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

print(color)
print(list)
for x in range (4):
    print(x)


vett_max = [0, 0, 0, 0]
col = "Red"
probability = array([[0.167, 0.167, 0.167, 0.167, 0.167, 0.175],
                     [0.167, 0.80, 0.167, 0.167, 0.167, 0.167],
                     [0.167, 0.167, 0.4, 0.167, 0.167, 0.167],
                     [0.167, 0.167, 0.167, 0.167, 0.167, 0.167]])

for x in range(4):
    maximum = 0
    for y in range(6):
        if y == 0:
            maximum = probability[x, y]
            col = "Red"
        elif maximum < probability[x, y]:
            maximum = probability[x, y]
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
        vett_max[x] = col

print (vett_max)