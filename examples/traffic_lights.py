# traffic lights
# 0,1,2 = road A red,amber,green
# 3,4,5 = road B red,amber,green

from machine import Pin
import p9813
from time import sleep_ms

num_leds = 10
chain = p9813.P9813(Pin(5), Pin(4), num_leds)

# reset
chain.fill((0,0,0))
chain.write()

# how long (in ms) light is green
active = 4000
# how long light is amber
transition = 1000
# how long both lights red before one becomes green
pause = 500

# colours
off = (0,0,0)
red = (255,0,0)
amber = (255,194,0)
green = (0,255,0)

# initial state: red/red
chain[0] = red
chain[3] = red
chain.write()

while(True):
	# red/red
	chain[3] = red
	chain[4] = off
	chain.write()
	sleep_ms(pause)

	# green/red
	chain[0] = off
	chain[2] = green
	chain.write()
	sleep_ms(active)

	# amber/red
	chain[1] = amber
	chain[2] = off
	chain.write()
	sleep_ms(transition)

	# red/red
	chain[0] = red
	chain[1] = off
	chain.write()
	sleep_ms(pause)

	# red/green
	chain[3] = off
	chain[5] = green
	chain.write()
	sleep_ms(active)

	# red/amber
	chain[4] = amber
	chain[5] = off
	chain.write()
	sleep_ms(transition)
