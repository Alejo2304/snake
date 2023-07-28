import sys, pygame, random
from pygame.math import Vector2

#main varibles
cells_number = 20
cells_size = 30

size = width, height = cells_number*cells_size, cells_number*cells_size
fps =  60

#Main Functions
def exit(): #this function is used to quit the loop while True.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

class FRUIT:

    def __init__(self):
        self.x = random.randint(0,cells_number-1)
        self.y = random.randint(0,cells_number-1)
        self.pos = Vector2(self.x,self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(cells_size*self.pos.x),int(cells_size*self.pos.y), cells_size, cells_size)
        pygame.draw.rect(screen,(255,0,0),fruit_rect)

class SNAKE:
    pass


#initialize pygame.
pygame.init
screen = pygame.display.set_mode(size)  #creates the window. 
pygame.display.set_caption('Snake Game') #change caption of the window
clock = pygame.time.Clock()

fruit = FRUIT()


  
while True:
    #draw all our elements
    exit() #check for the event pygame.QUIT and exit the execution.
    
    screen.fill(pygame.Color('green')) #fill the background with green color.
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(fps) #limitates the speed of the drawing. 
