# Mastermind

My program in python to solve mastermind game.

### **My idea to solve the problem:**

To use a matrix, a position is selected with (x,y) where x stands for straights and y for columns.

X corresponds to the position in the sequence

Y corresponds to the selected colour

<img src="matrix.jpg"
     style="float: left; margin-right: 10px;" />

In this way we could update the value of probability for all couple (position, colour).

At the start of the game all the value are set to 1/6 = 0.167 so the probabilities are equal.
sfdf

### **How to play?**


### **Rules:**
Think about a sequence of 4 colours choosen between the six colours: red, yellow, black, white, orange, purple.

Correct sequece for example are: R R R R or W R Y B or B W R O

The computer output at video a first solutions. Input the number of correct couple (position, solution).

The computer output at video a second solutions. Input the number of correct couple (position, solution).

And so go on...

If in ten iterations the computer guess your sequence ==> computer wins the game
else ==> you won the game! :)

