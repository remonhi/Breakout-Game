# - Yellow -  Information with a general, but relative importance
# ? Orange -  Examples, abbreviations, acronyms, or explanations
# + Green -  Key words, proper nouns, dates, symbols or mathematical formulas
# ~ Blue -  Definitions of key words, or tabular data
# ! Pink - Important, relative to a test or my career
# * Purple -  Personal interest
# // Gray - Done

# - establishing variables, immporting modules and setting up functions

import os         # - for OS commands to clear the screen
import random     # - for random number generation
import time       # - for time functions
import turtle     # - for turtle (the old Tcl/Tk) graphics
import art        # - for ASCII art
import time       # - for time funcdtions


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


def clear_screen():
    if os.name == 'nt':  # 'nt' stands for Windows
        os.system('cls')
    else:  # For macOS and Linux (posix-based systems)
        os.system('clear')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# - define a class named Paddle

L = 20
W = 100
B = 20


class Paddle(turtle.Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=L/B, stretch_wid=W/B)
        self.color("white")
        self.speed("fastest")
        self.goto(coordinates[0], coordinates[1])

    def up(self):
        print("UP")
        x = self.xcor()
        y = self.ycor() + B*2
        self.goto(x, y)

    def down(self):
        print("DOWN")
        x = self.xcor()
        y = self.ycor() - B*2
        self.goto(x, y)


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
