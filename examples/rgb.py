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


# Convert hex RRGGBB to (r,g,b)
def hex_to_rgb(hex_str):
    return tuple(int(hex_str[i : i + 2], 16) for i in (0, 2, 4))


# Orange FF9900 -> (255, 153, 1)
hex_to_rgb("FF9900")

# Set the first LED to red
chain[0] = hex_to_rgb("FF0000")

# Set the second LED to green
chain[1] = hex_to_rgb("00FF00")

# Set the third LED to blue
chain[2] = hex_to_rgb("0000FF")

# Set the fourth LED to yellow
chain[3] = hex_to_rgb("FFFF00")

# Set the fifth LED to magenta
chain[4] = hex_to_rgb("FF00FF")

# Set the sixth LED to cyan
chain[5] = hex_to_rgb("00FFFF")
