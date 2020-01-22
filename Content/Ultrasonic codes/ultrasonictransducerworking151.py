import machine
import sys
import time
from machine import Pin
import utime


time.sleep(1) #Just for everything to settle down



while True:
  trig=machine.Pin(25, machine.Pin.OUT)
  trig.off() #//stop reading
  utime.sleep_us(2)
  trig.on()
  utime.sleep_us(10)
  trig.off()
  echo=machine.Pin(26, machine.Pin.IN)
  while echo.value() == 0:
    pass
  t1 = utime.ticks_us()
  while echo.value() == 1:
    pass
  t2 = utime.ticks_us()
  cm = (t2 - t1) / 58.0
  print(cm)
  utime.sleep(2)