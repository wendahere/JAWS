# Week 1
Our week 1 documentation is the README.md file if you want to check it out then go ahead
# Week 2
This week my teacher, Mr Dorvile, gave us a task to make a space invaders game in under two hours. Thus, I attempted the challenge and these are the thought I have after the challenge.

If you don't know what am i talking about here is a example of the game [right here](https://www.youtube.com/watch?v=qtPmawMdgQ0)



## Reflections
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
## Reflections
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

fill this up

# Week 4
## Reflection
This week our lecturer, Mr Rodney, taught us micropython and how to install it on the ESP32. I'm going to summarise what he went though but if you want the full tutorials they will be at the bottom of this week's blog
  
<p>&nbsp;</p>

### How to install Micropython into ESP32
#### Step 1: Install python into your computer
i) Go to this [link](https://www.python.org/downloads/) and install a version of python. For this tutorial, and for future use. I would suggest installing the latest version of python(3.8.0 as the time of writing) to make sure you don't do any extra steps. However, if you want to install a specific version, make sure you have pip installed into your computer as it is needed for a later step. 

ii) Moving on, if you have a 32 bit computer(you can check it in settings), just click to where the arrow is pointing to then you will be able to install the latest version.![IMAGE ALT TEXT HERE](https://i.imgur.com/QP7Poi5.jpg)
However, if you do not have that, then you would have to scroll down the page until you find the latest version of python(newest release date does not mean it is the latest version of python). 
Click on it and you will be on another page. 

iii) Scroll down until you see this page. 
![IMAGE ALT TEXT HERE](https://i.imgur.com/Gcpp0Qp.png)
Download the x86-64 file(can be any of them) and run it on your computer. If you are a beginner, just put all the options as default **except for changing the option to adding it to path shown in the image below**:
![imgur](https://i.imgur.com/RRTOTsa.jpg)
Now you have python installed!
<p>&nbsp;</p>

#### Step 2:Using pip, download the ESP tool

i)Now you have python installed, go to your command prompt or windows powershell and type ```pip ```. It should list the functions that pip can do on your computer. However, if you are getting this output: ```Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pip' is not defined```, close the tab and type pip again. if the error still persists, it probably means you need to install pip on your computer which [this article will tell you how](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation). 

ii) If it is working correctly, type ```pip install esptool``` into the command prompt and it will download the esptool **make sure not to touch it to not sever the connection**.

iii) After that, type in the command ```esptool.py --port /dev/ttyUSB0 erase_flash``` if you are a mac user and ```esptool.py --port COM(port number) erase_flash``` if you are a windows user. if you do not know how to find a port number click [here](https://www.youtube.com/watch?v=VGW2dCGNBD0).

iv) After that, go to this [page](http://micropython.org/download#esp32)
  download will be the firmware that your ESP32 can use micropython. **Make sure you remeber where you save the file your going to path it later**
  
v) After that is done, type in ```esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 (firmware file name)``` if you are a mac user and ```esptool.py --chip esp32 --port COM(port number) write_flash -z 0x1000 (firmware file name, need to path it)``` .

vi) After that it will download the programe and now you have micropython on your ESP32

vii) Then, you can step up the web server,

# Week 5
## Reflection
Today it was a break week cause of some misunderstandings but our lecturer dabbled on power sources and you can check it out [here on the week 5 blog](https://github.com/wendahere/JAWS/blob/master/README.md)
This week i worked on the CA1 mechanical project that my teacher gave us in week 3. Here is my [solution](https://docs.google.com/presentation/d/14wCOhlp1a8PnIeWZdCQ_XQQmwKzjfe_fPMTIVctNZZI/edit?usp=sharing).
Well, that's all for this week!

# Week 6
## Reflection
For this week our lecturer went through with us how to move components and join those components to build assemblies for our project, the link for the lessons are [here]([https://f360ap.autodesk.com/courses/mechanical-assemblies-fundamentals])
Our teaher also has tasked us with making an assembly in Fusion 360 based on Mr Thang's creations on his [youtube channel](https://www.youtube.com/user/thang010146/videos)
I'll explain more in my holiday part of the blog

# Week 7
## Reflection
For this week our lecturer went through on power sources more and how we should use this knowledge and construct a rechargable power supply for our tracked vehicle and it will also be also be covered more in detail 
in the holiday blog. to learn about power sources, watch this video [here](https://www.youtube.com/watch?v=IT19dg73nKU&feature=youtu.be). For now, see ya!

# Week 8 - Week 14
## Reflection for mechanical homework
Looking back at week 6, the design I chose was [the woodpecker](https://www.youtube.com/watch?v=zqnzgwYDKLY) and     ,[Straight line drawing mechanism 9](https://www.youtube.com/watch?v=Zwwnr262Wlc) from [Mr Thang's youtube channel](https://www.youtube.com/channel/UCli_RJkGWfZvw4IlDLHNCQg). The woodpecker was really hard as the woodpecker toy moves by gravity and it is a very unique motion. Even Mr Tune, the lecturer that assigned me this task, also did not know how to do this in fusion 360 so i gave up on creating motion links for thisdesign and instead did the other one.
This one was actually much easier as because it only includes three types of joints: slide, revolution and ridgid.
The hardest part of me was that you need to be very presice with the measurement if not you would have a straight line so reviewing the original file helped a lot in recreating the deisgn

#### Lessons learnt:
1. If you were designing a new design or recreating a certian design. It is best that you should try to source exsisting designs of certian things like gears to save time in your designing phase.
2. Try to get a design that is not extremely hard if you are under a dateline cause its going to be very hard to emulate it.


## Reflection for electronics homework
It was honestly quite hard and I took quite long to get a working power circuit as I did not want to remove the batteries while charging.

My lecturer gave us a TP4056 charging module and two 3.7V 18650 lithium ion batteries to start with our project. **My goal was to create an internal charging station inside the track vehicle for two batteries to power the whole circuit**.

Firstly, I researched about the module to understand about how to use it to power the track vehicle. I tried
 to see the [datasheet](http://www.haoyuelectronics.com/Attachment/TP4056-modules/TP4056.pdf) and youtube videos about it and I realised a couple of things:

1. The TP4056 module only supports one cell or parallel charging and **if I were to use two batteries I would need to have two modules**
2. If you were to charge multiple batteries in parallel, the voltages of the batteries must be *almost identical* as batteries have different charging capacities so while one battery may be full, the other battery in parallel may be still charging. This causes overcharging in that one battery and it will damage and reduce the life of that battery faster. **Thus, I can't use batteries with different voltages**

3. If batteries were connected in series, they would not drain simultaneously, instead, the first battery would be the one to drain first. **Thus, the batteries would be in different voltages and would lead to overcharging. So all the more to get another charging module.**
4. Reading the datasheet for the charging module, I found out that it has battery protection, meaning that it has a measure to deal with overcharging. However, the module battery protection only kicks in if the battery's voltage has reached 4.2 volts. **That means if my battery's max voltage(achieved when it reaches max capacity) is less than 4.2 volts, the battery is not protected at all, casuing overcharging**
5. The output of the Vout is always the voltage of one battery. **Thus, if you were to connect the negative terminal of the Vout of one module to a positive terminal of the Vout of another module, then the voltage would not add up and will still be the voltage of one battery.**

To conclude, I would need to make two modes for my power circuit, the first mode is for charging which i will call rest mode, the second mode is for outputing the power to the rest of the components, I will call this active mode.
The first circuit design I created was inspired from [this video.](https://www.youtube.com/watch?v=rpRYNMrVCk0) It looks like this:

There were two problems:
1. It does not charge properly
2. It does not output 8V and the voltage was always decreasing. It also does not have current flowing through when it is at active mode.

Thus, I needed to change the power circuit and that 




<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM2MzYwOTE2MCwtMjAwOTYyMTc2MSwtND
YxMDg2MDcxLDczODI5MzIwNiwxNTM5NDc3NDA5LC0xMjkxOTI3
NjM4LDMzOTQwOTA5NywtMTU4MjIxMTg3NywtNjUwMTEyNTE5LD
EwOTYwNDM1NjMsMTExNDY4MTk4OCw2MzA1MDg3OTMsLTU0MjEx
MDg5OCwyMTIzNDY5OCwxOTQyMTM0MTQyLDE5MDQ1MjI3NTcsMT
gwNDU0OTcwMiwtMTczMjAxMDI2NCw5MTI4NjczNjIsLTU4NjYz
ODUzN119
-->