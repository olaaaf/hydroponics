import pigpio
import threading
import time

class PWM:
    frequency = 100
    hardware = True
    on = False

    def __init__(self, pi, port, percentage=50, hardware=True):
        self.pi = pi
        self.port = port
        self.percentage = percentage
        if not port in [12, 13, 18, 19] or not hardware:
            print ("Hardware PWM ports are: 12, 13, 18 and 19")
            print ("PWM port not included in hardware ports\nPWM will launch on a software thread...")
            self.hardware = False
            self.thread = threading.Thread(target=self.thread_update, name="PWM Thread on GPIO port " + str(port))

    def turn_off(self):
        self.pi.write(self.port, 0)

    def change_percentage(self, percentage):
        self.percentage = percentage 
        self.start()

    def start(self):
        self.on = True
        if self.hardware:
            #as the duty_cycle ranges from 0 to 1,000,000 percenatage needs to be
            #multiplied by 10,000
            self.pi.hardware_PWM(self.port, self.frequency, self.percentage * 10000)
        else:
            self.thread.start()

    def stop(self):
        self.on = False
        if self.hardware:
            self.pi.hardware_PWM(self.port, 0, 0)
    
    def is_on(self):
        return self.on
    
    def thread_update(self):
        while self.on:
            self.pi.write(self.port, 1)
            time.sleep((self.percentage / 100.0) / self.frequency)
            self.pi.write(self.port, 0)
            time.sleep((1.0 - self.percentage / 100.0) / self.frequency)
