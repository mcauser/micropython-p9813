# MicroPython P9813 RGB LED driver examples

from machine import Pin
import p9813
pin_clk = Pin(5, Pin.OUT)
pin_data = Pin(4, Pin.OUT)

num_leds = 10
chain = p9813.P9813(pin_clk, pin_data, num_leds)

# set the first LED to red
chain[0] = (255, 0, 0)

# set the second LED to green
chain[1] = (0, 255, 0)

# set the third LED to blue
chain[2] = (0, 0, 255)

# changes are not visible until you...
# write data to all LEDs
chain.write()

# get first LED colour
r, g, b = chain[0]

# get second LED colour
r, g, b = chain[1]

# make all LEDs red
chain.fill((255,0,0))
chain.write()

# turn off all LEDs
chain.reset()

# make only the second LED green
chain[1] = (0,255,0)
chain.write()

# rainbow
chain.buf = bytearray(b'\xff\x00\x00\xb4K\x00f\x99\x00\x1b\xe4\x00\x00\xcc3\x00~\x81\x003\xcc\x1b\x00\xe4f\x00\x99\xb4\x00K')
chain.write()
