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

##TL:DR
##Conclusion: 
My code was successful. The code can be seen below or [here](https://pastebin.com/sCmUxWWL).

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

####Pros:
- Goes through everything of Python, including installation of the program required
- Very clear on explanation and understandable English
- Considered short, compared to 4 hours tutorial 
- Everything packed into 1 hour 30mins
- Rather new video (2019) and updated channel
####Cons: 
- Video volume not consistent, start and end of video is VERY loud, please be careful
- Have to pause the video if you are following


##Journal for Week 2
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

####Traceback (most recent call last):File "<stdin>", line 13, in <module>ValueError: index out of bounds

At the the end, once any value exceeds the boundary, there will be this error, index out of bounds. I have tried using arrays but the value will still get out of bound of the array. The only solution I have for this is to simply reset the game before any value gets out of bounds, which includes the player.

###Revised Version of code
I rewrote the code from scratch after finding out my mistake, was stumped and could not figure out why after an hour of searching, therefore I started from scratch and used another method to move the spacecraft instead.


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
    
   #when alien and player collide, game will end and loop game over!

   if alienx == spacecraft and alieny == 4:
        break

        
   sleep(250)
        
display.scroll("GAME OVER!", loop=True)

###Space Invaders Demo

[![Space Invaders!](http://img.youtube.com/vi/JxIyh3bOaRo/0.jpg)](http://www.youtube.com/watch?v=JxIyh3bOaRo)



