import random

color = "Red"  # di default
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