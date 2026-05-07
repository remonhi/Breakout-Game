# pong.py

#- Yellow -  Information with a general, but relative importance
#? Orange -  Examples, abbreviations, acronyms, or explanations
#+ Green -  Key words, proper nouns, dates, symbols or mathematical formulas
#~ Blue -  Definitions of key words, or tabular data
#! Pink - Important, relative to a test or my career
#* Purple -  Personal interest
# // Gray - Done

# - establishing variables, immporting modules and setting up functions

import os         #- for OS commands to clear the screen
import random     #- for random number generation
import time       #- for time functions
import turtle     #- for turtle (the old Tcl/Tk) graphics
import art        #- for ASCII art
import time       #- for time funcdtions

turtle_colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan",
    "magenta", "brown", "black", "white", "gray", "gold", "silver",
    "darkblue", "lightgreen", "tomato", "lavender", "peachpuff",
    "deepskyblue", "forestgreen", "lightsalmon"
]

UP = 90                           # - up direction
DOWN = 270                        # - down direction
LEFT = 180                        # - left direction
RIGHT = 0                         # - right direction
ALIGN = "center"                  # - center the text
FONT = ("Courier", 80, "normal")  # - font for the text

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)




class Block(turtle.Turtle):
    def __init__(self, x, y, color="white"):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=W/B, stretch_wid=L/B)
        self.color(color)
        self.speed("fastest")
        self.goto(x, y)
        self.length = L
        self.height = W
        self.half_width = L / 2
        self.half_height = W / 2

    def hit(self):
        self.hideturtle()
        self.goto(2000, 2000)   # move off-screen







class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("normal")
        self.penup()
        self.shapesize(stretch_len=B/20, stretch_wid=B/20)
        self.color("white")
        self.speed("fastest")

    def move(self):
        self.forward(B/2)

    def bounce_wall(self):
        self.setheading(360 - self.heading())

    def bounce_paddle(self):
        self.setheading(180 - self.heading())


class Scoreboard(turtle.Turtle):
    # ? Constructor method to initialize attributes
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.board_update()

    def board_update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.left_score} ", align=ALIGN,
                   font=FONT)
        self.goto(100, 200)
        self.write(f"{self.right_score} ", align=ALIGN,
                   font=FONT)
