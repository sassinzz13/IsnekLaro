from tkinter import *
import random
import sys
import os

"""
Welcome to Javascript developer learning python

solely doing this for the purpose of learning python especially at the functions part
"""

#variables that are used in the game
GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 100
BG_COLOR = "black"
BODY_PARTS = 1
FOOD_COLOR = "#FF0000"
SNAKE_COLOR = "green"
SPACE_SIZE = 50
SCORE = 0
direction = 'down'


#main functions()
#a class is a blueprint for making objects within a function
class Snake():
    def __init__ (self):
        self.body_size  = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
               
            #we using x, y becuase our list have 2 coordinates
            for x,y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
                self.squares.append(square)

class Food():
    #will construct the food object
    def __init__(self):

        #also learning rand
        #to convert to pixel 
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        #coordinates
        self.coordinates = [x, y]

        #draw the food object to canvas
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

#2 parameters to call
#these gives us initial directions for our snake
def turnCoordinates(snake, food):
    
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    #0 is the head of the snake
    snake.coordinates.insert(0, (x, y))

    #make a new graphic for the snake head
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snakee")

    #update list of snakes
    snake.squares.insert(0, square)

    # to eat the apple we need logic
    if x == food.coordinates[0] and y == food.coordinates[1]:

        global SCORE

        SCORE += 1
        label.config(text="Score:{}".format(SCORE)) 
        canvas.delete("food")
        food = Food()

    #delete the last body parts 
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    #collissions statement
    if collissions(snake):
        game_over()
    
    else:  
        #game time
        window.after(SPEED, turnCoordinates, snake, food)

#the logic function for the directions 
def changeDirections(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    
    if new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction

#Game over when collided with wall statement logic
def collissions(snake):
    x , y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print("Game OVER")
        return True
    
    elif y < 0 or y >= GAME_HEIGHT:
        print("Game OVER")
        return True
    
    for BODY_PARTS in snake.coordinates[1:]:
        if x == BODY_PARTS[0] and y == BODY_PARTS[1]:
            print("Game over")
            return True
        
    return False

#Restart?
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
#game over function
def game_over():
    button = Button(text="Restart", font=("roboto", 40), command=restart_program).pack()
    
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('roboto', 70), text="GAME OVER", fill="red", tag="gameover")

#Our TKinter gui functions
window = Tk()
window.title("Larong Isnake")
window.resizable(True, True)
window.attributes('-fullscreen', True)


#create a score label
label = Label(window, text="score:{}".format(SCORE), font=("roboto", 40)) 
label.pack()


#make a canvas to create a board
canvas = Canvas(window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

#to render window
window.update()

#to center window to screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#variables for centering the window in basic algebra language
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

#geometry shits to center the window
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#our key functionality
window.bind('<Left>', lambda event: changeDirections('left'))
window.bind('<Down>', lambda event: changeDirections('down'))
window.bind('<Right>', lambda event: changeDirections('right'))
window.bind('<Up>', lambda event: changeDirections('up'))

#naming our functions through variables
snake = Snake()
food = Food()
turnCoordinates(snake,food)

#console DEBUGGER
print("Game is up and running goodluck soldier")


#the loop for the window
window.mainloop()

