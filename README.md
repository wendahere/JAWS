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

Sean Woo (DEEE)

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
1. {15} M3x8 Hexagonal Socket Screws
1. {2}  Caterpillar Tracks
1. {6}  M2 Flange Screws
1. {16} M2 Countersunk Screws
1. {}
1. 
1. 
1. 


We followed [this link](https://github.com/SmartArduino/ESPboard/blob/master/miniT100Instruction.pdf) to build the T100.

![assembly_pic1]() ![assembly_pic2]()

![assembly_pic3]() ![assembly_pic4](https://imgur.com/aI0B99K.png)

![full_assembly]()

_talk about how the given tracks were too long, and how we plan to solve it (show insert pictures also)_

### Week 3 Assignment - 
_placeholder text_

## Week 4 (4/11/19 - 10/11/19):
### ESP32
![esp32_front]() ![esp32_back]()

![Picture of Flowchart](https://imgur.com/rRrUc35.png)

_placeholder text_

## Week 5 (11/11/19 - 17/11/19):


## Week 6 (18/11/19 - 24/11/19)



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkzMDQ2NTA1MywtNDQ3MzAzODcyXX0=
-->