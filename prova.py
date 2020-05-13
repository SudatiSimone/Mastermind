import random

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