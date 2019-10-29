# Allen's Blog
## Week 1 (14/9/19 - 19/9/19):
## Week 2 (21/9/19 - 25/9/19):
### Coding with BBC micro:bit
This week we learnt how to code python using the BBC micro:bit. Our homework is to code a space invaders game.
After several trials and errors, I managed to come up with a working code for the game. The below is the code for the game.
![alt text](https://imgur.com/LLkHFSz)
This is a small preview on how the game works. The "alien" drops from the first line on top, the player's game is to maneuver the spacecraft at the bottom by either going left and right by pressing the respective buttons to evade the alien. The game ends once the alien collides with the spacecraft.
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/T7CeutXWiZE/0.jpg)](http://www.youtube.com/watch?v=T7CeutXWiZEE)
As previosuly mentioned, I didn't get the code correctly the first time, it was only after I meticulously rechecked my code, I realised what went wrong.

The first problem was I forgot to add in the colon signs after my If statements.
![alt text](https://imgur.com/WMcqX5b)
To fix this, I simply added the colon signs where necessary (i.e. Lines 13 and 16).

The second problem was after running the programme, when the "alien" doesn't hit my spacecraft and goes out of bounds, the game doesn't "reset", and everything just froze. An example of this problem is this video below.
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/hX4ReSyuBTU/0.jpg)](http://www.youtube.com/watch?v=YhX4ReSyuBTU)
To fix this, I added several new lines of codes to allow the game to continue when the "alien" goes out of bounds. Hence, the game will continue to run indefintely until it collides with the spacecraft.
The below is the new lines of codes I introduced.
![alt text](https://imgur.com/p7fK6il)

One obstacle that I faced is how the numbering system of LED lights on the BBC micro:bit works. I keep forgetting that it starts counting from 0 instead of 1. Therefore, this made troubleshooting the problems I faced slighty more challenging. In the end, I was able to grasp the basics, and able to come out with new codes to solve the issue of the "alien" going out of bounds causing the game to freeze.

For the readers that are aspiring to take up this mini project, I would like to give you a couple tips on how to code a successful code.
1. Patience, 
2. Perserverance,
3. 
I believe if 

### Thony IDE
Over the weekend, I have watched a couple You-tube videos on Thonny IDE, a platform 
