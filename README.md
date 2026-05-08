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

    2. Turtle Review - So, in some way glad not be working with Tkinter; however, the Turtle() library is not the most fun in the world.  Also, as I thought about the design my research lead me to the appraoch there only need to be 3 Turtle() instances...the paddle, the ball and the blocks.  My original idea was to make a Turtle instance for each little piece of block; however, apparently that would be a problem for the refresh. So, it is easier just to refresh one "giant" turle.  
 
    3. Previous Work - As the assignemnt suggested, I wanted to go back to Day 22.  Well, this was about a "relative" of Breakout and that is Pong.  Well, my approqach to writing and organizing my code is a bit different now.  Anyway, I decided to "migrate" Pong from May of 2025 to March of 2026.

        Saved 168.py as main.py
        
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
                - Before starting module, find an test external monitor setup
                - Then, life interrupted.


### 4/22/26-4/23/26, Getting Back

Okay, life interrupted and 

1. Python Update - Well, looks like last update with Python was using HomeBrew.  So, I ran...

    brew update
    brew update python

    ...and after udpated finished, I noted the status indicated all the symbomlic links updated.  I confirmed version with 'python --version.' ✅

2. VS Code Update - After opening, this seemed to be at version 1.113.0.  After checking for update, looking at version 1.117.0. ✅

3. OneDrive Sync - Yes, marked all directories as 'Always Keep on This Device.'  Then, found myself waiting all night for sync. Even in the next day, this was a probem.  It seems that the OneDrive applciaton crashed.  After a couple restarts, it seems that 'Day 87' was ready; however, there were many more files being downloaded.  ✅

4. Refreshing environment - 

    a. Confirm sync with GitHub - I was first thinking of pulling from GitHub, but realized this was updated at last stoppign point.  So, at this moment just wanted to make sure GitHub sync was still working.  Well, this just seemed to hang but I think this might be related to the issues with OneDrive.  Yes, that is definitely the problem; therefore, I just had to wait overnight to have the directory sync.  Yes, on Thursday finally got this thing working. ✅

    b. Setup virtual enviroment - source venv/bin/activate ✅

    c. See what is currently working - python main.py, and yes the "broken" Pong game started. ✅

5. Attack Plan 

    a. Refresh knowledge - Yeah, to reduce my dependance on AI decided to rerun 'Day 22'

        Module 160 - 
            - This was just an overview, so took time to just clean up the code.  
            - BTW, gonna with with my "own stuff" in lib.py, but might rename. 
            - Then, wasted a lot of time tweaking the Better Comments code for a better yelllow highlight

        Module 161 - 
            - Yeah, some more clean up of my code to match my conventin.  
            - Then, just a quick run though to refresh on how to setup a screen.

        Module 162 - 
            - This was to create the right paddle, so going in to pong.py file/module.  
            - Interesting tidbit that all turtles start off at 20 x 20
            - Look at this module, intersting that my code has created a Paddle class.
            - Also, .tracer() and .listen() important for Turtle; however, don't plan on using this everyday

        Module 163 - 
            - Hmmm, just watched video and looked at my code.
            - I ran the code and everyhing was stuck, so decided figure it out. 
            - I go it all cleaned up and then decided this needed a proper quit (just using "q")
            - Did not like traceback on exit, so got help to clean up . 
            - This was a good refresher on how my code got this way
            
        Module 164 - 
            - Well, had a little more time to kill today so I continued to work on this.
            - Hmmm, my code used .forward() versus the move() created in the module
            - With some help, .forward() just help to move in direction it is already going
            - Don't know how I ended up using .forward()

        Module 165 -
            - Okay, I had put in some much different "bouncing" math into my code
            - Did not drive myself crazy with "refactoring" the math        

        Module 166 -
            - Again, my own math here
            - Cleaned up the loop and got it working again

        Module 167 -
            - Ditto, my own code here
            - Just worked on cleaning up code.

        Module 168 - 
            - Ditto, my own code here
            - Just worked on cleaning up code.

        Module 169
            - Copy pong.py to breakout.py
            - Copied main.py to main-pong.py
            - Cleaned up main.py breakout.py
            - Then, problems with pushing to GitHub



### 4/23/26-5/7/26, Coding Time 

1. Main screen - Create the main screen

    a. First address OneDrive issues
        - Confirm able to push my 'Day 87' code to GitHub ✅
        - For now, just move 'Day 87' into Documents/Python-Local/ → mv 'Day 87' $HOME/Documents/Python-Local/ ✅
        - Wait for OneDrive sync to finish, and the move entire Python "tree" over to Documents - ✅
            i. Well, this was another rabbit hole
            ii. Had to get some help to stop entire Python directory from trying to download 
            iii. Seem that a larger 'Always Keep on this Device' causes OneDrive to crash
            iv. I think it is BS now that MS has all my data, so just need to think about how we move forward
            v. 
        - Last, setup rsync for a backup to OneDrive
        - Finally, moving forward with everything in a "local" file system
        - 
    
        ...shit, it is really hard getting time to code.   Also, still fighting with OneDrive; however, got the code for my current project moved and "local."  I cleaned up and verified it still worked.  

    b. Main screen 📺✅
        - Yeah, I started with my "leftovers" from my Pong project.
        - For some reason thought original breakout was portrait, but also landscape so updated screen to W=800 & H=600
    
2. The paddle ✅
    a. Hmmm, I almost pulled a "vibe coding" approach and geting the code from AI; however, dicided to hack my old code.
    b. I began with Paddle class that was in breakout.py
    c. I mangaed to create a paddle, but then realized it needed to be moved to a differnet location on the screen and a few other challenges...
       i. Move to "bottom" of screen. ✔️
       ii. Stop from running off the screen - 
            - Yeah, I decided this works best in the while loop
            - Again, I tried to attack this with my own brain 
            - This was not working, so got help and decided to pass the screen_width to Paddle class
            - RAN OUT OF TIME for 4/27
            - On 4/28, continue to clean this up & also looked to address moving all my code over 
            - I got it work and then went down rabbit hole about Turtle shapes and screen coordiantes. 
    d. Hmmm, when down a rabbit hole away from key board and decided to pull the classes into the main.
    e. Also, went back to fix the "screen edge" issue using max() and mim() functions for the "limits"
        

3. The "blocks" ✅
    a. Yes, I had to use AI here but as aid (not vibe coding) 🫤
    b. Again, not wanting to become a Turtle module guru; however, wanted to make sure code is in my conventions 🐢
    c. 5/6 - Okay, got the first row created 👍🏾
    d. 5/7 - Work on making just 5 rows of blocks 😎
        - just had to note, this was really fun section
        - I mininzed the use of AI and used my brain to address the columns and colors
        - Used AI for alternative (stampping) to drawing individual bocks

4. The ball ✅
    a. 5/7 - Create the ball and get it moving
        - Again, I decided to "hack" my old Pong code and not use AI
        - Then, I got help with...
            • paddle collision 💥
            • block collision 💥
        - The ball was moving way too fast, added time delay in loop. 🐇
        - Then, was getting a weird exit error (fun with Turtle). 🐢
        - Last, randomized the start of the ball. 

4. Keeping score ✅
    - Yeah, I feel like lessons have been learned with this project
    - For the sake of this class, I am skipping this for now
    - I learned how to keep score in Day 22  
    - However, I would like acknowledge messages
        - Hit!
        - Miss!
        - Done!  





5/7/26, Wrapping Up

1. Testing
    a. Noted sticky paddle, so updated from onkey() to onkeyress. 👍🏾
    b. Seems like I missed but ball bounces, had to change order  of check_paddle_collision() and ball.move()👍🏾
    c. Had some weird errors with quiting, that turned out to be Turtle quirks 👍🏾

2. Documentation - N/A ❌

3. Lesson... 😎

    Whew, this project was an example the cliché “lift gets in the way.”  Also, I have just not been crazy about using Turtle as I am more interested in developing data analysis, transformation, etc. type application. Yet, I felt there was some value in developing my coding skills about working through this one.  While life was “getting in the way,” I slowly worked through this project.  Then, once I finally cleared all the issue, I was able to put my head down and wrap this up.   Overall, the basic Python was easy.  The challenge was understanding how the Turtle library worked and “bending” it to my will.  
    So, with that, my approach was…

    1.	Refresh on Turtle knowledge
    2.	Research history of Breakout game
    3.	Layout my attack plan
    4.	Work through any issues
    5.	Test the code
    6.	Wrap it up

    My code is at https://github.com/remonhi/Breakout-Game


4. Push - DONE ✅





 



