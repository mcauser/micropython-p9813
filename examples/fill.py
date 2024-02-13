# SPDX-FileCopyrightText: 2017 Mike Causer <https://github.com/mcauser>
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

# Test colours
red = (16, 0, 0)
green = (0, 16, 0)
blue = (0, 0, 16)

# Set all LEDs red
chain.fill(red)

# Set all LEDs green
chain.fill(green)

# Set all LEDs blue
chain.fill(blue)

# Turn off all LEDs
chain.fill((0, 0, 0))

# Set all LEDs orange
chain.fill((0xFF, 0x99, 0x00))

# Turn off all LEDs
chain.reset()
