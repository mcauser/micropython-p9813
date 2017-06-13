from machine import Pin
import p9813
from time import sleep_ms
from urandom import getrandbits

num_leds = 10
chain = p9813.P9813(Pin(5), Pin(4), num_leds)

def random_colors(sleep):
	for r in range(50):
		for i in range(num_leds):
			chain[i] = (getrandbits(8), getrandbits(8), getrandbits(8))
		chain.write()
		sleep_ms(sleep)

# Random colours
random_colors(0)
