#Motor Control
import wifimgr
from time import sleep
import machine

Motor1a = Pin(0, Pin.OUT) #Purple
Motor1b = Pin(16, Pin.OUT) #Green
Motor2a = Pin(5, Pin.OUT) #Grey
Motor2b = Pin(19, Pin.OUT) #White
eA = Pin(15, Pin.OUT) #Green
eB = Pin(21, Pin.OUT) #Blue

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
# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  

# Main HTML
print("ESP OK")

def web_page():
    gpio_state="ON"
  
  html = """<html><head><title>ESP Web Server</title><meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"><style>html {font-family: Helvetica;display: inline-block;margin: 0px auto;text-align: center;
    }h1 {color: #0F3376;padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block;background-color: #e7bd3b;border: none;
    border-radius: 4px;color: white;padding: 16px 40px;text-decoration: none;font-size: 30px;margin: 2px;cursor: pointer;}
    .button2 {background-color: #4286f4;}</style></head><body><h1>ESP Web Server</h1><p>GPIO state:<strong>
    """ + gpio_state + """
    </strong></p>
    <p><a href="/?Forward=true"><button class="button">Up</button></a></p>
    <p><a href="/?Left=true"><button class="button button2">Left</button></a><a href="/?Right=true"><button class="button button2">Right</button></a></p>
    <p><a href="/?Backward=true"><button class="button button4">Backward</button></a></p>
    
    </body>
    
    </html>"""
    return html

try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind(('', 80))
  s.listen(5)
except OSError as e:
  machine.reset()

while True:
  try:
    conn, addr = s.accept()
    conn.settimeout(3.0)
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    conn.settimeout(None)
    request = str(request)
    print('Content = %s' % request)
    
    Forward = request.find('/?Forward=true')
    Back = request.find('/?Backward=true')
    Left = request.find('/?Left=true')
    Right = request.find('/?Right=true')

    if Forward == 6:
        print('Forward')
        Forward()
    if backward == 6:
        print('Backward')
        Backward()
    if left == 6:
        print('Left')
        Left()
    if Right == 6:
        print('Right')
        Right()

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
  except OSError as e:
    conn.close()
    print('Connection closed')