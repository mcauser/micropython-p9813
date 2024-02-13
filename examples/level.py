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

# Test colours
green = (0, 16, 0)
yellow = (16, 16, 0)
red = (16, 0, 0)
black = (0, 0, 0)

# 10 colour levels from ok (green) -> warning (yellow) -> error (red)
colors = [green, green, green, green, green, green, green, yellow, yellow, red]


def level(n):
    for i in range(num_leds):
        if n > i:
            chain[i] = colors[i]
        else:
            chain[i] = black
    chain.write()


# Draw 10 levels, starting with green then yellow then red.
level(5)  # GGGGG.....
level(0)  # ..........
level(8)  # GGGGGGGY
level(10)  # GGGGGGGYYR

for i in range(num_leds + 1):
    level(i)


# Same again, but this time draw the previous level at 1/8th brightness
last = 0


def level_sticky(n):
    global last
    for i in range(num_leds):
        if n > i:
            chain[i] = colors[i]
        elif last > i:
            (r, g, b) = colors[i]
            chain[i] = (r // 8, g // 8, b // 8)
        else:
            chain[i] = black
    last = n
    chain.write()


# 10 levels, with previous level remaining 1/8th lit for 1 step, like a vu meter
level_sticky(7)
level_sticky(10)
level_sticky(8)
level_sticky(5)

for i in range(0, 1000, 23):
    level_sticky(i % num_leds)
    sleep_ms(50)

# Why increment by 23? Just a prime number for some pseduo-randomness.
