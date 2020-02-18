from machine import Pin , ADC
from time import sleep

pot = ADC(Pin(33))
pot.atten(ADC.ATTN_11DB)

value = 0

while True:

    value = pot.read()
    CVolt= (value/4095)*3.3*4 
    
    
    
    print(CVolt)
    sleep(0.1)

