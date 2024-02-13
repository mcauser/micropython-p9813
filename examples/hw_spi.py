# SPDX-FileCopyrightText: 2024 Mike Causer <https://github.com/mcauser>
# SPDX-License-Identifier: MIT

"""
MicroPython P9813 RGB LED driver
https://github.com/mcauser/micropython-p9813
"""

from machine import SPI, Pin
import p9813

# MISO is not used. The LED driver is write only.

# TinyPICO (esp32)
spi = SPI(1, 10000000, sck=Pin(18), mosi=Pin(23), miso=Pin(19))

# TinyS2 (esp32s2)
# spi = SPI(1, 10000000, sck=Pin(4), mosi=Pin(5), miso=Pin(6))

# Hardware SPI, 10 LEDs, auto-write on
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
# Hardware SPI can refresh so fast that persistance of vision
# will only let you see white LEDs until the range is complete.
refresh_rate_test(10000)
