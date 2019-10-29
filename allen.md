# Allen's Blog
## Week 1 (14/9/19 - 19/9/19):
## Week 2 (21/9/19 - 25/9/19):
### Coding with BBC micro:bit
This week we learnt how to code python using the BBC micro:bit. Our homework is to code a space invaders game.
After several trials and errors, I managed to come up with a working code for the game. The below is the code for the game.
![alt text](https://imgur.com/LLkHFSz.png)

This is a small preview on how the game works. The "alien" drops from the first line on top, the player's game is to maneuver the spacecraft at the bottom by either going left and right by pressing the respective buttons to evade the alien. The game ends once the alien collides with the spacecraft.
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/T7CeutXWiZE/0.jpg)](http://www.youtube.com/watch?v=T7CeutXWiZEE)

As previosuly mentioned, I didn't get the code correctly the first time, it was only after I meticulously rechecked my code, I realised what went wrong.

The first problem was I forgot to add in the colon signs after my If statements.
![alt text](https://imgur.com/WMcqX5b.png)

To fix this, I simply added the colon signs where necessary (i.e. Lines 13 and 16).

The second problem was after running the program, when the "alien" doesn't hit my spacecraft and goes out of bounds, the game doesn't "reset", and everything just froze. An example of this problem is this video below.
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/hX4ReSyuBTU/0.jpg)](http://www.youtube.com/watch?v=YhX4ReSyuBTU)

This is the first version of the code that the second problem came from.
![alt text](https://i.imgur.com/rwFM5x2.png)

As you can see, there is no code that "resets" the game when the "alien" goes out of bounds.

To fix this, I added several new lines of codes to allow the game to continue when the "alien" goes out of bounds. Hence, the game will continue to run indefintely until it collides with the spacecraft.
The below is the new lines of codes I introduced.

![alt text](https://imgur.com/p7fK6il.png)

One obstacle that I faced is how the numbering system of LED lights on the BBC micro:bit works. I keep forgetting that it starts counting from 0 instead of 1. Therefore, this made troubleshooting the problems I faced slighty more challenging. In the end, I was able to grasp the basics, and able to come out with new codes to solve the issue of the "alien" going out of bounds causing the game to freeze.

For the readers that are aspiring to take up this mini project, I would like to give you a couple tips on how to code a successful code.
1. Patience. You must be patient while coding. Sometimes, it is better to take a step back and map out a process plan on how you are going to code, rather than typing the code immediately. This way, when you or other people look at your code, it is much more readable and easier to edit.
2. Perserverance. Setbacks are common, do not get discouraged when your code doesn't work out the first time. You must be actively trying to find new solutions on how to solve the problems that get in your way.
3. Curiousity. Having a curious mind is important, because this kind of mindset will help prepare you to face any challenges that might come into your way. Always be hungry for knowledge, you will constantly improve.
I believe that you will be able to do this mini project if you follow this 3 tips.

### Thony IDE
Over the weekend, I have watched a two You-tube videos on Thonny IDE, a platform used to code python. 
Out of the [two videos](https://www.youtube.com/watch?v=lWaCl0WjNZI) I watched, I will reccomend [this one](https://www.youtube.com/watch?v=nwIgxrXP-X4). The person is quite clear in narrating making it easy for people to follow. 
He gives a brief introduction on what Thonny is, and shows us the functions of Thonny with simple demonstrations to not overwhelm beginners. 
All in all, it is a terrific video for beginners to watch to get started on python programming using Thonny.

### Python Programming
I have also watched a video on python programming, and I think that it is quite helpful to beginners. Here is the [link](https://www.youtube.com/watch?v=N4mEzFDjqtA).

Pros:

- Different topics covered in the video is timestamped in the description bar.
- Goes through almost everything a beginner needs to know about python programming.
- Pleasant to watch, narrator is enthusiatic and clear in articulating.

Cons:
- Need to watch the video in order to know what is being taught, cannot open video in background and expect yourself to follow.
- Need to know a little bit of programming (other programming languages) beforehand.

