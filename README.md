# Day 87 - Breakout Game 

## Course Requirements

Breakout was a hit game originally coded up by Steve Wozniak before he and Jobs started Apple. It's a simple game that is similar to Pong where you use a ball and paddle to break down a wall - https://en.wikipedia.org/wiki/Breakout_(video_game).  You can try out the gameplay here:
https://elgoog.im/breakout/.  A good starting point is to review the lessons on Day 22 when we built the Pong game. But you will have plenty of things to Google, figure out and struggle through to complete this project. Try to avoid going to a tutorial on how to build breakout, instead spec out the project, figure out how it's going to work. Write down a checklist of todos and draw out a flow chart (if it helps).

## Development Notes

### 3/20/26, Getting Organized ✅

Today, I set out with two objectives.  First, get outline all the GUI project to get them "off my mind."  Second, organize myself for Day 87 project.  From looking though the Udemy courseware, the remaining GUI projects are...

Day 87 - Breakout Game
Day 90 - Disappearing Text Writing App
Day 92 - Image Colour Palette Generator
Day 94 - Automate the Google Dinosaur Game
Day 95 - Space Invaders

...whew, that still is a lot.

Alright, for the 'Breakout Game.'

    Copied over from previous project → cp -R 'Day 86' 'Day 87' ✔️
    Removed old virtual environment → rm -rf venv ✔️
    Removed the old git tracking → rm -rf .git ✔️
    Initialized the virtual environment → python -m venv venv ✔️
    Activated the virtual environment → source venv/bin/activate ✔️
    Initlaized a new repo → 
        git init
        git add .
        git commit -m "initial commit"
    Noted old Git Ignore still there → cat .gitignore ✔️
    Set branch name → git branch -M main ✔️
    Created new repo at Gig Hub → https://github.com/remonhi/Breakout-Game ✔️
    Connected to net repo → git remote add origin git@github.com:remonhi/Breakout-Game.git
    Pushed update → git push -u origin main 

    ...to wrap up day, laid out high level plans...

        1. Game History - Review at the page https://en.wikipedia.org/wiki/Breakout_(video_game)
        2. Game Play - https://elgoog.im/breakout/
        3. Previous Work - Check out lecture and my code from Day 22
        4. My Ideas - Layout my appraoch to this game.


### 3/25/26-, Refreshing Knowledge 

    1. Game History - Okay, from https://en.wikipedia.org/wiki/Breakout_(video_game) I learned a lot about this game.  I did not realize the envolvement from Apple founders.  Most of the challenges "back in the day" was about the right hardwware.  It is interesting that "these days" hardware is hardly a limtation.  

    2. Turtle Review - So, in some way glad not be workign with Tkinter; however, the Turtle() library is not the most fun in the world.  Also, as I thought about the design my research lead me to the appraoch there only need to be 3 Turle() instances...the paddle, the ball and the blocks.  My original idea was to make a Turtle instance for each little piece of block; however, apparently that would be a problem for the refresh. So, it is easier just to refresh one "giant" turle.  
 
    3. Previous Work - As the assignemnt suggested, I wanted to go back to Day 22.  Well, this was about a "relative" of Breakout and that is Pong.  Well, my approqach to writing and organizing my code is a bit different now.  Anyway, I decided to "migrate" Pong from May of 2025 to March of 2026.

        Saved 168.67 as main.py
        
        Also, saved pong.py in to current directory
        
        Just ran main.py to see what errors came back
            - Had to install the art module 
            - Restarted, and now the ball just shoots across the screen
            - Well, I had two options figure it out or get help from "the robot"
            - I looked at the code for a while and was stuck
            - Yet, to figure it out without AI I thought the best approach was go to through Day 22 again
        
        Refreshing the lesson

            - Day 160
                - Well, first the "classroom" would not show video
                - I ran through all the troubeshooting and seemed 
                - Then, I got into a rut where the video would not display wih Safari
                - Eventually, I had to run this with Chrome
                - I completed the overview, and then decided to get this woring on my laptop.
                    - Saved here
                    - Created requirements.txt file 
                    - Validated the latest sync for OneDrive
                    - Then, worked on installing Chrome and got logged into Udemdy 
                    - Last, sourced the environment and go the game running...interestingly it worked, but was too hard to play along
                    - Still, I want to review it all as a fresher.  


            - Day 161 



    5. Attack Plan 

        a. Create the main screen
        b. Make a paddle
        c. Make the ball
        d. Make the "blocks
        e. Make the ball move

    

        





### TBD, Wrapping Up

1. Testing
2. Documentation
3. Lesson
4. Push





 



