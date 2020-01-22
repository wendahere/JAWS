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

led = Pin(21, Pin.OUT)
leftfirst = Pin(0, Pin.OUT) #Pure White
leftsecond = Pin(16, Pin.OUT) #Grey
rightfirst = Pin(5, Pin.OUT) #Green
rightsecond = Pin(19, Pin.OUT) #Purple
eA = Pin(15, Pin.OUT) #Green
eB = Pin(21, Pin.OUT) #Blue

jaws_state="Stop"

def web_page():

  
  html = """<html><head> <title>WEB Controller</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 13.14px;}p{font-size: 24px;}
  
  .button{
   background-color: #4286f4;
   border: none;
   color: white;
   padding: 16px 40px;
   text-align: center;
   text-decoration: none;
   display: inline-block;
   font-size: 30px;
   margin-right: 500px;
   cursor: pointer;
   }
   
  .button2{
   background-color: #000000;
   border: none;
   color: white;
   padding: 16px 40px;
   text-align: center;
   text-decoration: none;
   display: inline-block;
   font-size: 30px;
   margin-right: 700px;
   cursor: pointer;
   }
   
  .button3{
   background-color: #4286f4;
   border: none;
   color: white;
   padding: 16px 40px;
   text-align: center;
   text-decoration: none;
   display: inline-block;
   font-size: 30px;
   margin-left: 400px;
   cursor: pointer;
   }
   
   .button4{
   background-color: #4286f4;
   border: none;
   color: white;
   padding: 16px 30px;
   text-align: center;
   text-decoration: none;
   display: inline-block;
   font-size: 30px;
   margin-right: 500px;
   cursor: pointer;
   }
   
   </style>
   </head>
   <body>
   
  <h1>WIFI CONTROLLER</h1>
  <p>JAWS state: <strong>""" + jaws_state + """</strong>
  </p><p><a href="/?forward"><button class="button">FORWARD</button></a>
  </p><p><a href="/?left"><button class="button button2">LEFT</button></a>
  <a href="/?right"><button class="button button3">RIGHT</button></a>
  </p><p><a href="/?backward"><button class="button button4">BACKWARD</button></a>
  </p></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  forward = request.find('/?forward')
  backward = request.find('/?backward')
  left = request.find('/?left')
  backward = request.find('/?right')
  if forward == 6:
    print('FORWARD')
    leftfirst(1)
    rightfirst(1)
    jaws_state = "Forward"
    
  if backward == 6:
    print('BACKWARD')
    leftsecond(1)
    rightsecond(1)
    jaws_state = "Backward"
    
  if right == 6:
    jaws_state = "Right"
    
  if left == 6:
    jaws_state = "Left"
      
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
