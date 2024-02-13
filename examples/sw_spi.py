# SPDX-FileCopyrightText: 2024 Mike Causer <https://github.com/mcauser>
# SPDX-License-Identifier: MIT

"""
MicroPython P9813 RGB LED driver
https://github.com/mcauser/micropython-p9813
"""

from machine import SoftSPI, Pin
import p9813

# MISO is not used. The LED driver is write only.

# TinyPICO (esp32)
spi = SoftSPI(baudrate=100000, sck=Pin(18), mosi=Pin(23), miso=Pin(19))

# TinyS2 (esp32s2)
# spi = SoftSPI(baudrate=100000, sck=Pin(4), mosi=Pin(5), miso=Pin(6))

# Software SPI, 10 LEDs, auto-write on
num_leds = 10
chain = p9813.P9813_SPI(spi, num_leds, True)


def refresh_rate_test(count):
    red = (16, 0, 0)
    green = (0, 16, 0)
    blue = (0, 0, 16)
    colors = [red, green, blue]
    for i in range(count):
        chain[i % num_leds] = colors[i % 3]


# For ~4 seconds, rapidly draw red, green, blue incrementally.
# Using a 100x slower SPI baud than the Hardware SPI example, running
# the same test will instead of showing solid white LEDs, shows
# them all flickering as it rapidly draws the colours.
refresh_rate_test(1000)
