# Allen's Blog
The following documents the work and progress done by Allen.

[This](https://github.com/wendahere/JAWS#jaws) is the link to the group blog.

## Week 1 (14/9/19 - 21/9/19):
This is the first week of our engineering realization module. 

We were introduced to what our project was which is by the end of the semester. we are to build a track vehicle that executes a specific task. We also formed groups of 4. In my group, 2 of us (Wen Da and I) are from the mechanical background, while the remaining two are from electrical background.

In our first group discussion, we discussed what kind of task will our track vehicle execute, and what kind of features it will have. Details of the discussion can be found [here](https://github.com/wendahere/JAWS#week-1-141019---181019).

## Week 2 (21/9/19 - 27/9/19):
### Coding with BBC micro:bit

![microbit_front]() ![microbit_back]()

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

## Week 3 (28/10/19 - 4/11/19):
This week we were taught the history of track vehicles, its development throughout the years, and its wide variety of applications.

Furthermore we also [assembled](https://github.com/wendahere/JAWS/blob/master/README.md#assembly) the T100 continous track vehicle which wil be used for learning and prototyping.

### Individual Assignment
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

## Week 4 (4/11/19 - 10/11/19):
Today we received the ESP32 board. 

![esp32_front]() ![esp32_back]()

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

## Week 5 (11/11/19 - 17/11/19):
This week Mr Rhodney talked about how we can use our ESP32, introduce us to the inputs and outputs. And provided us with useful  youtube links to watch over the coming weeks, so that we can code the required features of our track vehicle into our ESP32 and make everthing work together.

[Link 1.](https://www.youtube.com/channel/UCp2rS5TxRt6W8fieAk74bIw)
[Link 2.](https://www.youtube.com/results?search_query=just+enough+python)
[Link 3.](https://www.youtube.com/results?search_query=andreas+spies+esp32+tank)

## Week 6 (18/11/19 - 24/11/19):
### Fusion 360
This week Mr Tune went through with us the basics of fusion such as modelling and the assembly of different parts/components. These 3D CAD skills that he went through are essential to our project, which I will be using it extensively in the coming weeks as the main mechanical design engineer for my group.

#### Assignment
Furthermore, we were tasked with the assignment of going through this [youtube link](https://www.youtube.com/user/thang010146/videos) to pick out at least 1 design and redesign it with the required linkages, so that when a user moves one piece of the component, all connected moving pieces will move together as well.

![Imgur](https://i.imgur.com/DzoY68i.png)

This is a model of a compass.

![Imgur](https://i.imgur.com/ha14dpp.png)

This is a model of a 8 bar linkage.

## Week 7 (25/11/19 - 1/12/19):
This week Mr Rhodney talked about power, the ways we can provide power to our track vehicle, as it is not just connecting batteries to a couple motors. In addition, he went through with us how to charge our track vehicles using modules such as the TP4056 charging module.

## Week 8 (2/12/19 - 8/12/19):
### MST Week
This week was our mid-semester, as such I took a short hiatus from doing the project to focus during on my studies.

## Week 9 - 13 (9/12/19 - 12/1/20):
### Holiday Week
During the Holidays We went met up a couple times to decide how are we going to go about our project. What are the main things we should focus on, how are we going to design, what are the components, how will the eventual vehicle look like.

## Week 15 (20/1/20 - 26/1/20):
### Tank Chasis Modeling
I started work on modelling the tank chasis as Mr Tune tasked us to do that during this week. Using vernier calipers I measured every single dimension that is essential to the actual model, then noted them down. 

After measuring the dimensions that I need, I drew the model on Fusion 360. 

![Imgur](https://i.imgur.com/4SRlHNf.png)

Here is the finished design of the tank chasis.

Also, a big shoutout to Reynard who provided me with the CAD model of the very well detailed model of the tank tracks.

![Imgur](https://i.imgur.com/sR5b1t0.png)

## Week 16 - 18 (27/1/20 - 16/2/20):
### Modeling of the main part of our vehicle
After I finished the modelling the tank chasis, it is now time to model the main part of our vehicle, which is the box that will house all the electronics and any other mechanisms that we need. All of the electronic models are taken courtesy of the wonderful GrabCAD community, [link here](https://grabcad.com/). 

![Imgur](https://i.imgur.com/Bj4RWWg.png)

All the components above here you see are all taken from GrabCAD, but modified with fasterners that will be used as attachment to our final assembly model in Fusion 360.

#### Vision of the design
We do not only want our components neatly stored and organised in a box, but also separated into visible clusters, as it will make troubleshooting easier.

![Imgur](https://i.imgur.com/JeBiFTw.png)

As you can see here, this is a fully modelled assemly of our box design in Fusion 360. And you can see that we have 3 compartments. From the left, we have the mechanism compartment, which raises and lowers our ultrasonic transducer using a pulley system powered by a servo motor. Then in the middle, we have our components compartment, which houses the ESP32, L298N motor driver, OLED and more. And lastly in the right, we have our power compartment, with the switches, batteries and charging module. Then all the blank spaces you see here are basically spaces where our wires will run through.

#### Box
For the box itself, I decided to go for an transparent acrylic box shape.

The reason for it because:
1) The panels can be laser cut individually, allowing small incremental changes to certain sides of the box to be easier, as I do not need to reprint an entire box if we 3D printed it.
2) Lesser time to manufacture the box, as laser cutting is relatively fast.
3) It provides an ease of assemblying as we can just slot in the different panels together

![Imgur](https://i.imgur.com/B4bGttR.png)

So this is the final design of the different panels that will make up our component box.

![Imgur](https://i.imgur.com/HER7HOP.png)

Here is the assembled version of the box without any components.

![Imgur](https://i.imgur.com/8wURor8.png)
![Imgur](https://i.imgur.com/u5OgcCU.png)

Here are the assembled version of the box with the components.

##### Problems
During the first assembly of the box I realized that the slots i made for the box were too thin (2mm) and it resulted in many breakages. 

![Imgur](https://i.imgur.com/UANbdtG.jpg)

![Imgur](https://i.imgur.com/kUN7c0Z.png)

The slot is just too thin to handle the amount of stress that were induced during assembly.

So to solve it, I added 1mm, and made them 3mm thick. And that extra millimeter was enough to handle the job.

![Imgur](https://i.imgur.com/yvbGpd0.jpg)

New(3mm) slot (top), Old(2mm) slot (bottom)


Another issue I faced was the width of the box is too small, making it very compact, and unfortunately hard to fit in all our wires within the box. Sean pointed out this problem, when he did his first testing of the wires.

Therefore, I increased the width of the bottom panel so that there is for space for the wires and our fingers and tools to slot in the wires.

![Imgur](https://i.imgur.com/cM8Ymga.jpg)

Narrower box panel (left), Wider box panel (right)

#### Electrical Component Holder
As Sean and I wanted our circuit to be compact and neatly organised and contained in the box. I made some holder designs for our electrical components such as the TP4056 charging module, the MT3608 boost converter and a switch. And all these will be housed in the power compartment of the box.

![Imgur](https://i.imgur.com/b08WVLa.png)

Here are the modules which we will be keeing in our power compartment.

![Imgur](https://i.imgur.com/Rkk5KSn.png)
![Imgur](https://i.imgur.com/OHE6X8L.png)
![Imgur](https://i.imgur.com/tefjrZP.png)

The above are 3D models of the different component holders for the aforementoned components.

#### Mechanism
As our vehicle's purpose is to measure the depth of ice, we need a way to lower our sensor so that it can measure the depth of a medium. Before I modelled out the design, I sketched out with a couple designs. The purpose of our mechanism is to raise and lower the sensor, and maintain it flat and parallel to the ground when it is measuring.

##### Design 1
_Rack and pinion design_
![Imgur](https://i.imgur.com/3IwSfCY.jpg)

This design seems fine, but I was worried about the friction the gears will generate and also what if there was something wrong with our code and as such when lowering the sensor it lowers too much causing it to crash onto a rough ground surface hence damaging the sensor.

![Imgur](https://i.imgur.com/qGg0zQn.jpg)

This is a dirty prototype I made to help visualise how the rack and pinion design will actually look like, and from there I also forsaw a problem of tight tolerances that was needed for the gears to work smoothly without rubbing on the side panels.

##### Design 2
_Using linkages_
![Imgur](https://i.imgur.com/y6QQ3lR.jpg)
![Imgur](https://i.imgur.com/U8hNCnL.jpg)

We didn't use this design as there isn't much space to put in the mechcanical arm that holds the sensor.

##### Design 3 (Chosen)
Pulley system
![Imgur](https://i.imgur.com/PxODLd2.jpg)

This is the design that we was chosen because the string has the least friction generated when lowering our raising the sensor, and in the event of a malfunction of the motor, it wouldn't cause the sensor to crash onto the ground and as such damage it.

So with the concept in mind, I just needed to design 3 things, a holder for the sensor, a guide for the sensor to go down and up, and a pulley that will be connected to a stepper motor and to house the string.

![Imgur](https://i.imgur.com/EUjZZqD.png)

So this is the pulley that I had designed which will be used to attached to the following 360 stepper motor (SM-S4315R).

![Imgur](https://i.imgur.com/un279D3.png)

![Imgur](https://i.imgur.com/MDU8OxB.png)

This is the guide, that will guide the sensor back up and down, and as you can see the bottom is in a somewhat conical shape so that when the sensor is swaying around will being raised up, it helps to guide the sensor up into the cylinder housing.

![Imgur](https://i.imgur.com/tRAJowU.jpg)

Something to note is, the original design did not have a cylinder housing, as seen above, because during testing I found ou that when being lowered, the sensor does not really go down perpendicularly, and since we need the sensor to be flat to the ground, that might cause an issue. 

To solve this, I added the cylinder housing up top to help guide the sensor straight down.

![Imgur](https://i.imgur.com/WMUWrXB.jpg)

_Old guide (left), New guide (right)_

![Imgur](https://i.imgur.com/rROCjPV.png)
To hold our sensor, so that it can slide down the guide smoothly, I made a casing for it as seen above. 

This is also because the sensor itself is not a perfect cylinder as there are parts sticking out as shown below.

[Imgur](https://i.imgur.com/VoJivzV.png)

_Our ultrasonic transducer_

![Imgur](https://i.imgur.com/pg6bOcY.png)

_Assembly of the pulley system_

![Imgur](https://i.imgur.com/VKnaGeO.mp4)

_How the pulley system works_

#### Final Design in Fusion 360
After touching up the any

![Imgur](https://i.imgur.com/jy24wl7.png)

Here is a fully rendered image of our vehicle in Fusion 360 (also rendered there).

### Fabrication of Parts
With designs modelled in fusion 360, I proceeded to fabricate the parts so that we can test and make any necessary changes along the way. The evolution of the different parts have been talked before.

### Reflections
Should have made a dirty prototype first bla bla

### Mechanical Calculation
Using the knowledge gained from week 3, I calculated the required torque of our tracker vehicle in order to determine if the provided motors were able to output the torque required.

Furthermore taking into consideration of other factors such as human walking speed, dynamic friction of ice, and many other factors, I calculated wheel torque of our vehicle. And I am proud to say that our vehicle in the most perfect condition, will be able to traverse on ice without any issues. [Link here]() for the mechanical calculations. 

## Week 19 (17/2/20 - 23/2/20):
### Final Assembly
This week is our last week which we will be doing our project. So we were doing our final touches to the vehicle.

!

Here is the final assembly of our track vehicle.

### Presentation

[Link]() to our presentation slides.
