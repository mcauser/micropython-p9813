# SPDX-FileCopyrightText: 2017 Mike Causer <https://github.com/mcauser>
# SPDX-License-Identifier: MIT

"""
MicroPython P9813 RGB LED driver
https://github.com/mcauser/micropython-p9813
"""

# traffic lights
# 0,1,2 = road A red,amber,green
# 3,4,5 = road B red,amber,green

from machine import Pin
from time import sleep_ms
import p9813

# TinyPICO (esp32)
clk = Pin(4, Pin.OUT)
data = Pin(14, Pin.OUT)

# Bit-banged, 6 LEDs, auto-write off
num_leds = 6
chain = p9813.P9813_BITBANG(clk, data, num_leds, False)

# Reset
chain.fill((0, 0, 0))
chain.write()

# How long (in ms) light is green
active = 4000
# How long light is amber
transition = 1000
# How long both lights red before one becomes green
pause = 500

# Colours
off = (0, 0, 0)
red = (255, 0, 0)
amber = (255, 194, 0)
green = (0, 255, 0)

# Initial state: red/red
chain[0] = red
chain[3] = red
chain.write()

while True:
    # red/red
    chain[3] = red
    chain[4] = off
    chain.write()
    sleep_ms(pause)

    # green/red
    chain[0] = off
    chain[2] = green
    chain.write()
    sleep_ms(active)

    # amber/red
    chain[1] = amber
    chain[2] = off
    chain.write()
    sleep_ms(transition)

    # red/red
    chain[0] = red
    chain[1] = off
    chain.write()
    sleep_ms(pause)

    # red/green
    chain[3] = off
    chain[5] = green
    chain.write()
    sleep_ms(active)

    # red/amber
    chain[4] = amber
    chain[5] = off
    chain.write()
    sleep_ms(transition)
