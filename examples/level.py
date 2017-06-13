from machine import Pin
import p9813
from time import sleep_ms

num_leds = 10
chain = p9813.P9813(Pin(5), Pin(4), num_leds)

green = (0,16,0)
yellow = (16,16,0)
red = (16,0,0)
black = (0,0,0)
colors = [green,green,green,green,green,green,green,yellow,yellow,red]

def level(n):
	for i in range(num_leds):
		if n > i:
			chain[i] = colors[i]
		else:
			chain[i] = black
	chain.write()

# 10 levels, starting with green then yellow then red
level(5)
level(0)
level(10)

for i in range(num_leds + 1):
	level(i)


last = 0
def level_sticky(n):
	global last
	for i in range(num_leds):
		if n > i:
			chain[i] = colors[i]
		elif last > i:
			(r, g, b) = colors[i]
			chain[i] = (r//8, g//8, b//8)
		else:
			chain[i] = black
	last = n
	chain.write()

# 10 levels, with previous level remaining 1/8th lit for 1 step, like a vu meter
level_sticky(7)
level_sticky(10)
level_sticky(8)
level_sticky(5)

for i in range(0,1000,23):
	level_sticky(i % num_leds)
	sleep_ms(50)

# why inc by 23? just a prime number for some pseduo-randomness
