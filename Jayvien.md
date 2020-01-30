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

&rarr;*Important*: Capital, Underscore,String(need ""), From math import *

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

*Solution*: Schottky diode ( It has a low forward voltage drop and a very fast switching action), Fuseable Diodes

AC - DC Convert (230V AC / 3.3~24 DC)
Note: Some losses when conversion

[Power Your Electronics](http://youtube.com/watch?v=IT19dg73nKU&feature=youtu.be) 

>**WEEK 6**

-We learn how to use the different functions in the AutoCad:

The Author of these videos are Jamie Scherer, James Price who provide many videos for beginners.

[AutoCad Video Tutorial-Mechanical Assemblies](https://f360ap.autodesk.com/courses/mechanical-assemblies-fundamentals/lessons/lesson-1-create-component) 

[Homework for December Holiday](http://507movements.com/) 

>**WEEK 7**

**Buck Switch Mode Power Supply**:
- Reduce DC High Voltage to Low
- DC to Dc Converter & switching regulator

**Boost Switching Regulator**:
- Increase DC Low Voltage to High
- Common in Battery Chargers

**Buck Boost Switching Regulator**:
- ON (Sends energy to Inductor) / OFF (Delivers energy from Inductor)
- Duty Cycle determines the inverted output  voltage either greater/smaller than magnitude of input voltage

**Switch Mode Power Supply (SMPS)**:
- Buck Converters (Cheap / Converts High to Low DC Voltage)
- Boost Converters (Converts Low to High / Common in Li-ion Battery Banks (3.70V - 5V)

Voltages cannot be Low (Might not work properly) / Too High (Might destroy/burn)

**Lithium Battery** : Good Speed control, High acceleration, High starting torque(Wide Speed Range (RPM))
(Reacts to Air & Water) (Metal oxide + Lithium Ion = Lithium metal Oxide &rarr; Stable) 
Standard Cell (3V – 4.2V) produce a lot of heat (Use Battery Protection)

AC Source &rarr; Level Conversion (Transformer) &rarr;Rectifer (AC to DC) &rarr; Voltage regulator (To meet your voltage req)

>**WEEK 8**

**Wifi-Client**: [WIFI GUIDE](https://randomnerdtutorials.com/micropython-wi-fi-manager-esp32-esp8266/) 

Wi-Fi Manager is not in the MicroPython library so we need to upload it ourself.

&rarr; Firstly, check your Port & Micropython **(Search on your computer Device Manager then click on Port)**/**(Tools...Options...Interpreter)**

&rarr; Secondly, [Copy This To Your Thonny](https://raw.githubusercontent.com/tayfunulu/WiFiManager/master/wifimgr.py) & save this file in **Mi&rarr;cropython Device as wifimgr.py**
&rarr; Thirdly, [Open new file and Paste This File](https://raw.githubusercontent.com/RuiSantosdotme/Random-Nerd-Tutorials/master/Projects/ESP-MicroPython/esp_wifimanager_example.py) & save this file in **Micropython Device as Main.py**

&rarr; Next, Press EN button on ESP32 and check your wifi settings on your computer, it will state as **WifiManager and Password is tayfunulu**

> #### Micropython Shell Will Show This
> Connect to WiFi ssid WifiManager, default password: tayfunulu
> and access the ESP via your favorite web browser at 192.168.4.1.
> Listening on: ('0.0.0.0', 80)

**In case, there is a socket left open, Reset the ESP32 with machine.reset(). This will “forget” the open socket**

&rarr; When connected to the WifiManager, open your google chrome and paste 192.168.4.1. Next, choose a local network then enter the password to get access to the Wifi. **Getting a note stating: ESP Successfully connected to Wifi network**

Lastly, Reopen your browser and type the IP Address and you will get full access for ESP32 GPIO.

>**WEEK 9**

After doing the successful connection to the HTML webpage we try the LED method, Users click on the button in the HTML while controlling the LED to 'ON' or 'OFF':[HTML+LED](https://github.com/wendahere/JAWS/blob/master/Content/esp32%20as%20webserver%20to%20control%20LED%20on%20pin2.py)

This is just a follow up to check whether the HTML works well. We learn from this [Website](https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/)

>**WEEK 10**

As all vehicles needed to be moved using a command. 

I decided to take this opportunity to make a code that will move the Track Vehicle to what the user wants ("Forward","Left","Right"&"Backward")

This is my code that i came out with using REPL: [Motor Movement Code](https://github.com/wendahere/JAWS/blob/master/Content/ESPMOTORCODES/Jayvien%20WASD%20Movement.py)

Users can have the ability to move the Vehicle by using keys on the laptop (Got inspired by most game main key functions).

*TYPE THIS LETTERS ON YOUR REPL*

Forward --> 'w' / Left --> 'a' / Right --> 'd' / Backward --> 's' / Stop --> 'q'

After That, I tried to place the [Motor Movement Code](https://github.com/wendahere/JAWS/blob/master/Content/ESPMOTORCODES/Jayvien%20WASD%20Movement.py) together with the HTML [HTML+MOTOR](https://github.com/wendahere/JAWS/blob/master/Content/ESPMOTORCODES/MotorcontrolHTMLMark3.py) with WENDA assisting me to allocate the positioning yet again :9

>**WEEK 11-13**

WENDA bought his ultrasonic Sensor and tried to code it with the help of this [Website](). 
He tried the following codes inside:
[Code1](https://github.com/wendahere/JAWS/blob/master/Content/Ultrasonic%20codes/ultrasonictransducer.py)/
[Code2](https://github.com/wendahere/JAWS/blob/master/Content/Ultrasonic%20codes/ultrasonictransducermark2.py)/
[Code3](https://github.com/wendahere/JAWS/blob/master/Content/Ultrasonic%20codes/ultrasonictransducerworking151.py)

He did it successfully after trying it multiple times :0

While I researched more about other things to code for the next part of our project and tidy up some of the wires and labelled them on my previous code so that my teammates can do it themselves.

>**WEEK 14**


>**WEEK 15**

