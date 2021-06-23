from gpiozero import OutputDevice
import time
import _thread

class PWM:
    on = False
    frequency = 60.0

    def __init__(self, port, part):
        self.port = OutputDevice(port)
        self.part = part/100.0

    def start(self):
        self.on = True
        try:
            _thread.start_new_thread(self.cycle, ())
        except SystemExit:
            print(code)

    def stop(self):
        self.on = False
        self.port.off()

    def change_part(self, part):
        self.part = part/100.0

    def cycle(self):
        while self.on:
            self.port.on()
            time.sleep(self.part / self.frequency)
            self.port.off()
            time.sleep((1 - self.part) / self.frequency)
