
import breakout    #! starting with the pong game, but slowly transformed 
import lib         #* my own library of "stuff" 
import time        #- for time function
import art         #- for ASCII art
import turtle      #- for turtle (the old Tcl/Tk) graphics
import time        #- for time functions
import random      #- for random number generation
import os          #- for OS commands to clear the screen
import tkinter     #- to get the TK/TL errors 


#- Yellow -  Information with a general, but relative importance
#? Orange -  Examples, abbreviations, acronyms, or explanations
#+ Green -   Key words, proper nouns, dates, symbols or mathematical formulas
#~ Blue -    Definitions of key words, or tabular data
#! Pink -    Important, relative to a test or my career
#* Purple -  Personal interest
# // Gray - Done

#- establishing variables, immporting modules and setting up functions

W = 800
H = 600
C = 20

game_over = False
game_running = False

block_width = 100                           # don't know why I love this size
block_height = 20
block_gap = 2  
ball_start = 0
paddle_start = 0 - H/2 + C*3 

message_text = ""
message_timer = 0


class Paddle(turtle.Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.length = 100
        self.base = 20 
        self.width = 20
        self.penup()
        self.shapesize(stretch_len=self.length/self.base, stretch_wid=self.width/self.base)
        self.setheading(0)
        self.color("white")
        self.speed("fastest")
        self.goto(coordinates[0], coordinates[1])
        self.screen_width = W
        self.paddle_half = (self.length/self.base) * 10   #! pixels versus coordiantes 
        print(turtle.getshapes())
        print(self.shape())

    def left(self):
        print("LEFT")
        x = self.xcor() - self.width*4
        y = self.ycor()
        left_limit = -(self.screen_width / 2) + self.length/2
        x = max(x, left_limit) # okay, never more than left limit  
        self.goto(x, y)

    def right(self):
        print("RIGHT")
        x = self.xcor() + self.width*4
        y = self.ycor()
        right_limit = (self.screen_width / 2) - self.length/2
        x = min(x, right_limit)
        self.goto(x, y)


class Ball(turtle.Turtle):
    def __init__(self, start_x=0, start_y=0, speed=4):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(start_x, start_y)

        self.dx = random.choice([-1, 1]) * speed
        self.dy = speed
        self.radius = 10

    def move(self):
        """Move the ball by its dx/dy vector."""
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_x(self):
        """Reverse horizontal direction."""
        self.dx *= -1

    def bounce_y(self):
        """Reverse vertical direction."""
        self.dy *= -1

    def reset(self):
        """Reset ball to center and reverse direction."""
        self.goto(0, 0)
        self.bounce_y()


def draw_blocks():
    blocks.clear()
    for b in block_dic:
        if b["alive"]:
            blocks.goto(b["x"] - block_width/2, b["y"] + block_height/2) #? Move to top-left corner of the block
            blocks.color(b["color"])
            blocks.shapesize(
                stretch_wid=block_height / 20,
                stretch_len=block_width / 20
                )
            blocks.goto(b["x"], b["y"])
            blocks.stamp()

def check_paddle_collision(ball, paddle):
    # Paddle bounds
    p_left   = paddle.xcor() - paddle.length/2
    p_right  = paddle.xcor() + paddle.length/2
    p_top    = paddle.ycor() + paddle.width/2

    # Ball bottom
    ball_bottom = ball.ycor() - ball.radius

    # Collision check
    if (
        ball.dy < 0 and                         #? is moving downward
        p_left <= ball.xcor() <= p_right and    #? the ball’s x‑position is horizontally inside the paddle (algebric inequality)
        ball_bottom <= p_top):                  #? the bottom of the ball has reached the top surface of the paddle
        show_message("Hit!")
        
        ball.bounce_y()

def check_block_collision(ball, block_dic):
    for b in block_dic:
        if not b["alive"]:
            continue

        # Block bounds
        left   = b["x"] - block_width/2
        right  = b["x"] + block_width/2
        top    = b["y"] + block_height/2
        bottom = b["y"] - block_height/2

        # Ball position
        bx = ball.xcor()
        by = ball.ycor()
        r = ball.radius

        # Collision check
        if (left - r <= bx <= right + r and
            bottom - r <= by <= top + r):

            # Mark block dead
            b["alive"] = False

            # Bounce the ball
            ball.bounce_y()

            return True   # stop after first hit




    return False


def check_wall_collision(ball):
    # Left wall
    if ball.xcor() - ball.radius <= -W/2:
        ball.bounce_x()

    # Right wall
    if ball.xcor() + ball.radius >= W/2:
        ball.bounce_x()

    # Top wall
    if ball.ycor() + ball.radius >= H/2:
        ball.bounce_y()

    # Bottom (missed ball)
    if ball.ycor() - ball.radius <= -H/2:
        return "miss"




def show_message(text, duration=0.7):
    global message_text, message_timer
    message_text = text
    message_timer = duration
    message.clear()
    message.write(text, align="center", font=("Arial", 20, "bold"))


def quit_app():
    global game_over
    game_over = True
    screen.bye()   #- closes the window

def start_game():
    global game_running
    game_running = True
    message.clear()


#- the MAIN program

lib.clear_screen()  # - text based
title = "Breakout"
nam = os.path.basename(__file__)
nam = nam.replace(".py", "")
day = title + " - " + nam
print(art.text2art(title, font='medium'))

#- Main screen

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=W, height=H)
screen.title(title)
screen.tracer(0)  # - turning off the annimation

#- the Paddle

paddle = Paddle((0,paddle_start)) #? starting at bottom of screen, the C is the default Turtle size 

#- the Blocks

blocks = turtle.Turtle()
blocks.hideturtle()
blocks.penup()
blocks.speed("fastest")
blocks.shape("square")

block_unit = block_width + block_gap        # yeah, working in the gap but might change it later 
block_row = int(W/block_unit)               # how many blocks can fit on a row based on screen width
block_x = (                                 # making sure row of blocks is centered  
    -((block_row * block_unit) / 2) + (block_width / 2))
block_start = 200
block_colors = ["cyan", "red", "orange", "green", "purple", "yellow", "blue"]
block_dic = []   

for j in range(5):
    y = int(block_start - (block_height + block_gap)*j)
    for i in range(block_row):
        x = int(block_x + i * block_unit)
        block_dic.append({"x": x, "y": y, "color": block_colors[j], "alive": True })

draw_blocks()

#- the Ball

ball = Ball()

#- the Scoreboard

message = turtle.Turtle()
message.hideturtle()
message.penup()
message.color("white")


#- getting things moving 

screen.update()  #- update the screen because tracer turned off the animation
screen.listen()  #- this is essential for reading from the keyboard 

screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")
screen.onkey(quit_app, "q")
screen.onkey(quit_app, "Q")
screen.onkey(start_game, "space")

message.clear()
message.goto(0, H/2 - 80)   # near the top of the screen
message.write(
        "Press SPACE to start\nPress Q to quit",
        align="center",
        font=("Arial", 24, "bold")
    )

# --- WAIT HERE until SPACE or Q ---
while not game_running:
    screen.update()

try:
    while not game_over:

        if message_timer > 0:                           #- update message timer
            message_timer -= 0.005
            if message_timer <= 0:
                message.clear()


        check_paddle_collision(ball, paddle)            #- hitting the paddle

        if check_block_collision(ball, block_dic):      #- hitting the blocks 
            draw_blocks()
            if all(not b["alive"] for b in block_dic):  #- if all blocks cleared
                show_message("Done!", duration=1.5)

                message.clear()
                message.write(
                    "Press SPACE to start\nPress Q to quit",
                    align="center",
                    font=("Arial", 24, "bold")
                )

                game_running = False

                while not game_running:
                    screen.update()

                ball.reset()
                paddle.reset()
                for b in block_dic:
                    b["alive"] = True
                draw_blocks()

                continue

                

        result = check_wall_collision(ball)             #- bouncing off the wall
        if result == "miss":
            ball.reset()        # put ball back at center
            show_message("Miss!")
            screen.update()
            time.sleep(1)       # pause for a moment
            continue            # skip the rest of the loop this frame

        screen.update()                                 #- updating the screen 

        try:                                            #- stopping Turtle class from freaking out 
            ball.move()                                 #- then moving the ball
        except (turtle.Terminator, tkinter.TclError):           #- hopefully a clean exit from Turtle screen 
            break

        time.sleep(0.005)                               #- slowing the ball down

except turtle.Terminator:
    pass




