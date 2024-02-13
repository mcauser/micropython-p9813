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

# Set the first LED to red
chain[0] = (255, 0, 0)

# Set the second LED to green
chain[1] = (0, 255, 0)

# Set third LED to blue and forth LED magenta
chain[2:4] = [(0, 0, 255), (255, 0, 255)]

# Make all LEDs white
chain[:] = [(53, 53, 53)] * num_leds

# What colour is the forth LED?
print(chain[3])
# (255, 0, 255)

# How many LEDs in the chain again?
print(len(chain))
# 10

# What are the first two colours?
print(chain[0:2])
# [(255, 0, 0), (0, 255, 0)]

# What are all the colours?
print(chain)
# [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
