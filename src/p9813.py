# SPDX-FileCopyrightText: 2017 Mike Causer <https://github.com/mcauser>
# SPDX-License-Identifier: MIT

"""
MicroPython P9813 RGB LED driver
https://github.com/mcauser/micropython-p9813
"""

from machine import Pin

__version__ = "2.0.0"


class P9813:
    def __init__(self, num_leds, auto_write=True):
        self._num = num_leds
        self.auto_write = auto_write
        self.reset()

    def __setitem__(self, index, val):
        # (r, g, b) = val
        if isinstance(index, slice):
            start, stop, step = index.indices(self._num)
            length = stop - start
            if step != 0:
                length = (length + step - 1) // step
            if len(val) != length:
                raise ValueError("Slice and input sequence size do not match.")
            for val_i, idx_i in enumerate(range(start, stop, step)):
                self._set_led(idx_i, val[val_i])
        else:
            self._set_led(index, val)

        if self.auto_write:
            self.write()

    def __getitem__(self, index):
        # returns (r, g, b) if index is an int, eg. self[1]
        # or [(r, g, b), (r, g, b)] if index is a slice, eg. self[1:2]
        if isinstance(index, slice):
            out = []
            for idx_i in range(*index.indices(self._num)):
                out.append(self._get_led(idx_i))
            return out
        if index < 0:
            index += len(self)
        if index >= self._num or index < 0:
            raise IndexError
        return self._get_led(index)

    def __repr__(self):
        return "[" + ", ".join([str(x) for x in self]) + "]"

    def __len__(self):
        return self._num

    def _set_led(self, index, val):
        (r, g, b) = val
        # checksum bits (1, 1, blue[7], blue[6], green[7], green[6], red[7], red[6])
        self._buf[4 * index] = (
            0xC0 | (b & 0xC0) >> 2 | (g & 0xC0) >> 4 | (r & 0xC0) >> 6
        )
        # blue, green, red
        self._buf[4 * index + 1] = b
        self._buf[4 * index + 2] = g
        self._buf[4 * index + 3] = r

    def _get_led(self, index):
        # returns (r, g, b)
        return tuple(self._buf[index * 4 + i] for i in range(3, 0, -1))

    def fill(self, color):
        temp = self.auto_write
        self.auto_write = False
        for i in range(self._num):
            self[i] = color
        self.auto_write = temp
        if self.auto_write:
            self.write()

    def reset(self):
        self._buf = bytearray(self._num * 4)
        # checksums
        for i in range(0, self._num * 4, 4):
            self._buf[i] = 0xC0
        self.write()

    def write(self):
        raise NotImplementedError


class P9813_BITBANG(P9813):
    def __init__(self, pin_clk, pin_data, num_leds, auto_write=True):
        self._clk = pin_clk
        self._dat = pin_data
        self._clk.init(Pin.OUT)
        self._dat.init(Pin.OUT)
        super().__init__(num_leds, auto_write)

    def write(self):
        # Begin data frame 4 bytes
        self._frame()

        # Send 4 bytes for each LED (checksum, blue, green, red)
        for i in range(self._num):
            # Send checksum
            self._write_byte(self._buf[4 * i])
            # Send the 3 colours
            self._write_byte(self._buf[4 * i + 1])  # blue
            self._write_byte(self._buf[4 * i + 2])  # green
            self._write_byte(self._buf[4 * i + 3])  # red

        # End data frame 4 bytes
        self._frame()

    def _frame(self):
        # Send 32x zeros
        self._dat(0)
        for _ in range(32):
            self._clk_pulse()

    def _clk_pulse(self):
        self._clk(0)
        self._clk(1)

    def _write_byte(self, b):
        if b == 0:
            # Fast send 8x zeros
            self._dat(0)
            for _ in range(8):
                self._clk_pulse()
        else:
            # Send each bit, MSB first
            for i in range(8):
                if (b & 0x80) != 0:
                    self._dat(1)
                else:
                    self._dat(0)
                self._clk_pulse()

                # On to the next bit
                b <<= 1


class P9813_SPI(P9813):
    def __init__(self, spi, num_leds, auto_write=True):
        self._spi = spi
        self._fbuf = bytearray(4)
        super().__init__(num_leds, auto_write)

    def write(self):
        # Begin data frame 4 bytes (32x zeros)
        self._spi.write(self._fbuf)

        # Send 4 bytes for each LED (checksum, blue, green, red)
        self._spi.write(self._buf)

        # End data frame 4 bytes (32x zeros)
        self._spi.write(self._fbuf)
