from machine import Pin, PWM
import time

blue = PWM(Pin(12, mode=Pin.OUT))
green = PWM(Pin(13, mode=Pin.OUT))
red = PWM(Pin(14, mode=Pin.OUT))

blue.freq(1_000)
green.freq(1_000)
red.freq(1_000)

while True:
    blue.duty_u16(0)
    green.duty_u16(0)
    red.duty_u16(0)