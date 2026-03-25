import pong        # - for the pong game
import time        # - for time function
import art         # - for ASCII art
import turtle      # - for turtle (the old Tcl/Tk) graphics
import time        # - for time functions
import random      # - for random number generation
import os          # - for OS commands to clear the screen

# - Yellow -  Information with a general, but relative importance
# ? Orange -  Examples, abbreviations, acronyms, or explanations
# + Green -  Key words, proper nouns, dates, symbols or mathematical formulas
# ~ Blue -  Definitions of key words, or tabular data
# ! Pink - Important, relative to a test or my career
# * Purple -  Personal interest
# // Gray - Done

# - establishing variables, immporting modules and setting up functions

W = 800
H = 600
C = 20


def clear_screen():
    if os.name == 'nt':  # 'nt' stands for Windows
        os.system('cls')
    else:  # For macOS and Linux (posix-based systems)
        os.system('clear')


# - the MAIN program

clear_screen()  # - text based
day = "Breakout"
nam = os.path.basename(__file__)
nam = nam.replace(".py", "")
day = day + " - " + nam
print(art.text2art(day, font='medium'))

# - Module 161 | Setting up the screen

screen = turtle.Screen()
screen.setup(width=W, height=H)
screen.bgcolor("black")
screen.title(day)
screen.tracer(0)  # - turning off the annimation

# - Module 162 | Creating and moving the right paddle
# - Module 163 | Cleaning up class and creating left paddle
# - Module 164 | Adding the ball
# - Module 165 | Detecting collision with the wall
# - Module 166 | Detecting collision with the paddle


game_over = False

right_paddle = pong.Paddle((350, 0))
left_paddle = pong.Paddle((-350, 0))
ball = pong.Ball()
scoreboard = pong.Scoreboard()


screen.update()  # - update the screen because tracer turned off the animation
screen.listen()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

ball.setheading(random.randint(0, 360))
ball.setheading(10)


ball.goto(0, 0)
while game_over == False:
    # - bound off top and bottom
    if ball.ycor() >= (H/2) or ball.ycor() <= (-H/2):
        ball.bounce_wall()
        print("bounce off the wall")

    # - bounce off paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > (H/2-C) or ball.distance(left_paddle) < 50 and ball.xcor() < -(H/2-C):
        ball.bounce_paddle()
        print("bounce off the paddle")

    # - miss by player and start moving in the opposite direction
    if ball.xcor() >= (W/2) or ball.xcor() <= (-W/2):
        if ball.xcor() >= (W/2):
            scoreboard.left_score += 1
            scoreboard.board_update()
        elif ball.xcor() <= (-W/2):
            scoreboard.right_score += 1
            scoreboard.board_update()

        ball.goto(0, 0)
        ball.setheading(180 - ball.heading())
        screen.update()
        time.sleep(3)
        print("reset after miss by player")

    ball.move()

    screen.update()


screen.exitonclick()
