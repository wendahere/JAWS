from machine import Pin, I2C
import ssd1306
from time import sleep
import time

i2c = I2C(-1, scl=Pin(22), sda=Pin(21))#SDA Yellow & SCL White; 3.3V Red & Gnd Black

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('SAFElol', 0, 0)
time.sleep(3)

oled.show()

oled.fill(0)

oled.text('welp', 0, 0)
time.sleep(3)

oled.show()
