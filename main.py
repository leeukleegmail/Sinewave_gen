import math
from machine import I2C, Pin

import mcp4725

i2c = I2C(scl=Pin(5), sda=Pin(4))
i2c.scan()

dac = mcp4725.MCP4725(i2c, mcp4725.BUS_ADDRESS[0])

while True:
    for i in range(4095, 0, -50):
        dac.write(1400 + int(1240 * (math.sin(2 * math.pi * i / 4095))))
