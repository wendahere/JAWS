# Allen's Blog
## Week 1 (14/9/19 - 19/9/19):
This is the first week of our engineering realization module. 

We were introduced to what our project was which is by the end of the semester. we are to build a track vehicle that executes a specific task. We also formed groups of 4. In my group, 2 of us (Wen Da and I) are from the mechanical background, while the remaining two are from electrical background.

In our first group discussion, we discussed what kind of task will our track vehicle execute, and what kind of features it will have. Details of the discussion can be found [here](https://github.com/wendahere/JAWS#week-1-141019---181019).

## Week 2 (21/9/19 - 25/9/19):
### Coding with BBC micro:bit
This week we learnt how to code python using the BBC micro:bit. Our homework is to code a space invaders game.
After several trials and errors, I managed to come up with a working code for the game. The below is the code for the game.

    from microbit import  *
    import random
    
    #spacecraft is originally in the middle of screen
    spacecraft_x = 2
    
    # alien randomly starts at the top
    alien_x = random.randint(0,4)
    alien_y = 0
    
    while True:
      # draw the display
      display.clear()
      display.set_pixel(spacecraft_x, 4, 5)
      display.set_pixel(alien_x, alien_y, 9)
      
      # drop the alien on each turn
      alien_y = alien_y + 1
      
      # use buttons to move the spacecraft
      if button_a.is_pressed():
        # move left
        spacecraft_x = spacecraft_x - 1
       if button_b.is_pressed():
        # move right
        spacecraft_x = spacecraft_x + 1
        
       if alien_y == 5:
        # alien reaches the end but no collision
        alien_x = random.randint(0,4)
        alien_y = 0
        display.set_pixel(alien_x, alien_y, 9)
        alien_y = alien_y + 1
        sleep(250)
        
       if alien_x == spacecraft_x and alien_y == 4:
        # collision happens
        break
        
       # some delay to view the screen
       sleep(250)
       
    # End the game
    display.scroll("GAME OVER!", loop = True)
    
This is a small preview on how the game works. The "alien" drops from the first line on top, the player's game is to maneuver the spacecraft at the bottom by either going left and right by pressing the respective buttons to evade the alien. The game ends once the alien collides with the spacecraft.
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/T7CeutXWiZE/0.jpg)](http://www.youtube.com/watch?v=T7CeutXWiZEE)

As previosuly mentioned, I didn't get the code correctly the first time, it was only after I meticulously rechecked my code, I realised what went wrong.

The first problem was I forgot to add in the colon signs after my If statements.
![alt text](https://imgur.com/WMcqX5b.png)

To fix this, I simply added the colon signs where necessary (i.e. Lines 13 and 16).

The second problem was after running the program, when the "alien" doesn't hit my spacecraft and goes out of bounds, the game doesn't "reset", and everything just froze. An example of this problem is this video below.
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/hX4ReSyuBTU/0.jpg)](http://www.youtube.com/watch?v=hX4ReSyuBTU)

This is the first version of the code that the second problem came from.
![alt text](https://i.imgur.com/rwFM5x2.png)

As you can see, there is no code that "resets" the game when the "alien" goes out of bounds.

To fix this, I added several new lines of codes to allow the game to continue when the "alien" goes out of bounds. Hence, the game will continue to run indefintely until it collides with the spacecraft.
The below is the new lines of codes I introduced.

![alt text](https://imgur.com/p7fK6il.png)

One obstacle that I faced is how the numbering system of LED lights on the BBC micro:bit works. I keep forgetting that it starts counting from 0 instead of 1. Therefore, this made troubleshooting the problems I faced slighty more challenging. In the end, I was able to grasp the basics, and able to come out with new codes to solve the issue of the "alien" going out of bounds causing the game to freeze.

For the readers that are aspiring to take up this mini project, I would like to give you a couple tips on how to code a successful code.
1. Patience. You must be patient while coding. Sometimes, it is better to take a step back and map out a process plan on how you are going to code, rather than typing the code immediately. This way, when you or other people look at your code, it is much more readable and easier to edit.
2. Perserverance. Setbacks are common, do not get discouraged when your code doesn't work out the first time. You must be actively trying to find new solutions on how to solve the problems that get in your way.
3. Curiousity. Having a curious mind is important, because this kind of mindset will help prepare you to face any challenges that might come into your way. Always be hungry for knowledge, you will constantly improve.
I believe that you will be able to do this mini project if you follow this 3 tips.

### Thony IDE
Over the weekend, I have watched a two You-tube videos on Thonny IDE, a platform used to code python. 
Out of the [two videos](https://www.youtube.com/watch?v=lWaCl0WjNZI) I watched, I will reccomend [this one](https://www.youtube.com/watch?v=nwIgxrXP-X4). The person is quite clear in narrating making it easy for people to follow. 
He gives a brief introduction on what Thonny is, and shows us the functions of Thonny with simple demonstrations to not overwhelm beginners. 
All in all, it is a terrific video for beginners to watch to get started on python programming using Thonny.

### Python Programming
I have also watched a video on python programming, and I think that it is quite helpful to beginners. Here is the [link](https://www.youtube.com/watch?v=N4mEzFDjqtA).

Pros:

- Different topics covered in the video is timestamped in the description bar.
- Goes through almost everything a beginner needs to know about python programming.
- Pleasant to watch, narrator is enthusiatic and clear in articulating.

Cons:
- Need to watch the video in order to know what is being taught, cannot open video in background and expect yourself to follow.
- Need to know a little bit of programming (other programming languages) beforehand.

## Week 3 (28/10/19 - 2/11/19):
This week we were taught the history of track vehicles, its development throughout the years, and its wide variety of applications.
### Assignment
A grocery transportation drone is being designed. It will have continuous tracks as the method of propulsion. Only one sprocket axis is powered.

Determine the type of electrical motor(s) to be bought to power it? Budget constraint for motor(s): USD100 in total.

Functional constraint:

- Vmax = as fast as possible but limited only to motor's max rpm
- Acceleration time to Vmax = any number between 1 to 5 seconds (should be unique between students).
- Maximum incline = BCA-approved wheelchair ramp incline (find out and cite source)
- Weight = 1kg + weight of groceries
- Weight of groceries = combined weight of 5-6 randomly choose bulky goods from Redmart or Fairprice's website and cite their individual weights and their combined weight. 
- Graph of Tw vs Acceleration times need to be done in Excel (may need enough points for a best-fit graph), illustrating the range of viable Tw.

This [link](https://docs.google.com/presentation/d/1z6uqKXUzrGAHKOQaMHNoKKfvfchR32ZgUgN2NgdGU30/edit?usp=sharing) is the powerpoint slides where all my calculations, graphs and references can be found. It has been done in powerpoint format for an easy presentation of my assignment.

## Week 4 (4/11/19 - 8/11/19):
Today we received the ESP32 board. 

![Picture of the ESP32]()

We will be using it to do all our Python programming on. Before we do anything, we need to set up the ESP32 by installing micropython in it, so that we can do python programming in the board. Below is a flowchart I followed to set up the ESP32 and to test if it is functioning.

![Picture of Flowchart](https://imgur.com/rRrUc35.png)

Below are the steps that I've use to prepare my ESP32 so that I could do python programming in it using Thonny. I've also referenced [this link](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html).

1. Install latest version of python via [this link](https://www.python.org/downloads/).
1. Make sure that pip is also installed. We need pip to help install epstool.py which we will use to deploy the micropython firmware into the ESP32.
   1. To check, type 'pip feeze' in the command prompt, if pip is installed correctly, it should look like this.
    
          C:\Users\Allen Michael Bautisa Tan>pip freeze
          ecdsa==0.13.3
          esptool==2.8
          pyaes==1.6.1
          pyserial==3.4
          
    1. The first time I typed 'pip freeze', I got some error, and it was most probably because of my python not being installed properly. Below was the error message i got.
    
           'pip freeze' is not recognized as an internal or external command,
           operable program or batch file.
           
    1. To solve this, I unistalled my existing python and all related files, and reinstalled them.
1. Having pip installed, we need to deploy micropython firmware.
    1. I downloaded the micropython firmware from [here](https://micropython.org/download#esp32). The file is [this](https://micropython.org/resources/firmware/esp32-idf3-20191112-v1.11-576-gd667bc642.bin)
    1. Afterwards, I installed esptool.py. Type the following in the command prompt.
    
            pip install esptool
            
    1. Before moving on to the next step, we need to make sure that pip is in the latest version. Type the following in the command prompt. If it is not in the latest version, we need to update it (Which I did it during my installation).
   
            pip -V
            
    1. Erase the flash with the following command.
    
            esptool.py --port /COM5 erase_flash
            
    1. Then deploy the firmware that was just downloaded. 
    
            esptool.py --chip esp32 --port /COM5 write_flash -z 0x1000 esp32-idf3-20191106-v1.11-558-gd209f9ebe.bin
