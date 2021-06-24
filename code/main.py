import pigpio
import time
from pwm import *

pi = pigpio.pi()
pump = PWM(pi, 18, 100) 

def main():
    pump.start()

def close():
    pump.stop()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        close()        
        print ("Pumped turned off")
