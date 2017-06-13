from machine import Pin
import p9813
from time import sleep_ms

num_leds = 10
chain = p9813.P9813(Pin(5), Pin(4), num_leds)

# Theatre-style crawling lights
# X..X..X.
# .X..X..X
# ..X..X..X
def theatre_chase_rainbow(sleep):
	# cycle through all 256 colours, skipping 2/3s (86)
	for n in range(86):
		# 3 unique combinations in the pattern [100,010,001]
		for u in range(3):
			for i in range(num_leds):
				# turn every third pixel on, the others off
				if i % 3 == u:
					chain[i] = wheel((i + n * 3) % 255)
				else:
					chain[i] = (0, 0, 0)
			chain.write()
			sleep_ms(sleep)

# Helper for converting 0-255 offset to a colour tuple
def wheel(offset):
	# The colours are a transition r - g - b - back to r
	offset = 255 - offset
	if offset < 85:
		return (255 - offset * 3, 0, offset * 3)
	if offset < 170:
		offset -= 85
		return (0, offset * 3, 255 - offset * 3)
	offset -= 170
	return (offset * 3, 255 - offset * 3, 0)

# Theatre-style crawling lights, in rainbow colours
theatre_chase_rainbow(0)