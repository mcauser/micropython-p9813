from machine import Pin
import p9813

pin_clk = Pin(5, Pin.OUT)
pin_data = Pin(4, Pin.OUT)

num_leds = 10
chain = p9813.P9813(pin_clk, pin_data, num_leds)

# set the first pixel to red
chain[0] = (255, 0, 0)

# set the first pixel to green
chain[1] = (0, 255, 0)

# set the first pixel to blue
chain[2] = (0, 0, 255)

# changes are not visible until you...
# write data to all pixels
chain.write()

# get first pixel colour
r, g, b = chain[0]

# get second pixel colour
r, g, b = chain[1]
