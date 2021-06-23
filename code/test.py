from gpiozero import *
import time

pin = GPIODevice(18)
while True:
    pin.toggle()
    time.sleep(500)