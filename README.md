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

def __init__

    defines the variable x, y that represent the position in x axe and y axe, then in the variable pos we create a vector using x and y

def draw_fruit

    creates a rectangle and then draw the rectangle in the screen

def randomize

    updates the position of the fruit to a random position in the screen. 

# class SNAKE
    It creates an snake, it will work really similar to FRUIT, but instead of draw in just one cell, we will store and draw multiple cells that will represent our main character, the snake. 

    def __init__

    it containes self.body that represent the vectors where our snake is. 
    as well it containes self.direction, this one represent in which curret direction our 
    snake is moving. 

    def draw_snake

    This function will draw our snake into the screen.
    first it will create a rectangle and then will draw that reactangle into the screen.

    def move_snake

    this function will help us to move our snake into the screen, as well will add a new block when the condition new_block is true

    def add_block

    will change our boolean variable to True if the snake eat a fruit

# Class SCORE
    This class initialize an score in 0 and add points after every fruit that the snake ate

    def __init__
    initialize the variable score at 0

    def add_score 
    this add 100 points to the score, it is called in the class Main, in check_collision
    
    def draw_score
    this is intented to be a way to draw in screen the score so the user is able to see it while playing
    
# Class MAIN
    This class will contain the main logic that will be used for our game to run. 

    def __init__
    creates the object fruit and snake. 

    def update
    this function calls the functions move_snake, check_collision, check_fail

    def draw_elements
    calls the fuctions draw_fruit and draw_snake

    def check_collision
    this fuction will check if the snake eats a fruit, and if it does will call the fuction randomize for fruit and add_block for snake. 

    def check_fail
    this function will check if the snake is outside of the screen and then call the function game_over

    As well if the snake hits itself will call the fuction game_over

    def game_over
    this fuctions will end the execution of the program


# while True:
inside this infinite loop we will gather the events necessaries for change the direction of the snake.

as well we will call the fuction main_game.update() each time the event SCREEN_UPDATE is triggered by our timer. 

we will call the fuction main_game.draw_elements to draw our snake and fruit into the screen. 

