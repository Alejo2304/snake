import sys, pygame

#main varibles
size = width, height = 800, 600
fps =  60

#Main Functions
def exit(): #this function is used to quit the loop while True.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

#initialize pygame.
pygame.init
screen = pygame.display.set_mode(size)  #creates the window. 
pygame.display.set_caption('Snake Game') #change caption of the window
clock = pygame.time.Clock()



while True:
    #draw all our elements
    exit() #check for the event pygame.QUIT and exit the execution.
    
    screen.fill(pygame.Color('green')) #fill the background with green color.
    clock.tick(fps) #limitates the speed of the drawing. 
    pygame.display.update()
