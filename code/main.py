#import pigpio
import time
#from pwm import *
from server import *
from settings import *

#pi = pigpio.pi()
#pump = PWM(pi, 18, 20) 

def main():
    settings = Settings()
    if (settings.get_start_server()):
        start_server(settings.get_port())

def close():
    pump.stop()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        close()        
        print ("Pumped turned off")
