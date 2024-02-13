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


# Theatre-style crawling lights
# X..X..X.
# .X..X..X
# ..X..X..X
def theater_chase(color, wait):
    for _ in range(10):
        # 3 unique combinations in the pattern [100,010,001]
        for u in range(3):
            # for each LED
            for i in range(num_leds):
                # turn every third LED on, the others off
                if i % 3 == u:
                    chain[i] = color
                else:
                    chain[i] = (0, 0, 0)
            chain.write()
            sleep_ms(wait)


red = (16, 0, 0)

# Theatre-style crawling lights, in a given colour
theater_chase(red, 0)
