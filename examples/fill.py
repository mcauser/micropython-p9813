from machine import Pin
import p9813

num_leds = 10
chain = p9813.P9813(Pin(5), Pin(4), num_leds)

red = (16,0,0)
green = (0,16,0)
blue = (0,0,16)

chain.fill(red)
chain.write()

chain.fill(gren)
chain.write()

chain.fill(blue)
chain.write()

chain.fill((0,0,0))
chain.write()

chain.fill((0xff,0x99,0x00))
chain.write()

chain.reset()
