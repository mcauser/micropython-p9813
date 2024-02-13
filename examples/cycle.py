# SPDX-FileCopyrightText: 2017 Mike Causer <https://github.com/mcauser>
# SPDX-License-Identifier: MIT

"""
MicroPython P9813 RGB LED driver
https://github.com/mcauser/micropython-p9813
"""

from machine import Pin
from time import sleep_ms
import p9813

# TinyPICO (esp32)
clk = Pin(4, Pin.OUT)
data = Pin(14, Pin.OUT)

# Bit-banged, 10 LEDs, auto-write off
num_leds = 10
chain = p9813.P9813_BITBANG(clk, data, num_leds, False)


def cycle(color, sleep):
    for i in range(num_leds):
        for j in range(num_leds):
            chain[j] = (0, 0, 0)
        chain[i % num_leds] = color
        chain.write()
        sleep_ms(sleep)


# Test colours
red = (16, 0, 0)
green = (0, 16, 0)
blue = (0, 0, 16)
cyan = (0, 16, 16)
magenta = (16, 0, 16)
yellow = (16, 16, 0)
white = (16, 16, 16)
black = (0, 0, 0)
colors = [red, green, blue, cyan, magenta, yellow, white, black]

# Illuminate the LEDs one-by-one
for color in colors:
    cycle(color, 10)
