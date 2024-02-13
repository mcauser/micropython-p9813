# SPDX-FileCopyrightText: 2017 Mike Causer <https://github.com/mcauser>
# SPDX-License-Identifier: MIT

"""
MicroPython P9813 RGB LED driver
https://github.com/mcauser/micropython-p9813
"""

from machine import Pin
from time import sleep_ms
from urandom import getrandbits
import p9813

# TinyPICO (esp32)
clk = Pin(4, Pin.OUT)
data = Pin(14, Pin.OUT)

# Bit-banged, 10 LEDs, auto-write off
num_leds = 10
chain = p9813.P9813_BITBANG(clk, data, num_leds, False)


def random_colors(sleep):
    for _ in range(50):
        for i in range(num_leds):
            chain[i] = (getrandbits(8), getrandbits(8), getrandbits(8))
        chain.write()
        sleep_ms(sleep)


# Random colours
random_colors(10)
