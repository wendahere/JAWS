## This site records WDLee's work and progress reflection.

# Week 1
Learned about markdown and git.
Markdown after trying it out, seems relatively easy and useful to use. It can convert text to html format and make stuff like creating headers simple. 

Git on the other hand is more complicated. I cloned my repo for JAWS and replaced it with the git version. There was a hidden .git folder after cloning it. 
I think that the hard part about git is getting a hang of using the commands. I will keep a site of the commands open until I manage to memorize them. 

Organized and met up with groupmates to discuss on ideas. I like my tree sapling planting idea but as the Ice idea was more popular and fun, we decided to proceed with that.
Entire meeting took about 2.5 hours.

I have downloaded both markdown and  git on my laptop so I will be using them. I will keep using git to get used to it. I am currently writing this on markdown :)

# Week 2



##Conclusion: 
My code was successful. The code can be seen below.

	from microbit import *

	import random

	 #starting position of spacecraft
	spacecraft = 2
	display.set_pixel(spacecraft, 4,5)

	 #alien randomly appears from top y=0, x is random 0-4
	alienx = random.randint(0, 4)
	alieny = 0
		while True:
	    display.clear()
	    display.set_pixel(spacecraft, 4, 5)
 	   display.set_pixel(alienx, alieny,5)
   
 	   if button_a.is_pressed():
  	      spacecraft = spacecraft -1
  	    #move left
  	  elif button_b.is_pressed():
  	      spacecraft = spacecraft +1
 	  #move right
 	 #move alien down by y+= 1
 	   alieny = alieny + 1
    
 	   if alieny >4:
  	      alieny=0
  	      alienx= random.randint(0,4)
  	 #when alien and player collide, game will end and loop game over!
  	  if alienx == spacecraft and alieny == 4:
  	      break
  	  sleep(250)
        
	display.scroll("GAME OVER!", loop=True)

I had problems moving my spacecraft, I found out that the method I was using to move the spacecraft could not be used in micropython, ( x-=1 cannot be used), ( spacecraft = spacecraft -1) was used instead.

I had problems with unresponsive spacecraft, when I pressed any button, the spacecraft would not move or would move late. I had put sleep(500) at first. I changed to sleep(200) and it was fixed.

I also had problems with the old spacecraft staying in place after moving. I did not use display.clear(). At first, I did display.set_pixel(x+1,4,0) and display.set_pixel(x-1,4,0). To delete the spaces left and right of the new spacecraft. I read my old notes and remembered about display.clear and used it instead.

I had obstacles writing unfamiliar parts of the code, such as :"display.set_pixel(spacecraft, 4, 5)". I had to search online for examples as I have not written set_pixel before.

A tip I would give to make your program succeed is to plan out first, in this place, plan out where would the spacecraft start position be, which buttons would move it. This will make the flow of writing the code simpler as there is no need to think about what is next, we can just refer to the plan to know what is next.

I have watched 2 [youtube videos](https://www.youtube.com/watch?v=JLOOWVwDftg) and the youtube video I would recommend for beginners is [this](https://www.youtube.com/watch?v=nwIgxrXP-X4). There is very simple demo for you to follow and get interested in coding. He is understandable and slow, we can understand can easily follow his steps.

I have watched a video on Python programming and would like to recommend it. This is the 
[link](https://www.youtube.com/watch?v=IMGzzK9Wn4w). 


[![Or below here](http://img.youtube.com/vi/IMGzzK9Wn4w/0.jpg)](http://www.youtube.com/watch?v=IMGzzK9Wn4w)

#### Pros:
- Goes through everything of Python, including installation of the program required
- Very clear on explanation and understandable English
- Considered short, compared to 4 hours tutorial 
- Everything packed into 1 hour 30mins
- Rather new video (2019) and updated channel
#### Cons: 
- Video volume not consistent, start and end of video is VERY loud, please be careful
- Have to pause the video if you are following


## Journal for Week 2
Learned about micropython and using the BBC Microbit.
We used Thonny to program the Microbit. I was really interested and invested in this as it was a fun topic for me. I liked that I could create simple games and displays using the Microbit with little effort. 

Our assignment was to download the python editor, I used Thonny during class but I am thinking of using MU editor instead as it was for more beginners like me.

###  Week 2 - Second half of the week
I used Thonny to code this.

I have done the space invader game (Below)
This was my original code, I had troubles getting the x value to move, I referred to 
[Python Link](https://www.tutorialspoint.com/increment-and-decrement-operators-in-python) which was python and not micropython. 
For micropython, I don’t think x-=1 or x+=1 can be used, therefore my original code did not work.

from microbit import *
import random

x=2
display.set_pixel(x,4,5)
while True:
    if button_a.is_pressed():
        x-=1
        display.set_pixel(x,4,5)
        display.set_pixel(x+1,4,0)
    elif button_b.is_pressed():
        x+=1
        display.set_pixel(x,4,5)
        display.set_pixel(x-1,4,0)  

#### Traceback (most recent call last):File "<stdin>", line 13, in <module>ValueError: index out of bounds

At the the end, once any value exceeds the boundary, there will be this error, index out of bounds. I have tried using arrays but the value will still get out of bound of the array. The only solution I have for this is to simply reset the game before any value gets out of bounds, which includes the player.

### Revised Version of code
I rewrote the code from scratch after finding out my mistake, was stumped and could not figure out why after an hour of searching, therefore I started from scratch and used another method to move the spacecraft instead.


### Space Invaders Demo

[![Space Invaders!](http://img.youtube.com/vi/JxIyh3bOaRo/0.jpg)](http://www.youtube.com/watch?v=JxIyh3bOaRo)

# Week 3 (28/10/19 - 4/11/19)

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



# Week 4

##### For class, we used ESP32.

### Tutorial to use ESP32
Follow this [guide](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation) if unclear, there are picture and clear steps. This is a good guide.

1. [Install Python](https://www.python.org/downloads/) (Make sure to tick Path installation)
2. [Install Pip](https://bootstrap.pypa.io/get-pip.py) (Right click and save as link)
		
		a. Use "py -m pip" if "pip" does not work

3. Step up PATH and ENVIRONMENT VARIABLE to be able to run Pip and Python from anywhere
4. [Download firmware](https://github.com/espressif/esptool/) or [This](https://micropython.org/download#esp32) Use "pip install esptool"
5. Deploy firmware using command, follow below.

"esptool --port COM3 write_flash 0x1000 my_app-0x01000.bin" OR "esptool.py --port COM3 write_flash 0x1000 my_app-0x01000.bin" if the earlier doesn't work.

esptool worked for me but esptool.py does not.

--port is your port that the ESP32 is plugged into, you can use Device Manager to find what port it is plugged into

my_app-0x01000.bin is the firmware name, rename it to your current firmware .bin name.

### Done!

# Week (5-7)

Mechanical CAD Assignment. 

I did 2 designs. [Easier one](https://youtu.be/9oUzNAoKIjM) for practice and [Main one](https://www.youtube.com/watch?v=rGYGc-Qtqgk) for submission. 
[My completed design](https://youtu.be/2u0hkplDt-E)


# Week (8-13)

### Installing wifimanager and main on ESP32.
I used Thonny for this.
Guide followed: [Link](https://randomnerdtutorials.com/micropython-wi-fi-manager-esp32-esp8266/)

Step 1: In Thonny, top bar, open Tools>Options>Interpreter
Check if "MicroPython On ESP32" is there. Port, if you know what port is plugged into, click that, if not use <Try to detect port automatically>

If there is no esp32 option, go on google and download it.

Step 2: Plug in ESP32 into the computer. Press boot on the ESP32 and look at shell if the ESP32 is connected.

Step 3: Upload wifimgr.py [Copy and paste this](https://raw.githubusercontent.com/tayfunulu/WiFiManager/master/wifimgr.py) into Thonny and click File>Save As> Micropython Device (Important!). Name the file "wifimgr.py".

Step 4: Similar to step 3. [Open this](https://raw.githubusercontent.com/RuiSantosdotme/Random-Nerd-Tutorials/master/Projects/ESP-MicroPython/esp_wifimanager_example.py) and paste the code into Thonny but save as "Main.py" instead into the Micropython Device.

Step 5: Press "EN" button on the ESP32 and look at the shell. If there is no error code, it is working. Check by opening wifi (bottom right) on your computer/phone. If there is "WifiManager" means it is working.

[Such as this.](https://raw.githubusercontent.com/wendahere/JAWS/master/Images/esp32wifi.png)

### Hello World in browser.
By default, IP Address is set to http://192.168.4.1/
Follow [this](https://randomnerdtutorials.com/micropython-esp32-esp8266-access-point-ap/) guide. I made the ESP32 into a web server, an access point and printed "Hello World" in that address.

Upload [this](https://raw.githubusercontent.com/RuiSantosdotme/Random-Nerd-Tutorials/master/Projects/ESP-MicroPython/esp_access_point_boot.py) as boot.py and run.

## Controlling LED using ESP32 as a web server

I followed this guide, [link](https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/). As my ESP32WROOM 32D has no inbuilt LED, I had to plug into a breadboard and control that LED instead. Have to change the [code](https://www.codepile.net/pile/J2GjNkVa). I modified the code such that the ESP32 does not connect to the internet but we connect to the ESP32 instead.

We completed the chassis for JAWS.

#Week 14


Milestone 1 Day.

Coded ESP Webserver without motor controls yet. My teammate did manual control (WASD) input to control the motors. 
[This was the code for HTML](https://github.com/wendahere/JAWS/blob/master/Content/ESPMOTORCODES/motortest2withhtml.py)

We did the boost converter and batteries chargers this week.

The movement works for WASD controls, we ended up getting 75/100 for 15% of the project.

#Week 15


I combined the codes to enable movement using the web server. 



[![Video!](http://img.youtube.com/vi/otZNYrKTPwY/0.jpg)](http://www.youtube.com/watch?v=otZNYrKTPwY)

The circuit is powered using batteries, showing boost converter and buck converter working!

I will be working on the ultrasonic sensor web server control.

#Week 16


I had issues with the code. After researching the error message, I realized that I did not put a return on the ultrasonic sensor function. ![This is how the current html code looks like](https://raw.githubusercontent.com/wendahere/JAWS/master/Images/29-1.PNG).
This is how the current code looks like.

We were tasked to change the IP address of the esp32.
Adding this line changes the IP address:
ap.ifconfig(('192.168.16.4', '255.255.255.0', '192.168.16.1', '8.8.8.8'))

We are group 6, this it is "16" after the second fool-stop at the IP address. 
At first I had difficulties with this. The shell output had no error but I could not access the site, it kept writing connection failed even though it was working earlier in the morning. I realized only that I had removed all the connections and that made me unable to connect to the site. I reconnected the pins and I was able to access the site again.

[This is the current code](https://github.com/wendahere/JAWS/blob/master/Content/MotorANDUltrasoniccodes/M%26TMARK3%23Version1.py).

###More progress on dropdown menu
Initially Jayvien added a dropdown menu with no functions. (below) The dropdown portion also has problems, it is too far to the left.
![functions.](
https://raw.githubusercontent.com/wendahere/JAWS/master/Images/25-1.PNG) 

I made changes to the code to enable the dropdown menu to select medium to detect distance. I also change style of the button and changed position of the dropdown to relative instead of absolute. I had troubles changing the style of the button at first as if I removed :hover, the dropdown will not work properly, it will display the list without hovering the button.

I learned that I should not ONLY change the hover button but also the button itself without putting the class infront. Putting the class will disable the dropdown function, it will act as if hover was not written. Below is the working version. [CUrrent code.](https://github.com/wendahere/JAWS/blob/master/Content/MotorANDUltrasoniccodes/M%26TMARK5%23Version1.py)
 ![dropdown](https://raw.githubusercontent.com/wendahere/JAWS/master/Images/30-1withdropdown.PNG)

###1st Feb 2020

I Met up with Sean to do more work.
I did soldering while Sean did design for stripboard.
After showing my html web controller I realized that the distance unit was wrong. It was mm instead of cm.


#Week 17


Did laser cutting, had error in designs, so Allen had to redesign and re-cut tomorrow. Did 3D printing at home for sensor casing.

Met up online to do code. 

Initially I tried using PCA9685, I used pip to install adafruit_pca96685 to control the servo.

We later discussed and decided not to use PCA9685 as it adds more difficulty and reduces usage of few pins only. 

I did standalone code for servo control, move clockwise and anti-clockwise.

Added buttons to control servo on web, changed Stop to red. 
[Current code](https://github.com/wendahere/JAWS/blob/master/Content/MotorANDUltrasoniccodes/M%26TMARK7%23Version1.py). Below is the most updated image.

![Image update](https://raw.githubusercontent.com/wendahere/JAWS/master/Images/4%20feb%20update.PNG)

Jayvien made OLED code with Ultrasonic sensor.
I helped to make it into a function.

#Week 18

I used the OLED function and put it into the main code. Current code has Motors, Ultrasonic sensor, OLED and servo. It is currently at first version.

I did the voltage divider code and soldered the circuit. I have added heat shrink and tape to cover any exposed wires. ![VoltDivider](https://raw.githubusercontent.com/wendahere/JAWS/master/Images/VoltageDivider.jpeg)

Voltage Divider code is here. ESP32 pins can read input up to 3.3v. The batteries in series is 8.4v. The voltage divider is made such that 8.4v will be reduced to 3.3vs. ESP32 will read. If 3.3v is read, it means that batteries are at max capacity, 8.4v . Math is CVolt= (value/4095)*3.3*4 . Output will be from 0 to 4095, we have to change this to show the current battery voltage. Voltage is stepped down about 4 times, thus (value/4095)*3.3*4, will get voltage out of 8.4v.

I followed this [guide](https://randomnerdtutorials.com/esp8266-adc-reading-analog-values-with-nodemcu/)

#Week 19

###Monday 17/2/2020

Finally tested the code and it had trouble running. I was very frustrated as I kept pushing for a test but the electrical components were not soldered and changing to breadboard was very troublesome.

I asked Vincent for help and he told me my indentation was wrong. I used an older working version of the code and slowly copied the new code into the working version while editing the indentation. The HTML portion works and I am confident the motors will work but we have to wait till tomorrow to test.

[Current Code Mark 9](https://github.com/wendahere/JAWS/blob/master/Content/MotorANDUltrasoniccodes/M%26TMARK9%23Version1.py)

I plan to test the motors first, thus the other components in the code are in comment, when the motors work, I will remove the comments for servo and test that and so on.

###Tuesday 18/2/2020

I used mark9 code.

The motors initially only ran on one side, but was fixed. Error was the pins for one side of the motor was wrong.

I then tested the ultrasonic transducer and it works.

The servo does not work.

The error was int was not callable. My mistake was I set the function name for moving servos and if else statement for moving servo to be the same, thus had that error. I made updated the code to [mark10](https://github.com/wendahere/JAWS/blob/master/Content/MotorANDUltrasoniccodes/M%26TMARK10%23Version1.py) and it worked.

However, there was issue stopping the servo. When I pressed stop button, the web link will change but JAWS state remained the same. I realised that the capital letter for if else statement was different and I standardized it and it worked. [Mark 11](https://github.com/wendahere/JAWS/blob/master/Content/MotorANDUltrasoniccodes/M%26TMARK11%23Version1.py)

I added voltage divider code to the main code, [Mark 12](https://github.com/wendahere/JAWS/blob/master/Content/MotorANDUltrasoniccodes/M%26TMARK12%23Version1.py).