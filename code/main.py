import pigpio
from pwm import *
from server import *
from settings import *
from schedule import *

pi = pigpio.pi()
pump = PWM(pi, 18, 20) 
settings = None
schedule = None

def main():
    #Get the settings
    global settings, schedule, pump
    settings = Settings(update_settings)
    schedule = Schedule(settings.get_schedule(), pump.start, pump.stop)
    schedule.launch()
    #Launch the server if the settings say so
    if (settings.get_start_server()):
        start_server(settings)

def update_settings():
    global settings, pump
    pump.change_percentage(settings.get_pump_intensity())
    schedule.update_schedule(settings.get_schedule())

def close():
    pump.stop()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        close()        
        print ("Pumped turned off")
