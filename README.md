# Mastermind
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

My program in python to solve mastermind game.

### **My idea to solve the problem:**

Using a matrix, a position is selected with (x,y) where x stands for straights and y for columns.

X corresponds to the position in the sequence

Y corresponds to the selected colour

<img src="matrix.jpg"
     style="float: left; margin-right: 10px;" />

In this way we could update the value of probability for all couple (position, colour).

At the start of the game all the value are set to 1/6 = 0.167 so the probabilities are equal.


### **How to play?**
--> Download or clone the repository and run the main.py file

### **Rules:**
Think about a sequence of 4 colours choosen between the six colours: red, yellow, black, white, orange, purple.

Correct sequece for example are: R R R R or W R Y B or B W R O

The computer output at video a first solutions. Input the number of correct couple (position, solution).

The computer output at video a second solutions. Input the number of correct couple (position, solution).

And so go on...

If in ten iterations the computer guess your sequence ==> computer wins the game

else ==> you won the game! :)

