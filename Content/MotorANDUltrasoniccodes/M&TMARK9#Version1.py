try:
    import usocket as socket
except:
    import socket
  
from machine import Pin
import network
from machine import PWM

import esp
esp.osdebug(None)

import gc
gc.collect()

import machine
import sys
import time
import utime

ssid = 'WenDaESP'
password = 'meowmeowmeow'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password, authmode=3)
ap.ifconfig(('192.168.16.4', '255.255.255.0', '192.168.16.1', '8.8.8.8'))

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

#Pinout

Motor1a = Pin(2, Pin.OUT) #Purple
Motor1b = Pin(0, Pin.OUT) #Green
Motor2a = Pin(4, Pin.OUT) #Grey
Motor2b = Pin(16, Pin.OUT) #White
eA = Pin(15, Pin.OUT) #Green
eB = Pin(17, Pin.OUT) #Blue
trig=machine.Pin(25, machine.Pin.OUT)
echo=machine.Pin(26, machine.Pin.IN)

cm =0
jaws_state="Stop" #Starting position is Stop, this will be reflected on the ESP html page

#Transducer portion

"""
def depth(): #default is air
    t1=0
    t2=0
    trig.off() #//stop reading
    utime.sleep_us(2)
    trig.on()
    utime.sleep_us(10)
    trig.off()
    
    while echo.value() == 0:
        pass
        t1 = utime.ticks_us()
    while echo.value() == 1:
        pass
        t2 = utime.ticks_us()
    cmd = ((t2 - t1)*(340/00000))/2;
    print(cm)
    utime.sleep(2)
    return cmd

cm = depth() #Run transducer once

def depthwood(): #wood depth
    t1=0
    t2=0
      #Transducer portion
    trig.off() #//stop reading
    utime.sleep_us(2)
    trig.on()
    utime.sleep_us(10)
    trig.off()
    
    while echo.value() == 0:
        pass
        t1 = utime.ticks_us()
    while echo.value() == 1:
        pass
        t2 = utime.ticks_us()
    cmw = ((t2 - t1)*(12.25/10000))/2;
    print(cmw)
    utime.sleep(2)
    return cmw

def depthice(): #ice depth
    t1=0
    t2=0
      #Transducer portion
    trig.off() #//stop reading
    utime.sleep_us(2)
    trig.on()
    utime.sleep_us(10)
    trig.off()
    
    while echo.value() == 0:
        pass
        t1 = utime.ticks_us()
    while echo.value() == 1:
        pass
        t2 = utime.ticks_us()
    cmi = ((t2 - t1)*(4000/10000))/2;
    
    print(cmi)
    utime.sleep(2)
    return cmi
"""

def Forward(): 
    
    Motor1a.value(1)
    Motor1b.value(0)
    Motor2a.value(1)
    Motor2b.value(0)
    eA.value(1)
    eB.value(1)

def Backward():
    
    Motor1a.value(0)
    Motor1b.value(1) 
    Motor2a.value(0)
    Motor2b.value(1)
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

#SERVO PART
"""
def servostop():
    servo = machine.PWM(servopin, freq=0)  
    servo.duty(0)    
    
def servoup():
    servo = machine.PWM(servopin, freq=1000)  #50 for clockwise
    servo.duty(500)
    time.sleep_ms(500)  #ensure that the sensor doesnt keep moving
    servostop()
    
def servodown():
    servo = machine.PWM(servopin, freq=50)
    servo.duty(500)
    time.sleep_ms(500)  #ensure that the sensor doesnt keep moving
    servostop()
"""

def web_page():

  
    html = """<html><head><title>JAWS Controller</title><meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <style>html {font-family: Helvetica;display: inline-block;margin: 0px auto;text-align: center;
    }h1 {color: #0F3376;padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block;background-color: #e7bd3b;border: none;
    border-radius: 4px;color: white;padding: 16px 40px;text-decoration: none;font-size: 30px;margin: 2px;cursor: pointer;}
    .button2 {background-color: #4286f4;} .button6 {background-color: #4286f4; font-size: 15px; padding: 10px 24px;} .button7{background-color: #f44336; font-size: 15px; padding: 10px 24px;} .button8{background-color: #4286f4; font-size: 15px; padding: 10px 24px;} .button5{background-color: #f44336;}


    
    </style>
    </head>
    <body>
    <h1>JAWS WIFI Controller</h1><p>JAWS state:<strong>
    """ + jaws_state + """    
    </strong></p>
    <p>Depth:<strong>
    """ + str(cm) + """    
    </strong></p>
    <p><a href="/?Forward=true"><button class="button">Up</button></a></p>
    <p><a href="/?Left=true"><button class="button button2">Left</button></a><a href="/?Right=true"><button class="button button2">Right</button></a></p>
    <p><a href="/?Backward=true"><button class="button button4">Backward</button></a></p>
    <p><a href="/?Stop=true"><button class="button button5">Stop</button></a></p>
    <p>
    <font face="verdana" color="green">Sensor Control</p></font>
    <p><a href="/?Servo=up"><button class="button button6">Up</button></a></p>
    <p><a href="/?Servo=Stop"><button class="button button7">Stop</button></a></p>
    
    <p><a href="/?Servo=down"><button class="button button8">Down</button></a></p>
    <style>



    .dropdown-content {
      display: none;
      position: relative;
      background-color: #f9f9f9;
      min-width: 160px;
      box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
      z-index: 1;
    }

    .dropdown-content a {
      color: black;
      padding: 12px 16px;
      text-decoration: none;
      display: block;
    }

    .dropdown-content a:hover {background-color: #f1f1f1}

    .dropdown:hover .dropdown-content {
      display: block;
    }

    .dropdown:hover .dropbtn {
      background-color: #3e8e41;
      width: 300px;
      height: 40px;
      font-size: 20px;
      border-radius: 10px;
      color: white;
    }

    .dropbtn {
      background-color: #3e8e41;
      width: 300px;
      height: 40px;
      font-size: 20px;
      border-radius: 10px;
      color: white;
    }

    </style>
    </head>
    <body>

    <div class="dropdown">
      <button class="dropbtn">Medium</button>
      <div class="dropdown-content">
      <a href="/?Air">Air</a>
      <a href="/?Wood">Wood</a>
      <a href="/?Ice">Ice</a>
      </div>
    </div>
        </body>
        </html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request) #determine after the ip address, what motion is JAWS in
  print('Content = %s' % request)
      
  forward = request.find('/?Forward=true')
  backward = request.find('/?Backward=true')
  left = request.find('/?Left=true')
  right = request.find('/?Right=true')
  backward = request.find('/?Backward=true')
  stop = request.find('/?Stop=true')
      
      #Medium
      
  air = request.find('/?Air')
  wood = request.find('/?Wood')
  ice = request.find('/?Ice')
      
      #Servo motor control ((Move sensor)
      
  servoup = request.find('/?Servo=up')
  servostop = request.find('/?Servo=stop')
  servodown = request.find('/?Servo=down')
  
  if forward == 6: #if the 6th position onwards is eg(Forward), JAWS will run Forward(). visa versa
    print('FORWARD')
    Forward()
    jaws_state = "Forward"
    
  if backward == 6:
    print('BACKWARD')
    Backward()
    jaws_state = "Backward"
    
  if right == 6:
    print('RIGHT')
    Right()
    jaws_state = "Right"
    
  if left == 6:
    print('LEFT')
    Left()
    jaws_state = "Left"
    
  if stop == 6:
    print('STOPPED')
    Stop()
    jaws_state = "Stopped"

     #TRANSDUCER MEDIUM PART
      
  if air == 6:
    print('Dist in Air')
    Stop()
    jaws_state = "Reading Distance (Medium: Air)"
    depth()
    cm = depth()
        
  if wood == 6:
    print('Dist in Wood')
    Stop()
    jaws_state = "Reading Distance (Medium: Wood)" 
    depthwood()
    cm = depthwood()
        
  if ice == 6:
    print('Dist in Ice')
    Stop()
    jaws_state = "Reading Distance (Medium: Ice)"
    depthice()
    cm = depthice()
       
        #SERVO CONTROL PART

  if servoup == 6:
    print('Sensor Up')
    Stop()
    jaws_state = "Sensor moving up"
    servoup()
          
  if servostop == 6:
    print('Sensor Stop')
    Stop()
    jaws_state = "Sensor stop moving"
    servostop()      
          
  if servodown == 6:
    print('Sensor moving down')
    Stop()
    jaws_state = "Sensor moving down"
    servodown()           


  response = web_page()
  conn.sendall(response)
  conn.close()




