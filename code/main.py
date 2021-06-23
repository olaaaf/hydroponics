from gpiozero import *
from pwm import *
import time
import _thread

def main():
    percentage = 5.0
    port = PWM(4, percentage)
    port.start()
    for i in range(100):
        port.change_part(i)
        time.sleep(0.07)
    input()
    print("Exiting...")
    port.stop()

if __name__ == '__main__':
    main()
