import sys, pygame, time

#main varibles
size = width, height = 800, 600

#initialize the screen
pygame.init

window = pygame.display.set_mode(size)  #creates the window. 
pygame.display.set_caption('Snake Game') #change caption of the window
screen = pygame.display.get_surface()

def exit(): #this function is used to quit the loop while True.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

while True:
    exit()
