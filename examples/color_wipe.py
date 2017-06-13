from machine import Pin
import p9813
from time import sleep_ms

num_leds = 10
chain = p9813.P9813(Pin(5), Pin(4), num_leds)

# Illuminate the pixels one by one
# X.......
# XX......
# XXX.....
# XXXX....
# XXXXX...
# XXXXXX..
# XXXXXXX.
# XXXXXXXX
def color_wipe(color, wait):
	for i in range(num_leds):
		chain[i] = color
		chain.write()
		sleep_ms(wait)

red = (16,0,0)
green = (0,16,0)
blue = (0,0,16)
cyan = (0,16,16)
magenta = (16,0,16)
yellow = (16,16,0)
black = (0,0,0)
colors = [red,green,blue,cyan,magenta,yellow,black]

# Illuminate the pixels one by one, keeping them lit
for color in colors:
	color_wipe(color, 0)
