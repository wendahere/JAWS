from machine import Pin, I2C, ADC
import ssd1306
from time import sleep
import machine
import sys
import time

pot = ADC(Pin(33))
pot.atten(ADC.ATTN_11DB)

value=0

def show():

    while True:
        
        value = pot.read()
        CVolt= (value/4095)*3.3*4 
    
        print(CVolt)
        time.sleep(1)
        return CVolt

CVolt = show()

#OLED MAIN CODE

i2c = I2C(-1, scl=Pin(22), sda=Pin(21))#SDA Yellow & SCL White; 3.3V Red & Gnd Black

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while (1):
    CVolt = round(show())

    oled.text('SAFElol', 0, 0)
    time.sleep(3)

    oled.show()

    oled.fill(0)

    oled.text(''+str(CVolt), 0, 0) #remove voltage if it doesnt work
    time.sleep(3)

    oled.show()
