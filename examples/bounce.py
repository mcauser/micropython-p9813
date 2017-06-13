from machine import Pin
import p9813
from time import sleep_ms

num_leds = 10
chain = p9813.P9813(Pin(5), Pin(4), num_leds)

def bounce(color, sleep):
	for i in range(4 * num_leds):
		for j in range(num_leds):
			chain[j] = color
		if (i // num_leds) % 2 == 0:
			chain[i % num_leds] = (0, 0, 0)
		else:
			chain[num_leds - 1 - (i % num_leds)] = (0, 0, 0)
		chain.write()
		sleep_ms(sleep)

red = (16,0,0)
green = (0,16,0)
colors = [red,green]

# Bounce a dark pixel back and forth
for color in colors:
	bounce(color, 0)
