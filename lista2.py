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



    
    

    
def Leds1 (a,b,c,d,e,f,g,h):
    luz_led.value(a)
    luz_led1.value(b)
    luz_led2.value(c)
    luz_led3.value(d)
    luz_led4.value(e)
    luz_led5.value(f)
    luz_led6.value(g)
    luz_led7.value(h)
    
def Leds2 (i,j,k,l,m,n,o,p):
    luz_led.value(i)
    luz_led1.value(j)
    luz_led2.value(k)
    luz_led3.value(l)
    luz_led4.value(m)
    luz_led5.value(n)
    luz_led6.value(o)
    luz_led7.value(p)

def modos():
    
    Modo = print(input("Que modo quieres? 1  o 2:   "))
    
    if Modo == "1":
    
        Leds1()
    
    elif Modo == "2":
        
        leds2()
    else:
        print("Sea serio tonto")

    while True:
    
    
        Leds1(0,0,0,0,0,0,0,0)
        utime.sleep(0.1)
        Leds1(1,0,0,0,0,0,0,0)
        utime.sleep(0.1)
        Leds1(1,1,0,0,0,0,0,0)
        utime.sleep(0.1)
        Leds1(1,1,1,0,0,0,0,0)
        utime.sleep(0.1)
        Leds1(1,1,1,1,0,0,0,0)
        utime.sleep(0.1)
        Leds1(1,1,1,1,1,0,0,0)
        utime.sleep(0.1)
        Leds1(1,1,1,1,1,1,0,0)
        utime.sleep(0.1)
        Leds1(1,1,1,1,1,1,1,0)
        utime.sleep(0.1)
        Leds1(1,1,1,1,1,1,1,1)
    
        utime.sleep(0.1)
        Leds1(1,1,1,1,1,1,1,1)
        utime.sleep(0.1)
        Leds1(1,1,1,1,1,1,1,0)
        utime.sleep(0.1)
        Leds1(1,1,1,1,1,0,0,0)
        utime.sleep(0.1)
        Leds1(1,1,1,1,0,0,0,0)
        utime.sleep(0.1)
        Leds1(1,1,1,0,0,0,0,0)
        utime.sleep(0.1)
        Leds1(1,1,0,0,0,0,0,0)
        utime.sleep(0.1)
        Leds1(1,0,0,0,0,0,0,0)
        utime.sleep(0.1)
        Leds1(0,0,0,0,0,0,0,0)
        utime.sleep(0.1)
    
    
        print("Luces led >u<")
    