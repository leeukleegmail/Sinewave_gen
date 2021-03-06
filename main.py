import math
from time import sleep

from machine import I2C, Pin

import mcp4725

i2c = I2C(scl=Pin(5), sda=Pin(4))
i2c.scan()

dac = mcp4725.MCP4725(i2c, mcp4725.BUS_ADDRESS[0])


def sine_wave():
    for i in range(4095, 0, -50):
        dac.write(500 + int(500 * (math.sin(2 * math.pi * i / 4095))))


def square_wave():
    dac.write(1240)
    sleep(0.5)
    dac.write(0)
    sleep(0.5)


def sawtooth_wave():
    start = 0
    max = 1040
    value = 0
    step = 100
    sleep_time = 0.01
    while value < max:
        value = value + step
        dac.write(value)
        sleep(sleep_time)
    while value > start:
        dac.write(value)
        value = value - step
        sleep(sleep_time)


while True:
    sine_wave()
    square_wave()
    sawtooth_wave()
