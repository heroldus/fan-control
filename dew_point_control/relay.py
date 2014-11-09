# coding=utf-8
import RPi.GPIO as GPIO
from config import Config

class RelayService():

    def __init__(self, relay_gpio_pins):
        self.pins = relay_gpio_pins
        GPIO.setmode(GPIO.BOARD)
        self.setup_pins()

    def setup_pins(self):
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, Config.RELAY_OFF)

    def switch_on(self, nr):
        self.switch(nr, Config.RELAY_ON)

    def switch_off(self, nr):
        self.switch(nr, Config.RELAY_OFF)

    def switch(self, nr, state):
        GPIO.output(self.pins[nr], state)




