from machine import Pin
import p9813
from time import sleep_ms

num_leds = 10
chain = p9813.P9813(Pin(5), Pin(4), num_leds)

def cycle(color, sleep):
	for i in range(num_leds):
		for j in range(num_leds):
			chain[j] = (0, 0, 0)
		chain[i % num_leds] = color
		chain.write()
		sleep_ms(sleep)

# Predefine some colours
red = (16,0,0)
green = (0,16,0)
blue = (0,0,16)
cyan = (0,16,16)
magenta = (16,0,16)
yellow = (16,16,0)
white = (16,16,16)
black = (0,0,0)
colors = [red,green,blue,cyan,magenta,yellow,white,black]

# Illuminate the pixels one by one
for color in colors:
	cycle(color, 0)
