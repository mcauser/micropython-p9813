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

# TinyS2 (esp32s2)
# clk = Pin(4, Pin.OUT)
# data = Pin(5, Pin.OUT)

# Wemos D1 Mini (esp8266)
# clk = Pin(4, Pin.OUT)
# data = Pin(5, Pin.OUT)

# Bit-banged, 10 LEDs, auto-write off
num_leds = 10
auto_write = False
chain = p9813.P9813_BITBANG(clk, data, num_leds, auto_write)

# Set the first LED to red
chain[0] = (255, 0, 0)

# Set the second LED to green
chain[1] = (0, 255, 0)

# Set the third LED to blue
chain[2] = (0, 0, 255)

# With auto-write off, changes are not seen until you call write()
chain.write()

# Get second LED colour
(r, g, b) = chain[2]

# Print as hex colour
print(f"{r:02X}{g:02X}{b:02X}")
# prints 00FF00
