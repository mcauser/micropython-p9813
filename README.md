# MicroPython P9813

A MicroPython library for P9813 RGB LED drivers.

For example, the Seeed Studio [Grove - Chainable RGB LED](http://wiki.seeed.cc/Grove-Chainable_RGB_LED/).

![demo](docs/demo.jpg)

## Example

Copy the file to your device, using ampy, webrepl or compiling and deploying. eg.

```
$ ampy put p9813.py
```

**Basic usage**

```python
from machine import Pin
import p9813

pin_clk = Pin(5, Pin.OUT)
pin_data = Pin(4, Pin.OUT)

num_leds = 10
chain = p9813.P9813(pin_clk, pin_data, num_leds, False)

# set the first LED to red
chain[0] = (255, 0, 0)

# set the second LED to green
chain[1] = (0, 255, 0)

# write data to all LEDs
chain.write()

# make all LEDs red
chain.fill((255,0,0))
chain.write()

# turn off all LEDs
chain.reset()
```

See [p9813_examples.py](p9813_examples.py) and [examples](examples/) for more.

### Parts

* [WeMos D1 Mini](https://www.aliexpress.com/store/product/D1-mini-Mini-NodeMcu-4M-bytes-Lua-WIFI-Internet-of-Things-development-board-based-ESP8266/1331105_32529101036.html) $4.00 USD
* [Grove - Chainable RGB LED](https://www.seeedstudio.com/Grove-Chainable-RGB-LED-p-850.html) $3.90 USD
* [Grove Male Jumper Cable](https://www.seeedstudio.com/Grove-4-pin-Male-Jumper-to-Grove-4-pin-Conversion-Cable-%285-PCs-per-Pack%29-p-1565.html) $2.90 USD

## #Connections

WeMos D1 Mini | Grove Chainable RGB LED
------------- | -----------------------
D1 (GPIO5)    | CI (clock) (yellow)
D2 (GPIO4)    | DI (data) (white)
3V3 (or 5V)   | VCC (red)
G             | GND (black)

If you are chaining multiple LEDs, clock out -> clock in, data out -> data in, eg.

LED1 | LED2
---- | ----
CO   | CI (yellow)
DO   | DI (white)
VCC  | VCC (red)
GND  | GND (black)

### Links

* [WeMos D1 Mini](https://wiki.wemos.cc/products:d1:d1_mini)
* [micropython.org](http://micropython.org)
* [Adafruit Ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy)
* [P9813 datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Chainable_RGB_LED/master/res/P9813_datasheet.pdf)

## Example for BBC micro:bit

### Software Setup - mu

* Download and setup the [mu editor](https://codewith.mu/).
* Copy the `p9813.py` file from this repository into your `mu` code directory (usually ```USER_DIR/mu```)
* Create a new file with the code below
* Flash it to the micro:bit. **This will fail, the mirco:bit will display an error message**
* Go into the files section of mu and copy the `p9813.py` file over. 
* micro:bit will restart and it should work

### Software Setup - micro:bit editor

* go to the [micro:bit python editor](https://python.microbit.org/v/2.0)
* select `Load/Save`
* Unfold the *Project Files* at the bottom of the pop-up
* Select *Add File* and select the `p9813.py` file from this repo
* paste the sample code below 
* flash the mirco:bit

### Example Script

```python
from microbit import *
from p9813 import P9813

pin_clk = pin14
pin_data = pin0

num_leds = 2
chain = P9813(pin_data, pin_clk, num_leds, True)

# set the first LED to red
chain[0] = (255, 0, 0)

# set the second LED to green
chain[1] = (0, 255, 0)

# write data to all LEDs
chain.write()
sleep(200)
# make all LEDs red
chain.fill((255,0,0))
chain.write()
sleep(2000)
# turn off all LEDs
chain.reset()
```

### Parts: 
* [micro:bit](https://microbit.org/)
* [mirco:bit groove shield](https://www.seeedstudio.com/Grove-Shield-for-micro-bit-v2-0.html)
* [Grove - Chainable RGB LED](https://www.seeedstudio.com/Grove-Chainable-RGB-LED-p-850.html)

## License

Licensed under the [MIT License](http://opensource.org/licenses/MIT).
