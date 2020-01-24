# Jaws
>**SP Engineering Academy Year 2, Sem 2, Engineering Realisation Project**
- [x] Discuss about our Problem Statement,Features,Reasons(mainly 3 reasons for the society)& who.
- [x] Everyone learn about Markdown Guide
- [ ] Meet up frequently to do our prototype during the Holidays (so that we dont do last minute)
- [ ] Presentation Slides & Prototype ready to show off
- [ ] Ready to Impress Everyone!!

## Team Members:
WDLEE (DME)

AMBTan (DME)

SWoo (DEEE)

JNg (DEEE)

This is our group blog where we post our group discussion for our project. For more further information of each team member's weekly reflection/progress please refer to the following links.

- [Allen's Blog](https://github.com/wendahere/JAWS/blob/master/allen.md)
- [Jayvien's Blog](https://github.com/wendahere/JAWS/blob/master/Jayvien.md)
- [Sean's Blog](https://github.com/wendahere/JAWS/blob/master/Sean.md)
- [Wen Da's Blog](https://github.com/wendahere/JAWS/blob/master/wenda.md)

## Week 1 (14/10/19 - 20/10/19):
### Brainstorming Session:
Initial ideas:
1. Deliver food in kitchen (due to oil in floor)
2. Automatic ward bed (less stress for nurses)
3. Stable rescue stretcher (reduce unnecessary movement of casualty)
4. Grab rubbish (easier for cleaners)
5. Exploration under river (Help with further experiment)
6. Construction site (transport of loads and construction materials due to loose and uneven soil)

Features:
1. Suspension (Better ground traction)
2. Carry load
3. Controllable
4. Lightweight

How we brainstorm our ideas (based on): 
Demographics
Types of terrain
Situations

![alt text](https://i.imgur.com/mrkp1fu.jpg)

According to the picture above, we have narrowed down to 4 ideas, a tree planting machine, a partially autonomous stretcher, an autonomous first aid delivery drone, and an ice depth sensing robot.

After considering the 4 aforementioned ideas, we decided to go with the ice depth sensing robot. This is because we want to create something that can phase out the traditional methods of testing the depth of frozen ice paths to determine if it's safe to walk. The current methods mostly include a person to manually drill holes in the ice to check for the depth, which is often quite dangerous if there is a mistep as the person my accidentally walk on thin ice and fall into a pool of freezing water.

This will benefit society by:
1. Allowing people to safely play on ice without risk of death
2. Prevents harm from people checking ice
3. Can be modified such that it can be a subsitute to prevent deaths from landmines

Hence, our idea can benefit the society by automating or quickening the process of checking the depths of ice.
Its features include:
1. An ultrasonic depth scanner
2. Remote controllable
3. Able to work in extreme cold
4. Able to move well on ice

## Week 2 (21/10/19 - 27/10/19):  
### Week 2 Assignment-

- [Micropython BBC](https://microbit-micropython.readthedocs.io/en/latest/)
- [Micropython ESP32](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
- [Python Beginners](https://codewith.mu/)
- [Python Intermediate](https://thonny.org/)

>Advantages of Java:
It have a protocol to communicate with everyone

>Advantages of Python:
 Much easier/simple, function type, object-oriented approach and readable 

[Processing](https://processing.org/):

Processing is a flexible software sketchbook and learn how to code within the context of the visual arts.

**(Important)** : from microbit import *

display.show(Image.HEART)/display.show(Image.SQUARE)
sleep(500)
display.scroll("Welcome to Python")

**If Else Function**
while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SAD)
    else:
        display.clear() (clear display)

**Making Use Of Accelerometer**
while True:
    display.clear()
    if accelerometer.was_gesture("shake"):
        display.show(Image.ANGRY)
        sleep(2000)
        
*(recognised gestures are up,down,left,right,face up, face down, freefall, 3g,6g,8g,shake)*

**How to make your own images**
mytick = Image(“00500:”
		  “00500:”
  “55555:”
  “00500:”
  “00500:”)

display.show(mytick)

**ROCK PAPER SCISSORS**

from microbit import *

ROCK = Image("00000:"
             "55000:"
             "55500:"
             "55550:"
             "55550:")

SCISSORS = Image("50005:"
                  "05050:"
                  "00500:"
                  "00500:"
                  "00500")

PAPER = Image("55555:"
              "50005:"
              "50005:"
              "50005:"
              "55555")
while True:
    display.show(PAPER)
    sleep(500)
    display.show(SCISSORS)
    sleep(500)
    display.show(ROCK)
    sleep(500)

**Arrays**
-List is a collection which is ordered and changeable. Allows duplicate members.
-Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
-Set is a collection which is unordered and unindexed. No duplicate members.
-Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

*Microbit.display class*:

-> display.scroll(string)

-> display.show(image)

-> display.setpixel(x,y,value)

-> display.clear()

-> display.read_light_level()

## Week 3 (28/10/19 - 3/11/19):
### Continuous Track Vehicle
[History and application of track vehicles.](https://www.wikiwand.com/en/Continuous_track)

### T100

![t100](https://imgur.com/2S6XT3W.png)

We were given the mini T100 track vehicle to assemble and do our initial prototyping. We got this model from [aliexpres](https://www.aliexpress.com/item/32799533790.html).

### Assembly

![parts](https://imgur.com/O1qHP1a.png)
Parts (from top down and left to right):
1. {4}  Gaskets 
1. {15} M4x8 Hexagonal Socket Screws
1. {2}  Caterpillar Tracks
1. {6}  M2 Flange Screws
1. {2} Stents
1. {2} U-Shaped Brackets
1. {2} AA Battery Holder
1. {16} M2 Countersunk Screws
1. {40} M3x8 Hexagonal Socket Screws
1. {4} M2 Set Screws
1. {2} DC Motors
1. {2} M4x16 Hexagonal Socket Screws
1. {1} M2 Allen Key
1. {1} M3 Allen Key
1. {1} M4 Allen Key
1. {8} Follower Wheels
1. {6} Long Copper Spacers
1. {6} M4 Plain Washers
1. {8} Bearings
1. {12} Short Copper Spacers
1. {2} M3 Nuts
1. {4} Sprockets
1. {11} M4 Nuts

We followed [this link](https://github.com/SmartArduino/ESPboard/blob/master/miniT100Instruction.pdf) to build the T100.

![assembly_pic1](https://imgur.com/vtMDcJp.png) ![assembly_pic2](https://imgur.com/DlGoqch.png)

![assembly_pic3](https://imgur.com/Oz7rzAO.png) 

![full_assembly](https://imgur.com/SWuOjMp.png)

When building the T100, we ran into a problem, the given tracks were too long, which caused the initial assembled T100's tracks to have too much slack. This is an undesirable trait in a track vehicle.

![too much slack](https://imgur.com/598jnwR.png)

To rectify this problem, we simply removed the extra tracks from the full track length to a suitable length and then reassembled the T100.

![removal of tracks](https://imgur.com/9uyQHuN.png)

This is how the T100 looks after rectifying the problem.

![rectified](https://imgur.com/DlGoqch.png)

### Week 3 Assignment - 
_placeholder text_

## Week 4 (4/11/19 - 10/11/19):

Today our team recieved our ESP32(DevKit V1) for our project. This will be the actual board that we will use for our project.
Here's how it looks:
### ESP32
Front:
![esp32_front](https://imgur.com/9oX23iu.png)
 **&nbsp;**
 Back:![esp32_back](https://imgur.com/aJdcXof.png)
**&nbsp;**
**&nbsp;**
**&nbsp;**
Here is the pin layout:
![ESP32 board layout](https://user-images.githubusercontent.com/43029229/72858635-64df4380-3cfc-11ea-9816-811599423d33.jpeg)
**&nbsp;**
After that, our teacher gave us a mindmap for us that shows us the steps to download firmware and test our ESP32 with a simple code to make usre our boards are fully working
![Picture of Flowchart](https://imgur.com/rRrUc35.png)
Our group downloaded the firmware and also set up the wifi server on the ESP32 by ourselves on each of [our personal blogs](https://github.com/wendahere/JAWS) we successfully lit up the LED! Here's the code:
```
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
  led.value(not led.value())
  sleep(0.5)
```
credits to randomnerd tutorials
We also did some code to light up an LED using a web server. It can be found [here](https://github.com/wendahere/JAWS/blob/master/Content/esp32%20as%20webserver%20to%20control%20LED%20on%20pin2.py). See you next week!

_placeholder text_

## Week 5 (11/11/19 - 17/11/19):
There was not as much content gone through but our lecturer dabbled on the inputs and outputs how you should supply power to your circuit depending on your circuit.
For I/O ---> Fan In (Number of inputs a logic gate can handle) & Fan Out (Number of gate inputs that the output of a logic gate drives)
### The two ways were:
![power source](https://i.imgur.com/1joVHve.jpg?1)
1.  Sink:
As shown in the diagram, the method is using a external supply and connecting it onto(Able to effectively reduce large currents & Also use small currents)  **Recommended**
2.  Source (Relies on the main supply)

These two opetions refer to the direction of current flow between an I/O point on an I/O module and the connected device.

**WARNING**: Only relevant for DC circuits with positive and negative polarities since current flows both directions in an AC circuit.

-Prevent Overcurrent & Protect Internal Resistance

_Solution_: Schottky diode ( It has a low forward voltage drop and a very fast switching action), Fuseable Diodes



## Week 6 (18/11/19 - 24/11/19)
This week, our lectuer Mr Tune went through with us the software Fusion 360 which you can learn what is it about [here]([https://www.autodesk.com/products/fusion-360/overview#banner](https://www.autodesk.com/products/fusion-360/overview#banner)). 
If you are an enginner, we highly recommend this 3D software because:
1) It is cheap(or even free if you are a student or an educator), it offers a lot of features and modes you can use to make your product with that price.

2) It is heavily supported with very good guides made by the creators themselves that are easy to follow

3) It will be used by professionals in the near future due to its price and accessibility

4) It is a great beginner design software for engineers due to it being not as difficult and a good transition software, autodesk has even given some courses on helping you make transition to some other design softwares like soildworks and mastercam

Our lecturer went through with us [this lesson]([https://f360ap.autodesk.com/courses/mechanical-assemblies-fundamentals/lessons/lesson-1-create-component](https://f360ap.autodesk.com/courses/mechanical-assemblies-fundamentals/lessons/lesson-1-create-component))

## Week 7 (25/11/19 - 31/11/19)
Today our lecturer went through about power and taught us how to charge our track vehicle using modules and 
### Assignment
We were tasked to create a movable track vehicle system that includes:
- Motor Control
- Complete Power Requirments
- Power & Control Circuitry
- Minimum Vehicular Control

This [link](https://docs.google.com/spreadsheets/d/1R0S9KrCoPH62kREoQjKckePXDlVACkAIEKATCFftJw0/edit?usp=sharing) is the link to the spreadsheet that contains all the required calculations for the power requirement of our vehicle. 

The following is the schematics of our vehicle.
![Full schematic of the vehicle]()

This is how we coded the app used to control our vehicle. 

_then maybe add a video showing how the vehicle moves_

### Group Pitch
On top of going through the lecture about power, each group also presented what kind of track vehicle are they building and the features.

This [link](https://docs.google.com/presentation/d/1G-Mtn2crr3oMn-h9OzoTzIzBxInWUobSz7nGN9KObng/edit?usp=sharing) is our presentation slides. After our presentation, we were given feedback by our lecturers and classmates.

_insert feedback here_

## Week 8-14
During the holiday time, we each were doing our own parts for the track vehicle:
Mechanical &rarr; Allen and Wen Da
Coding &rarr; Jayvien and Wen Da
Electronics &rarr; Sean


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MzgwMTcxNTQsLTMyNzA0ODAyNiwtMz
Y0NjE2MDEyLC0xMTc4Mzk1NjE4LDE4NDg3MzM1NjQsMzc1MTI0
NjMwLC0yMDg5ODY5NTk1LC02OTI4Mjk1NTksLTE4NTE5MzI4OD
AsMjA3NDI2OTc1MiwtMTUzMDcxNjg5NywtNjIyMTIxMTIxLDE4
MDYwNjM5MjcsLTE1NzM1MzA2MTIsMjU4ODk0NzMyLC0xNTczNT
MwNjEyXX0=
-->