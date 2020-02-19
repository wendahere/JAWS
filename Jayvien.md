# *Week 1*


- Brainstorming Ideas (Together with my teammates):
1. Deliver food in kitchen (due to oil in floor)
2. Automatic ward bed (less stress for nurses)
3. Stable rescue stretcher (reduce unnecessary movement of casualty)
4. Grab rubbish (easier for cleaners)
5. Exploration under river (Help with further experiment)
6. Construction site (transport of loads and construction materials due to loose and uneven soil)
7. Machine that helps to spot Thin ice for people

![Brainstorming Ideas](https://i.imgur.com/mrkp1fu.jpg)


# *Week 2*


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

## Video (Python): 

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
	
# *Week 3* (MECHANICAL)

Friction Important (Cause of Traction) 

Forces Calculation 

&rarr; Aerodynamic Forces (Extra Marks):
-Motion Resistance
-Lift Force
-Lateral Force

&rarr; Tyre behaviour (Rolling Resistance)
~Contact Pressure distribution of non-moving tyre
(Need Calculate)


TTE (Total Tractive Effort), RR (Force necessary to overcome Rolling Resistance), GR (Force required to climb a Grade), Fa (Force required to Accelerate to Final Velocity)

TTE [Ib] = RR [Ib] + GR [Ib] + Fa [Ib]

# *Week 4* (Applying MicroPython In ESP32)


[ESP32 Reference](http://esp32.net/): This might help beginners to undestand more about ESP32

**Beginners Help (Steps Below:)**

1st Step: [Download Python Programe](https://www.python.org/downloads/) 
> Remember to **Tick** the pip box so do not need to reinstall pip again!!

2nd Step: [Understand about ESP32 & Installation of Python in ESP32](http://github.com/espressif/esptool/)

3rd Step: [Further application of MicroPython to ESP32](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)

***DOWNLOAD LINK TO BIN ACCESS PLS SCROLL DOWN*: [ESP32 FLASH BIN](http://micropython.org/download#esp32)

&rarr; Open your Device Manager and locate your USB Port Number (Eg: COM13) & put the following commands: 

| Commands    | Description |
| ----------- | ----------- |
|Firstly, --port (COM 13) erase_flash | Clear the data first before starting |
|Secondly, --chip esp32 --port (COM 13) write_flash -z 0x1000 (esp32-20180511-v1.9.4.bin) | Deploying the new firmware to your ESP32 |
>**ALL IN BRACKETS IS SUBJECTED TO CHANGE TO THE INDIVIDUAL'S USB Port Number & File Bin**

# *Week 5*

- Fan In (Number of inputs a logic gate can handle) 

- Fan Out (Number of gate inputs that the output of a logic gate drives)

>Two Options for ESP32 Devices:

1. Sink (Able to effectively reduce large currents & Also use small currents)  **Recommended**
2. Source (Relies on the main supply)
 
These two opetions refer to the direction of current flow between an I/O point on an I/O module and the connected device. 

**WARNING**: Only relevant for DC circuits with positive and negative polarities since current flows both directions in an AC circuit.

-Prevent Overcurrent & Protect Internal Resistance

*Solution*: Schottky diode ( It has a low forward voltage drop and a very fast switching action), Fuseable Diodes

AC - DC Convert (230V AC / 3.3~24 DC)
Note: Some losses when conversion

[Power Your Electronics](http://youtube.com/watch?v=IT19dg73nKU&feature=youtu.be) 

# *Week 6*

We learn how to use the different functions in the AutoCad:

[AutoCad Video Tutorial-Mechanical Assemblies](https://f360ap.autodesk.com/courses/mechanical-assemblies-fundamentals/lessons/lesson-1-create-component) 

[Homework for December Holiday](http://507movements.com/) 

# *Week 7*

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

*Voltages cannot be Low (Might not work properly) / Too High (Might destroy/burn)*

**Lithium Battery** : Good Speed control, High acceleration, High starting torque(Wide Speed Range (RPM))
(Reacts to Air & Water) (Metal oxide + Lithium Ion = Lithium metal Oxide &rarr; Stable) 
Standard Cell (3V – 4.2V) produce a lot of heat (Use Battery Protection)

**AC Source &rarr; Level Conversion (Transformer) &rarr; Rectifer (AC to DC) &rarr; Voltage regulator (To meet your voltage req)**

# *Week 8*

**Wifi-Client**: [WIFI GUIDE](https://randomnerdtutorials.com/micropython-wi-fi-manager-esp32-esp8266/) 

Wi-Fi Manager is not in the MicroPython library so we need to upload it ourself.

&rarr; Firstly, check your Port & Micropython **(Search on your computer Device Manager then click on Port)**/**(Tools...Options...Interpreter)**

&rarr; Secondly, [Copy This To Your Thonny](https://raw.githubusercontent.com/tayfunulu/WiFiManager/master/wifimgr.py) & save this file in **Micropython Device as wifimgr.py**

&rarr; Thirdly, [Open new file and Paste This File](https://raw.githubusercontent.com/RuiSantosdotme/Random-Nerd-Tutorials/master/Projects/ESP-MicroPython/esp_wifimanager_example.py) & save this file in **Micropython Device as Main.py**

&rarr; Next, Press EN button on ESP32 and check your wifi settings on your computer, it will state as **WifiManager and Password is tayfunulu**

> #### Micropython Shell Will Show This
> Connect to WiFi ssid WifiManager, default password: tayfunulu
> and access the ESP via your favorite web browser at 192.168.4.1.
> Listening on: ('0.0.0.0', 80)

**In case, there is a socket left open, Reset the ESP32 with machine.reset(). This will “forget” the open socket**

When connected to the WifiManager, open your google chrome and paste 192.168.4.1. Next, choose a local network then enter the password to get access to the Wifi. **Getting a note stating: ESP Successfully connected to Wifi network**

Lastly, Reopen your browser and type the IP Address and you will get full access for ESP32 GPIO.

# *Week 9*

After doing the successful connection to the HTML webpage we try the LED method, Users click on the button in the HTML while controlling the LED to 'ON' or 'OFF':  [HTML+LED](https://github.com/wendahere/JAWS/blob/master/Content/esp32%20as%20webserver%20to%20control%20LED%20on%20pin2.py)

This is just a follow up to check whether the HTML works well. We learn from this [Website](https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/)

# *Week 10*

As all vehicles needed to be moved using a command. 

I decided to take this opportunity to make a code that will move the Track Vehicle to what the user wants ("Forward","Left","Right"&"Backward")

This is my code that i came out with using REPL: [Motor Movement Code](https://github.com/wendahere/JAWS/blob/master/Content/ESPMOTORCODES/Jayvien%20WASD%20Movement.py)

Users can have the ability to move the Vehicle by using keys on the laptop (Got inspired by most game main key functions).

*TYPE THESE LETTERS IN YOUR REPL*:

**Forward --> 'w' / Left --> 'a' / Right --> 'd' / Backward --> 's' / Stop --> 'q'**

After that, I tried to place the [Motor Movement Code](https://github.com/wendahere/JAWS/blob/master/Content/ESPMOTORCODES/Jayvien%20WASD%20Movement.py) together with the [HTML+MOTOR](https://github.com/wendahere/JAWS/blob/master/Content/ESPMOTORCODES/MotorcontrolHTMLMark3.py). 

I also placed more buttons so that we can click different buttons to work.

![HTML+MOVEMENT](https://github.com/wendahere/JAWS/blob/master/Images/29-1.PNG)

# *Week 11-13*

While I researched more about other things to code for the next part of our project and tidy up some of the wires and labelled them on my previous code so that my teammates can do it themselves.

I input the dropdown menu for our team so to allow users to choose the mediums & Wenda helped me to align the position of the dropdown menu.

- I learned that the button and changed position of the dropdown should be relative not absolute. 

![HTML+Functions](https://github.com/wendahere/JAWS/blob/master/Images/30-1withdropdown.PNG)


# *Week 14*

Our Teacher, Mr Rodney Dorville. He showed us some videos in youtube that will teach us to use different types of devices that the experts used before to improve their project.

One example is [rdagger68](https://www.youtube.com/channel/UCp2rS5TxRt6W8fieAk74bIw). 

>*He mainly uses Raspberry Pi & Other items that teaches viewers on things that we can do with different types of devices through his tutorials.*

**&rarr; 1st Milestone:
Everything works well but Sean do his part very last minute which causes our team to lose 15 marks for it.**

I showed my [Working Movement Code](https://github.com/wendahere/JAWS/blob/master/Content/ESPMOTORCODES/Jayvien%20WASD%20Movement.py) to Mr Rodney and he was impressed with it. Also showed the [HTML+MOTOR](https://github.com/wendahere/JAWS/blob/master/Content/ESPMOTORCODES/MotorcontrolHTMLMark3.py) to him as well.


So i was interested with the PCA9685 it with the servor motor.

*I asked for the components from Mr Rodney so that i can try it my own at home*

**[AdaFruit PCA9685 Explain](https://learn.adafruit.com/16-channel-pwm-servo-driver?view=all)

**[Further More Explaination](https://www.youtube.com/watch?v=y8X9X10Tn1k)

--> So i read it and tried to do the code also listen to [Youtuber,Robojax](https://www.youtube.com/channel/UCkcBSig_Iu4ZnAIeCeG1TVg)...I actually saw one of the led in the ULN2003 Motor Driver lit up but i totally forget to take a picture and video which lose my effort for proving it. 

[pca9685.py](https://github.com/wendahere/JAWS/blob/master/Content/SERVO/pca9685.py)

[ULN2003 MOTOR DRIVER](https://www.google.com/search?q=ULN2003+driver+pinout&rlz=1C1NDCM_enSG809SG809&tbm=isch&source=iu&ictx=1&fir=kgwz541PNmwbyM%253A%252CTpIyhKIj55w4qM%252C_&vet=1&usg=AI4_-kQFJ28WLiIUOHT33_YMlS3NzBUyjA&sa=X&ved=2ahUKEwjh1N7r0rLnAhVj7XMBHVyMDy0Q9QEwBXoECAkQDg#imgrc=mXENAulIXQIhOM:&vet=1). This will show the pinouts needed to be placed.


# *Week 15*

Our Teacher, Mr Chien Jung Tune. He told us the importance of showing our track vehicle and other parts in FUSION 360. [FUSION 360 DOWNLOAD](https://www.autodesk.com/products/fusion-360/students-teachers-educators)

He told us that we need to show a sketch of how it looks like because it mainly describes clearly to viewers as well as teammates on how the physical parts looks like and the implentation of it as well. **Presenting the entire chasis, motors, nuts, and all the parts required in our track vehicle.**
 
# *Week 16*

This Week, I did the OLED Coding Tasks that Mr Rodney assigned each team to do. 

- Firstly, in order to have the OLED working with ESP32 we need to create a [OLED Library](http://github.com/wendahere/JAWS/blob/master/Content/MAIN%20OLED%20ssd1306.py) for it. **Save this file as ssd1306.py.**

*The main purpose of this is to allow ESP32 to access the OLED to print something on the screen , set its sizes & dimensions.*

- After doing that, it is important to display something on your screen to show the output of it. So I asked my team what output they want to see in the OLED Display and they decided they want 'SAFE' & 'NOT SAFE'. And I Showed the [OLED MAIN CODE](https://github.com/wendahere/JAWS/blob/master/Content/Jay%20OLED%20main.py) to them.

However, there is one more important step after doing all of these. It is very important to **Press the EN button on your ESP32** to enable it to the OLED Display. This will pop out the words you type inside the [OLED MAIN CODE](https://github.com/wendahere/JAWS/blob/master/Content/Jay%20OLED%20main.py) that i given to you before. [MORE GUIDES](https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/)

# *Week 17*

I combined both the Ultrasonic Seonsor & OLED together and changed a little to show the display of the status of the vehicle as well as the value of the ultrasonice sensor in the OLED. [Combined OLED+ULTRASONIC Code](https://github.com/wendahere/JAWS/blob/master/Content/Jay's%20Oled+Ultrasonic%20Sensor.py).
It worked prefectly showing what i want.

Wenda wanted to try do the PCA9685. So he used the codes that i did it before and he just copy and paste a long string of code without understanding it, of course it didnt work anything for him since he didnt take time to understand it clearly. Then he just gave up it and said he will just do a normal servor motor basic code.

# *Week 18*

This week, i passed my [Combined OLED+ULTRASONIC Code](https://github.com/wendahere/JAWS/blob/master/Content/Jay's%20Oled+Ultrasonic%20Sensor.py) to WenDa so that he can help me combined it with our HTML. So i can help Sean with his electronics as an assistant and update some of our slides as well. I also stayed back to help sean with his electronics so that we can get tested all our components & codes.

I also read up the [Display Analog value Tips](https://randomnerdtutorials.com/esp8266-adc-reading-analog-values-with-nodemcu/).

This is for the voltage divider to show battery life value which requires about 3 different ohm resistors since the website suggests us to use 1k potentiometer.

It gave the code for micopython and explains it clearly to readers.

# *Week 19*

This week, i countinued helping sean in his electronics and changed the lengthy sentences of the poster to something sweet and short for the readers. We assembled our prototype together so that we can put it in our poster.

![Done Construction](https://github.com/wendahere/JAWS/blob/master/Images/FULL%20CONSTRUCTION.jpg)

Before testing of all our codes in HTML MAIN CODE, Wenda collate the code together in [Main#4](https://github.com/wendahere/JAWS/blob/master/Content/MAIN/Main%234.py). He told me to change the code when needed so to show values in the OLED. At first, i thought i dont need to change anything after reading through [It](https://github.com/wendahere/JAWS/blob/master/Content/MAIN/Main%234.py) also since i figured out the [OLED SWITCH SCREEN](https://github.com/wendahere/JAWS/blob/master/Content/Jay's%20Oled%20skip%20timing.py) and my teammate wanted the switching screen idea as well. 

The code was quite messy and less comments which are quite hard to understand what wenda trying to achieve. This, however lead to Wenda's code having a few problems (mainly capital letters, OLED positioning clashes, one of the servo's command doesnt work) during our testing. Also Sean's soldering circuit have some minor problems that he fixed while we was testing.

Wenda even admit to Vincent that he mostly copy and paste codes from internet...this shows why he wasnt able to understand what he was doing all this time.

Since i did the OLED for my team i realised that we dont need the switching screen idea. And i checked another time and realised that the code didnt import the ssd1306 file in the ESP32 so i just changed the positioning of the STATUS, Ultrasonic Transducer & Battery Life value in the code as well as put in the OLED ssd1306 library to the ESP32.

&rarr; **[Main#5 Updated](https://github.com/wendahere/JAWS/blob/master/Content/MAIN/Main%235.py)**

>OLED finally shows what i wanted to see:

*little Bit Blur Sorry :9*

![Jay's Oled Prove](https://github.com/wendahere/JAWS/blob/master/Images/Jayvien%20OLED%20Prove.jpeg)

We recheck by testing the servor motor movement and the wheel movement just to check before going home. 

[HERE IS THE YOUTUBE VIDEO](https://www.youtube.com/watch?v=qm3RDykjh20&feature=youtu.be)

# *Presentation Week*

[Here](https://docs.google.com/presentation/d/1Lq_Oh_S7RbmHg3k1PEp-lbV-0LjMcQh1vjn0CY7_IiM/edit?usp=sharing) is the link to our Presentation Slides.

Before our team's presentation start, Wenda tested to see whether his own servo motor working but unfortunately there is some error in the calulatations & the commands for the ultrasonic transducer.

Our Teacher, Mr Rodney Dorville & Mr Chien Jung Tune was kind enough to give every group some time to make amends because VIPs & Directors of different school are coming to see it on Friday, *(21 Feb 2020)* .

Since Wenda code the servo motor and the ultrasonic transducer before giving me to make it finalise it to the OLED display, he have some experience with it and wanted to spot his own mistake. So he redo our [Our Main Code](https://github.com/wendahere/JAWS/blob/master/Content/MAIN/Main%237.py).



# *SPECIAL THANKS TO OUR TEACHER, <MR RODNEY DORVILLE & MR CHIEN JUNG TUNE> FOR SHARING EXPERIENCES, TIPS & ADVICES TO IMPROVE*
