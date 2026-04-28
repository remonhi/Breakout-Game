
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

# - Module 162 | Creating and moving the right paddle
# - Module 163 | Cleaning up class and creating left paddle
# - Module 164 | Adding the ball
# - Module 165 | Detecting collision with the wall
# - Module 166 | Detecting collision with the paddle

game_over = False

paddle = breakout.Paddle((0,0 - H/2 + breakout.B *2), W) #? starting at bottom of screen, the B is the default Turtle size 
#ball = breakout.Ball()
#scoreboard = breakout.Scoreboard()

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

