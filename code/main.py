#import pigpio
import time
#from pwm import *
from server import *
from settings import *
from schedule import *

#pi = pigpio.pi()
#pump = PWM(pi, 18, 20) 

def main():
    #Get the settings
    settings = Settings()
    #pump.change_percentage(settings.get_pump_intensity())
    #sch = Schedule(settings.get_schedule(), pump.start, pump.stop)
    #sch.launch()
    #Launch the server if the settings say so
    if (settings.get_start_server()):
        start_server(settings)

def close():
    pump.stop()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        close()        
        print ("Pumped turned off")
