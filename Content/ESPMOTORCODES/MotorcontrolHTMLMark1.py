try:
  import usocket as socket
except:
  import socket
  
from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'WenDaESP'
password = 'meow'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

Motor1a = Pin(0, Pin.OUT) #Purple
Motor1b = Pin(16, Pin.OUT) #Green
Motor2a = Pin(5, Pin.OUT) #Grey
Motor2b = Pin(19, Pin.OUT) #White
eA = Pin(15, Pin.OUT) #Green
eB = Pin(21, Pin.OUT) #Blue

jaws_state="Stop" #Starting position is Stop, this will be reflected on the ESP html page

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

def web_page():

  
  html = """<html><head><title>JAWS Controller</title><meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"><style>html {font-family: Helvetica;display: inline-block;margin: 0px auto;text-align: center;
    }h1 {color: #0F3376;padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block;background-color: #e7bd3b;border: none;
    border-radius: 4px;color: white;padding: 16px 40px;text-decoration: none;font-size: 30px;margin: 2px;cursor: pointer;}
    .button2 {background-color: #4286f4;}</style></head><body><h1>JAWS WIFI Controller</h1><p>JAWS state:<strong>
    """ + jaws_state + """
    </strong></p>
    <p><a href="/?Forward=true"><button class="button">Up</button></a></p>
    <p><a href="/?Left=true"><button class="button button2">Left</button></a><a href="/?Right=true"><button class="button button2">Right</button></a></p>
    <p><a href="/?Backward=true"><button class="button button4">Backward</button></a></p>
    <p><a href="/?Stop=true"><button class="button button5">Stop</button></a></p>
      </body>
    
    </html>"""
    return html

try:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  try:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request) #determine after the ip address, what motion is JAWS in
  print('Content = %s' % request)
  forward = request.find('/?forward')
  backward = request.find('/?backward')
  left = request.find('/?left')
  backward = request.find('/?right')
  stop = request.find('/?stop')
  
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
    jaws_state = "Stoped"
      
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  response = web_page()
  conn.send(response)
  conn.close()
