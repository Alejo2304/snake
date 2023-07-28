# snake.py
The objectve is to build a snake game using the library pygame. 

# objects in the screen. 
The idea is to create a grid of 25 cells x 25 cells, each cell will have a size of 30px*30px. Each time the snake moves to any position it will move one cell up, down, left or right. As well if a fruit appears into the screen it will have the size of 1 cell. 

for the screen 2 main variables will be create:

cells_number = 25 (the number of cells we want in our screen.)
cells_size = 30 (pixels.)

# Class FRUIT
This class will have 2 main sections, set position and draw fruit, in set position we will use a random number to generate the X cell and the Y cell. Then with draw function we will place our Fruit into the screen. 

