from neopixel import NeoPixel
from machine import Pin, TouchPad
from time import sleep_ms

THRESHOLD=const(30_000)

pin = Pin(21, mode=Pin.OUT)
pixel = NeoPixel(pin, 1)
touch_pin = TouchPad(Pin(4, mode=Pin.IN))

def led(r=0, g=0, b=0):
    pixel[0] = (g, r, b)
    pixel.write()

while True:
    touch_value = touch_pin.read()

    if touch_value > THRESHOLD:
        led(r=0xFF)
    else:
        led(r=0)

    sleep_ms(100)
