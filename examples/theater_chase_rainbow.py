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
def theatre_chase_rainbow(sleep):
    # cycle through all 256 colours, skipping 2/3s (86)
    for n in range(86):
        # 3 unique combinations in the pattern [100,010,001]
        for u in range(3):
            for i in range(num_leds):
                # turn every third LED on, the others off
                if i % 3 == u:
                    chain[i] = wheel((i + n * 3) % 255)
                else:
                    chain[i] = (0, 0, 0)
            chain.write()
            sleep_ms(sleep)


# Helper for converting 0-255 offset to a colour tuple
def wheel(offset):
    # The colours are a transition r - g - b - back to r
    offset = 255 - offset
    if offset < 85:
        return (255 - offset * 3, 0, offset * 3)
    if offset < 170:
        offset -= 85
        return (0, offset * 3, 255 - offset * 3)
    offset -= 170
    return (offset * 3, 255 - offset * 3, 0)


# Theatre-style crawling lights, in rainbow colours
theatre_chase_rainbow(0)
