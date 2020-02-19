from machine import Pin, PWM
import time
import esp32

Motor1a = Pin(0, Pin.OUT) #White
Motor1b = Pin(16, Pin.OUT) #Grey
Motor2a = Pin(5, Pin.OUT) #Green
Motor2b = Pin(19, Pin.OUT) #Purple
eA = Pin(21, Pin.OUT) #Green
eB = Pin(15, Pin.OUT) #Blue

def Forward(): 
    
    Motor1a.value(1)
    Motor1b.value(0)
    Motor2a.value(0)
    Motor2b.value(1)
    eA.value(1)
    eB.value(1)

def Backward():
    
    Motor1a.value(0)
    Motor1b.value(1) 
    Motor2a.value(1)
    Motor2b.value(0)
    eA.value(1)
    eB.value(1)
    
def Left():
    
    Motor1a.value(0)
    Motor1b.value(0)
    Motor2a.value(1)
    Motor2b.value(0)
    eA.value(1)
    eB.value(1)

def Right():
    
    Motor1a.value(1)
    Motor1b.value(0)
    Motor2a.value(0)
    Motor2b.value(0)
    eA.value(1)
    eB.value(1)

def Stop():
    
    Motor1a.value(0)
    Motor1b.value(0)
    Motor2a.value(0)
    Motor2b.value(0)
    eA.value(1)
    eB.value(1)
    
def rest():
    
    stop()
    time.sleep(1)
    
while True:
    
    control = input()
    
    if control == 'w':
        Forward()
        time.sleep(1)
       # rest(1)
    elif control == 's':
        Backward()
        time.sleep(1)
       # rest(1)
    elif control == 'a':
        Left()
        time.sleep(1)
       # rest(1)
    elif control == 'd':
        Right()
        time.sleep(1)
      #  rest(1)
    elif control == 'q':
        Stop()
        time.sleep(1)
     #   rest(1)
    
    else:
        control.clear()