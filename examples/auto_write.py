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

# With auto-write enabled, each time you modify the LEDs, it calls
# write() and sends the data for every pixel in the chain.

# You can't update a single LED. You have to write the data for all.

# When making lots of individual LED changes, it's faster to defer
# writing until all changes have been made.

# Set first LED to red
chain[0] = (127, 0, 0)
# Notice it's immediately red

# Switch off auto-write
chain.auto_write = False

# Set second LED to green
chain[1] = (0, 127, 0)

# Set third LED to blue
chain[2] = (0, 0, 127)

# With auto-write off, modifications to the chain only update
# the internal buffer (checksum + red + green + blue values)
# Calling write() later sends the buffer to all LEDs.

# Notice the second and third LEDs are not lit yet
chain.write()
# Now they are lit

# Switch auto-write back on
chain.auto_write = True

# Make all LEDs green
chain.fill((0, 127, 0))
# Auto-write is temporarily ignored as fill() populates the entire buffer.
# Once the buffer is ready, if auto-write was previously on, data is send out.
