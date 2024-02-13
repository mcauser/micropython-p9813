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


def bounce(color, sleep):
    for i in range(4 * num_leds):
        for j in range(num_leds):
            chain[j] = color
        if (i // num_leds) % 2 == 0:
            chain[i % num_leds] = (0, 0, 0)
        else:
            chain[num_leds - 1 - (i % num_leds)] = (0, 0, 0)
        chain.write()
        sleep_ms(sleep)


# Test colours
red = (16, 0, 0)
green = (0, 16, 0)
colors = [red, green]

# Bounce a dark (off) LED back and forth
for color in colors:
    bounce(color, 0)
