>**WEEK 1**


- Brainstorming Ideas(Together with my teammates):
1. Deliver food in kitchen (due to oil in floor)
2. Automatic ward bed (less stress for nurses)
3. Stable rescue stretcher (reduce unnecessary movement of casualty)
4. Grab rubbish (easier for cleaners)
5. Exploration under river (Help with further experiment)
6. Construction site (transport of loads and construction materials due to loose and uneven soil)
7. Machine that helps to spot Thin ice for people

![Brainstorming Ideas](https://i.imgur.com/mrkp1fu.jpg)


>**WEEK 2**


>Learning Python:

Micropython BBC: https://microbit-micropython.readthedocs.io/en/latest/

Micropython for ESP32: https://docs.micropython.org/en/latest/esp32/tutorial/intro.html 

Micropython: https://docs.micropython.org/en/latest/

Helpful Tutorials for begineers: https://codewith.mu/ 

Thonny : https://thonny.org/

Java have a protocol to communicate with everyone

Python is much easier, function type and object-oriented approach 

Readability is important for everyone (clear understanding)

Arduino uses processing : https://processing.org/

## Two videos (Python): 

 [4 Hours Python ](https://www.youtube.com/watch?v=rfscVS0vtbw):

- Pros:
~Show most of the things needed to know within 4 hours
~Good examples & explanation

- Cons:
~Complicated for beginners
~Too lengthy the video

[Python Tutorial: Datetime Module](https://www.youtube.com/watch?v=eirjjyP2qcQ ):
- Pros:
~Explanation and clear to understand
~Interesting Tutorial about dates/time

- Cons:
~Talk too fast

*1st Python website* 

>*Important*: Capital, Underscore,String(need ""), From math import *

	print("*-*") --> *-*
	character_name = "John", character_age = 50/50.555/False.
	print("Hello" + character_name)


	print("LOL/n Meow") --> LOL Meow

	print(phrase.upper()) --> change the phrase to all upper

	print(phrase.isupper()) --> will state whether the phrase is upper is True/False.

	print(len(phrase)) --> is to check whether how many characters in the string.

	print(phrase[0]) --> show the character of the first letter.

	print(phrase.index("A letter") --> show the number for where the letter is.

	print(phrase.replace("Heaven", "God")) --> replace Heaven to God.

	print(max(4,6)) --> show the largest number

	print(round(3.7)) --> help to round off the number

	print(sqrt())/print(ceil())--> round 
	up/print(floor(3.7))--> round down

	name = input("Enter your name: ")
	print("Hello" + name)

	num1 = input("Enter a number: ")
	result = num1/ int(num1) --> whole number/float(num1) -->decimal
	print(result)

	friends = ["..","..",]
	print(friends[0:1])/print(friends.count()) 
	friends.sort/reverse() --> ascending order/alphabetical order

	def --> function?

*2nd Python website* 

>**WEEK 3** (MECHANICAL)


Friction Important (Cause of Traction) 

Forces Calculation 

Aerodynamic Forces (Extra Marks):
-Motion Resistance
-Lift Force
-Lateral Force

Tyre behaviour (Rolling Resistance)
~Contact Pressure distribution of non-moving tyre
(Need Calculate)


TTE (Total Tractive Effort), RR (Force necessary to overcome Rolling Resistance), GR (Force required to climb a Grade), Fa (Force required to Accelerate to Final Velocity)

TTE [Ib] = RR [Ib] + GR [Ib] + Fa [Ib]

>**WEEK 4** (Applying MicroPython In ESP32)


[ESP32 Reference](http://esp32.net/): This might help beginners to undestand more about ESP32

**Beginners Help (Steps Below:)**

1st Step: [Download Python Programe](https://www.python.org/downloads/) 
>Remember to **Tick** the pip box so do not need to reinstall pip again!!

2nd Step: [Understand about ESP32 & Installation of Python in ESP32](http://github.com/espressif/esptool/)

3rd Step: [Further application of MicroPython to ESP32](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)

Open your Device Manager and locate your USB Port Number (Eg: COM13) & put the following commands: 

| Commands    | Description |
| ----------- | ----------- |
|Firstly, --port (COM 13) erase_flash | Clear the data first before starting |
|Secondly, --chip esp32 --port (COM 13) write_flash -z 0x1000 (esp32-20180511-v1.9.4.bin) | Deploying the new firmware to your ESP32 |
>**ALL IN BRACKETS IS SUBJECTED TO CHANGE TO THE INDIVIDUAL'S USB Port Number & File Bin**

>**WEEK 5**

-Fan In (Number of inputs a logic gate can handle) & Fan Out (Number of gate inputs that the output of a logic gate drives)

-Two Options for ESP32 Devices:

1. Sink (Able to effectively reduce large currents & Also use small currents)  **Recommended**
2. Source (Relies on the main supply)
 
These two opetions refer to the direction of current flow between an I/O point on an I/O module and the connected device. 

**WARNING**: Only relevant for DC circuits with positive and negative polarities since current flows both directions in an AC circuit.

-Prevent Overcurrent & Protect Internal Resistance
Solution: Schottky diode ( It has a low forward voltage drop and a very fast switching action), Fuseable Diodes
