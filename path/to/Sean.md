# Week 1
Our week 1 documentation is the README.md file if you want to check it out then go ahead
# Week 2
This week my teacher, Mr Dorvile, gave us a task to make a space invaders game in under two hours. Thus, I attempted the challenge and these are the thought I have after the challenge.

If you don't know what am i talking about here is a example of the game [right here](https://www.youtube.com/watch?v=qtPmawMdgQ0)



### Reflections
I did not complete the entire code but I managed to figure out the ship movements.

Here it is below:

	from microbit import *
	# import to the microbit
	
	spacecraft_x = 2
	# get the x-value to the centre of the device

    while True:
        display.clear()
        display.set_pixel(spacecraft_x, 4, 9)
        # display the spaceship dot

        if button_a.is_pressed():
            spacecraft_x = spacecraft_x - 1
            # makes the space ship to move left

        if button_b.is_pressed():
            spacecraft_x = spacecraft_x + 1
            #makes the space ship to move right
            
        sleep(100)
        #To make sure the output display properly
Though my teacher only tasks us with the movement of the space ship and the movement of the aliens which my teammate Allen did correctly [here](https://github.com/wendahere/JAWS/blob/master/allen.md), I didn't complete it in two hours but however in my failure I learnt a few things about coding in python. Here is what I learnt

#### Lesson 1:Include delays(or called sleep in python) into your code

As a beginner coder, I didn't realise how important to put delays are to making your code work. Even the timings for the delays are very important as it can make your code from a not working one to a perfectly functioning one. For example, this image below:
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/hX4ReSyuBTU/0.jpg)
This is would be the output of the microbit for the spaceship if you didn't put the delay for the spaceship and it wouldn't be able to move, which was what i didn't put in the beginning.  This is because the delay allows the microbit to realise that you have pressed the button and will excecute the code to move the spaceship.
 This is because the code runs much fster than you pushing the button. Thus, the microbit not sensing the push of the button.
 That's one of the reasons why you should put the delays in your coding. But be warned, casue the timing of the delays will also affect your output of the code which leads to my second lesson.


#### Lesson 2: Repeated testing for the code to work more efficiently
Going back to the delay example, it had to take multiple tries for me to see which delay timing would make the outout be the most responsive
I had a problem of my programs not working and even though i didn't solve the challenge I realised that if you keep trying you will succeed and also it will make your product better

These are some videos that my friend Allen recommended, here is an execept of my teammates blog

#### Thony IDE
Over the weekend, I have watched a two You-tube videos on Thonny IDE, a platform used to code python. 
Out of the [two videos](https://www.youtube.com/watch?v=lWaCl0WjNZI) I watched, I will reccomend [this one](https://www.youtube.com/watch?v=nwIgxrXP-X4). The person is quite clear in narrating making it easy for people to follow. 
He gives a brief introduction on what Thonny is, and shows us the functions of Thonny with simple demonstrations to not overwhelm beginners. 
All in all, it is a terrific video for beginners to watch to get started on python programming using Thonny.

#### Python Programming
I have also watched a video on python programming, and I think that it is quite helpful to beginners. Here is the [link](https://www.youtube.com/watch?v=N4mEzFDjqtA).

Pros:

- Different topics covered in the video is timestamped in the description bar.
- Goes through almost everything a beginner needs to know about python programming.
- Pleasant to watch, narrator is enthusiatic and clear in articulating.

Cons:
- Need to watch the video in order to know what is being taught, cannot open video in background and expect yourself to follow.
- Need to know a little bit of programming (other programming languages) beforehand.

# Week 3
### Reflections
For this week we learnt about the history of tanks and how they were built. I was a very helpful lesson as I, as a guy that does not know much about mechanical engineering, had no idea how an actual tank actually worked and it was very enlightening to find out.
Here's what i learned:

#### Things to note

Friction is important cause it is what causes any vehicle to move on the ground. The tank is designed in such a way that it can move on most/all terain.
There are many forces that i will not go into detail as i do not know all of them but when i know all of them i will make a update on the blog but these are some of the examples that affect the movement o fthe tank

-Forces Calculation

-Aerodynamic Forces

-Motion Resistance

-Lift Force

-Lateral Force

-Tyre behaviour (Rolling Resistance)

-Contact 

-Pressure distribution of non-moving tyre

Some formulas:
TTE (Total Tractive Effort), RR (Force necessary to overcome Rolling Resistance), GR (Force required to climb a Grade), Fa (Force required to Accelerate to Final Velocity)
TTE [Ib] = RR [Ib] + GR [Ib] + Fa [Ib]

# Week 4
### Reflection
This week our lecturer, Mr Rodney, taught us micropython and how to install it on the ESP32. I'm going to summarise what he went though but if you want the full tutorials they will be at the bottom of this week's blog

#### Step 1: Install python into your computer
Go to this [link]([https://www.python.org/downloads/](https://www.python.org/downloads/)) and install a version of python. For this tutorial, and for future use. I would suggest installing the latest version of python(3.8.0 as the time of writing) to make sure you don't do any extra steps. Make sure you tick the box add to path
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjExNTI1NDA4N119
-->