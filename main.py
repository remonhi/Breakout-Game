
import breakout    #! starting with the pong game, but slowly transformed 
import lib         #* my own library of "stuff" 
import time        #- for time function
import art         #- for ASCII art
import turtle      #- for turtle (the old Tcl/Tk) graphics
import time        #- for time functions
import random      #- for random number generation
import os          #- for OS commands to clear the screen


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
        x = self.xcor() - self.base
        y = self.ycor()
        left_limit = -(self.screen_width / 2) + self.length/2
        x = max(x, left_limit) # okay, never more than left limit  
        self.goto(x, y)

    def right(self):
        print("RIGHT")
        x = self.xcor() + self.base
        y = self.ycor()
        right_limit = (self.screen_width / 2) - self.length/2
        x = min(x, right_limit)
        self.goto(x, y)


def draw_blocks():
    blocks.clear()
    for b in block_dic:
        if b["alive"]:
            # Move to top-left corner of the block
            blocks.goto(b["x"] - block_width/2, b["y"] + block_height/2)
            blocks.color(b["color"])
            blocks.begin_fill()
            for _ in range(2):
                blocks.forward(block_width)
                blocks.right(90)
                blocks.forward(block_height)
                blocks.right(90)
            blocks.end_fill()




def quit_app():
    global game_over
    game_over = True
    screen.bye()   #- closes the window

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

paddle = Paddle((0,0 - H/2 + C *2)) #? starting at bottom of screen, the C is the default Turtle size 

#- the Blocks

blocks = turtle.Turtle()
blocks.hideturtle()
blocks.penup()
blocks.speed("fastest")

block_width = 100                           # don't know why I love this size
block_height = 20
block_gap = 2                               # a little gap, but might change this later
block_unit = block_width + block_gap        # yeah, working in the gap
block_row = int(W/block_unit)               # how many blocks can fit on a row based on screen width
block_x = (                                 # making sure row of blocks is centered  
    -((block_row * block_unit) / 2) + (block_width / 2))
block_y = 200

block_dic = []   
for i in range(block_row):
    x = int(block_x + i * block_unit)
    block_dic.append(
        {
            "x": x,
            "y": block_y,
            "color": "cyan",
            "alive": True
        }
    )
    print(
        f"dictionary item: ({x},{block_y}), "
        f"color: {block_dic[i]['color']}, "
        f"alive: {block_dic[i]['alive']}"
    )


draw_blocks()




#- the Ball

#- the Scoreboard

#- getting things moving 

screen.update()  #- update the screen because tracer turned off the animation
screen.listen()  #- this is essential for reading from the keyboard 

screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")
screen.onkey(quit_app, "q")
screen.onkey(quit_app, "Q")


#ball.setheading(random.randint(0, 360)) #! - pick a random direction 
#ball.setheading(10)                     # 
#ball.goto(0, 0)

try: 
    while not game_over:
        #! managing the paddle position
        if paddle.xcor() >= W/2:
            #- move then, move left
            paddle.left
            print("off the screen")
        # #- bound off top and bottom
        # if ball.ycor() >= (H/2) or ball.ycor() <= (-H/2):
        #     ball.bounce_wall()
        #     print("bounce off the wall")

        # #- bounce off paddle if not pass the paddle 
        # if ball.distance(right_paddle) < 50 and ball.xcor() > (H/2-C) or ball.distance(left_paddle) < 50 and ball.xcor() < -(H/2-C):
        #     ball.bounce_paddle()
        #     print("bounce off the paddle")

        # #- miss by player and start moving in the opposite direction
        # if ball.xcor() >= (W/2) or ball.xcor() <= (-W/2):
        #     if ball.xcor() >= (W/2):
        #         scoreboard.left_score += 1
        #         scoreboard.board_update()
        #     elif ball.xcor() <= (-W/2):
        #         scoreboard.right_score += 1
        #         scoreboard.board_update()

        #     #! reset the ball 
        #     ball.goto(0, 0)
        #     ball.setheading(180 - ball.heading())
        #     screen.update()
        #     time.sleep(3)
        #     print("reset after miss by player")

        # ball.move() #- keep the game going 
        # time.sleep(0.01) #! so I can see the ball 
        screen.update() #- fun with Turtle 

except turtle.Terminator:
    pass #- clean exit with no traceback 

