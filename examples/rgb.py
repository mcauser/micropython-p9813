from machine import Pin
import p9813

num_leds = 10
chain = p9813.P9813(Pin(5), Pin(4), num_leds)

# helper
def rgb(i,j):
	return 16 if i % 3 == j else 0

# red, green, blue, red, green, blue, ...
for i in range(num_leds):
	chain[i] = (rgb(i,0), rgb(i,1), rgb(i,2))
chain.write()
