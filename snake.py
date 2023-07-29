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

class SNAKE:

    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            #create a rect
            block_rect = pygame.Rect(block.x*cells_size,block.y*cells_size,cells_size,cells_size)
            #draw the rectangle
            pygame.draw.rect(screen,(0,0,200),block_rect)
    
    def move_snake(self):
        body_copy = self.body[:-1] #copy the array except the last item. 
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]


#initialize pygame.
pygame.init
screen = pygame.display.set_mode(size)  #creates the window. 
pygame.display.set_caption('Snake Game') #change caption of the window
clock = pygame.time.Clock()

fruit = FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT #creates a custom event that will later help us to set a timer. 
pygame.time.set_timer(SCREEN_UPDATE, 150) #It triggers our event Screen update every 150 ms
  
while True:
    #draw all our elements
    #check for the event pygame.QUIT and exit the execution.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        if event.type == SCREEN_UPDATE:
            snake.move_snake()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1,0)
    
    
    screen.fill(pygame.Color('green')) #fill the background with green color.
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(fps) #limitates the speed of the drawing. 
