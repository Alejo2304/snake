import sys, pygame, random
from pygame.math import Vector2

#main varibles
cells_number = 20
cells_size = 30

size = width, height = cells_number*cells_size, cells_number*cells_size
fps =  60

#Main Functions


class FRUIT:

    def __init__(self):
        self.x = random.randint(0,cells_number-1)
        self.y = random.randint(0,cells_number-1)
        self.pos = Vector2(self.x,self.y)

    def draw_fruit(self):
        #fruit_rect creates a rectangle with a random position in the screen with the size of the cell
        #Draw fruit_rect into the screen. 
        fruit_rect = pygame.Rect(int(cells_size*self.pos.x),int(cells_size*self.pos.y), cells_size, cells_size)
        pygame.draw.rect(screen,(255,0,0),fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cells_number-1)
        self.y = random.randint(0,cells_number-1)
        self.pos = Vector2(self.x,self.y)        

class SNAKE:

    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            #create a rect
            block_rect = pygame.Rect(block.x*cells_size,block.y*cells_size,cells_size,cells_size)
            #draw the rectangle
            pygame.draw.rect(screen,(0,0,200),block_rect)
    
    def move_snake(self):
        
        if self.new_block == True:
            body_copy = self.body[:] #copy the array except the last item. 
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1] #copy the array except the last item. 
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            #Move the fruit of position.
            self.fruit.randomize()
            # add another block to the snake
            self.snake.add_block()

#initialize pygame.
pygame.init
screen = pygame.display.set_mode(size)  #creates the window. 
pygame.display.set_caption('Snake Game') #change caption of the window
clock = pygame.time.Clock()


SCREEN_UPDATE = pygame.USEREVENT #creates a custom event that will later help us to set a timer. 
pygame.time.set_timer(SCREEN_UPDATE, 150) #It triggers our event Screen update every 150 ms

main_game = MAIN()
while True:
    #draw all our elements
    #check for the event pygame.QUIT and exit the execution.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)
    
    
    screen.fill(pygame.Color('green')) #fill the background with green color.
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(fps) #limitates the speed of the drawing. 
