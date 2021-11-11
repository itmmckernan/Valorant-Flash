import serial

class gpio:
    BCM = "BCM"
    OUT = "OUTPUT"
    HIGH = "HIGH"
    LOW = "LOW"
    serial = ...
    def __init__(self):
        print('fakeGPIO started')
        self.serial = serial.Serial(
            port='COM12',
            baudrate=9600
        )

    def setmode(self, opt):
        print("setmode to {}".format(opt))

    def setup(self, pin, opt):
        print("set pin mode of {} to {}".format(pin, opt))

    def output(self, pin, state):
        if state == gpio.HIGH:
            self.serial.write(bytes('\x0F', 'ascii'))
        elif state == gpio.LOW:
            self.serial.write(bytes('\x0A', 'ascii'))
        print("set pin state of {} to {}".format(pin, state))