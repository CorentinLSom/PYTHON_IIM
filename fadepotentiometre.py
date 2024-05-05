from machine import Pin, PWM, ADC
import time

adc = ADC(Pin(27, mode=Pin.IN))
pwm_led = PWM(Pin(17,mode=Pin.OUT))
pwm_led.duty_u16(13000)

while True:
    val = adc.read_u16()
    val = val * (10 / 500)
    pwm_led.duty_u16(int(val))
    time.sleep(0.01)
    print(int(val))