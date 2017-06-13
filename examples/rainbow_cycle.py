from machine import Pin
import p9813
from time import sleep_ms

num_leds = 10
chain = p9813.P9813(Pin(5), Pin(4), num_leds)

def rainbow_cycle(np, sleep):
	# 5 cycles of all colors on wheel
	for r in range(5):
		for n in range(256):
			for i in range(num_leds):
				chain[i] = wheel(((i * 256 // num_leds) + n) & 255)
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

# Fade all pixels together through rainbow colours, offset each pixel
rainbow_cycle(0)
