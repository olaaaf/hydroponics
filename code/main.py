import pigpio
import time
from pwm import *
from server import *

pi = pigpio.pi()
pump = PWM(pi, 18, 20) 

def main():
    pass

def close():
    pump.stop()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        close()        
        print ("Pumped turned off")
