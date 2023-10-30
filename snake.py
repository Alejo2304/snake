import sys, pygame, random, time
import tkinter as tk
from tkinter import ttk
from db import DB_SNAKE
from menu_gui import MENU
from pygame.math import Vector2

#DATABASE
db = DB_SNAKE()
db.open_connection()

game_id = db.execute(f"SELECT MAX(id_game) FROM games;")
if game_id[0] == None:
    game_id = 1
else:
    game_id = game_id[0] + 1
    
#main varibles
cells_number = 20 #NUMBER OF CELLS INS THE GRID
cells_size = 30 #SIZE IN PX OF EACH CELL
size = width, height = cells_number*cells_size, cells_number*cells_size
sec_played = 0
fps =  60


class PLAYER:

    def __init__(self):
        self.email = "guest"
        self.password = ""

    def login(self, email = 'guest', password = ''):

        email_select = db.execute(f"SELECT email FROM players WHERE players.email = '{email.lower()}';")
        password_select = db.execute(f"SELECT password FROM players WHERE players.email = '{email.lower()}';")

        if email_select != None:
            if email == email_select[0] and password == password_select[0]:
                self.email = email
                self.password = password
                return True
        else:
            return False
            
    def register(self, email, password, nickname):

        email_select = db.execute(f"SELECT email FROM players WHERE players.email = '{email.lower()}';")
        nickname_select = db.execute(f"SELECT nickname FROM players WHERE players.nickname = '{nickname.lower()}';")

        if email_select != None:
            return False
        elif nickname_select != None:
            return False
        else:
            db.execute(f"INSERT INTO players (email, password, nickname, register_date) VALUES('{email}', '{password}', '{nickname}', CURRENT_TIMESTAMP); ")
            return True

class FRUIT:

    def __init__(self):
        self.x = random.randint(0,cells_number-1)
        self.y = random.randint(0,cells_number-1)
        self.pos = Vector2(self.x,self.y)
        #this check how much fruits the snake eat per game.
        self.fruits_eated = 0

    def draw_fruit(self):
        #fruit_rect creates a rectangle with a random position in the screen with the size of the cell
        #Draw fruit_rect into the screen. 
        fruit_rect = pygame.Rect(int(cells_size*self.pos.x),int(cells_size*self.pos.y), cells_size, cells_size)
        pygame.draw.rect(screen,(255,0,0),fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cells_number-1)
        self.y = random.randint(0,cells_number-1)
        self.pos = Vector2(self.x,self.y)        

    def set_fruits(self, value):
        self.fruits_eated += value
        

class SNAKE:

    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
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

class SCORE:
    def __init__(self):
        self.score = 0
        self.text_size = 50

    def add_score(self):
        self.score += 100 #pending to update from the DATABASE

    def draw_score(self):
        font = pygame.font.Font(None, self.text_size)
        text = font.render(f"Your Score is: {self.score}", 1, (255,  0,  0))
        textpos = text.get_rect()
        textpos.topleft = screen.get_rect().topleft
        screen.blit(text, textpos)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.score = SCORE()
        self.player = PLAYER()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.score.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            #add score
            self.score.add_score()
            #Move the fruit of position.
            self.fruit.randomize()
            #update counter of fruits
            self.fruit.set_fruits(1)
            #add another block to the snake
            self.snake.add_block()
            
    
    def check_fail(self):
        #check if snake outside screen in x
        if not 0 <= self.snake.body[0].x < cells_number or not 0 <= self.snake.body[0].y < cells_number:
            self.game_over()
        #check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()


    def game_over(self):
        db.execute(f"INSERT INTO games(id_game,seconds_played, fk_player) VALUES({game_id},{sec_played}, '{player.email}');")
        db.execute(f"INSERT INTO fruits_per_game(fk_idfruit, fk_idgame, total_fruits) VALUES(1,{game_id},{main_game.fruit.fruits_eated});")
        db.close_connection()
        pygame.quit()
        sys.exit()


player = PLAYER()
menu = MENU()

menu.show(player)

#initialize pygame.
pygame.init()
#SET UP THE WINDOW
screen = pygame.display.set_mode(size)  #creates the window. 
pygame.display.set_caption('Snake Game') #change caption of the window
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT #creates a custom event that will later help us to set a timer
pygame.time.set_timer(SCREEN_UPDATE, 100) #It triggers our event Screen update every 150 ms
main_game = MAIN()
i = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        if event.type == SCREEN_UPDATE:
            main_game.update()
            i += 1
            if i == 10:
                sec_played += 1
                i = 0
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
        
    screen.fill(pygame.Color('green')) #fill the background with green color.
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(fps) #limitates the speed of the drawing. 
