# SPDX-FileCopyrightText: 2024 Mike Causer <https://github.com/mcauser>
# SPDX-License-Identifier: MIT

"""
MicroPython P9813 RGB LED driver
https://github.com/mcauser/micropython-p9813
"""

from machine import Pin
import p9813

# TinyPICO (esp32)
clk = Pin(4, Pin.OUT)
data = Pin(14, Pin.OUT)

# Bit-banged, 10 LEDs, auto-write on
num_leds = 10
chain = p9813.P9813_BITBANG(clk, data, num_leds, True)


def refresh_rate_test(count):
    red = (16, 0, 0)
    green = (0, 16, 0)
    blue = (0, 0, 16)
    colors = [red, green, blue]
    for i in range(count):
        chain[i % num_leds] = colors[i % 3]


# For ~4 seconds, rapidly draw red, green, blue incrementally.
# Roughly 2x slower than Software SPI at baud 100_000.
# Running the same test will instead of showing solid white LEDs,
# show them all flickering as it rapidly draws the colours.
refresh_rate_test(500)
