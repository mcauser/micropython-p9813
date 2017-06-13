from machine import Pin
import p9813
from time import sleep_ms

num_leds = 10
chain = p9813.P9813(Pin(5), Pin(4), num_leds)

# Theatre-style crawling lights
# X..X..X.
# .X..X..X
# ..X..X..X
def theater_chase(color, wait):
	for n in range(10):
		# 3 unique combinations in the pattern [100,010,001]
		for u in range(3):
			# for each pixel
			for i in range(num_leds):
				# turn every third pixel on, the others off
				if i % 3 == u:
					chain[i] = color
				else:
					chain[i] = (0, 0, 0)
			chain.write()
			sleep_ms(wait)

red = (16,0,0)

# Theatre-style crawling lights, in a given colour
theater_chase(red, 0)