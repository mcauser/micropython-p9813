from machine import Pin
import p9813

num_leds = 10
chain = p9813.P9813(Pin(5), Pin(4), num_leds)

def fade():
	for i in range(0, 4 * 256, 8):
		for j in range(num_leds):
			if (i // 256) % 2 == 0:
				val = i & 0xff
			else:
				val = 255 - (i & 0xff)
			chain[j] = (val, 0, 0)
		chain.write()

# Fade in/out
fade()
