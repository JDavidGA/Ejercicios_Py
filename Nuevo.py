from machine import Pin
import utime


luz_led = Pin(15,Pin.OUT)
luz_led1 = Pin(2,Pin.OUT)
luz_led2 = Pin(4,Pin.OUT)
luz_led3 = Pin(16,Pin.OUT)
luz_led4 = Pin(17,Pin.OUT)
luz_led5 = Pin(5,Pin.OUT)
luz_led6 = Pin(18,Pin.OUT)
luz_led7 = Pin(19,Pin.OUT)

Leds = [luz_led,luz_led1,luz_led2,luz_led3,luz_led4,luz_led5,luz_led6,luz_led7]


while True:
    
    for Elemento in Leds[0:8:1]:
        Elemento.value(1)
        utime.sleep_ms(30)
        Elemento.value(0)
        utime.sleep_ms(30)
        
    for Elemento in Leds[2:7:1]:
        Elemento.value(1)
        utime.sleep_ms(15)
        Elemento.value(0)
        utime.sleep_ms(15)
        