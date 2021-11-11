from fakeGPIO import gpio
import time
gpio = gpio()

for i in range(50):
    gpio.output(69, gpio.HIGH)
    time.sleep(.08)
    gpio.output(69, gpio.LOW)
    time.sleep(.08)