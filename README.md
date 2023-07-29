# snake.py
The objectve is to build a snake game using the library pygame. 

# objects in the screen. 
The idea is to create a grid of 25 cells x 25 cells, each cell will have a size of 
30px*30px. Each time the snake moves to any position it will move one cell up, down, 
left or right. As well if a fruit appears into the screen it will have the size of 1 
cell. 

for the screen 2 main variables will be create:

cells_number = 25 (the number of cells we want in our screen.)
cells_size = 30 (pixels.)



# Class FRUIT
This class will have 2 main sections, set position and draw fruit, in set position we will use a random number to generate the X cell and the Y cell. Then with draw functions we will place our Fruit into the screen.

# class SNAKE
It creates an snake, it will work really similar to FRUIT, but instead of draw in just one cell, we will store and draw multiple cells that will represent our main character, the snake. 

 def __init__

 it containes self.body that represent the vectors where our snake is. 
 as well it containes self.direction, this one represent in which curret direction our 
 snake is moving. 


# SNAKE movements
Now the snake is created it is needed to add some movement to the snake, how it works?

The snake is currently placed in an especific number of cells, in order to move the snake the head is moved to a new block, the block before the head will update its position to the place the head was before and the same will happen to the other blocks.

The requirements

1. We need a player input (event)
2. move the snake to the input provided on a certain time, we will need 

# Class MAIN
This class will contain the main logic that will be used for our game to run. 

# while True:
inside this infinite loop we will gather the events necessary for quiting the game,
chaging the direction of the snake, and of course drawing all of our objects into 
the screen. 
