import RPi.GPIO as GPIO
from time import sleep
from time import time
def dec2bin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

def adc():
    v = 0
    t = v + 128
    GPIO.output(dac, dec2bin(t))
    sleep(0.001)
    if GPIO.input(comp) == 0:
        v = t

    t = v + 64
    GPIO.output(dac, dec2bin(t))
    sleep(0.001)
    if GPIO.input(comp) == 0:
        v = t

    t = v + 32
    GPIO.output(dac, dec2bin(t))
    sleep(0.001)
    if GPIO.input(comp) == 0:
        v = t

    t = v + 16
    GPIO.output(dac, dec2bin(t))
    sleep(0.001)
    if GPIO.input(comp) == 0:
        v = t

    t = v + 8
    GPIO.output(dac, dec2bin(t))
    sleep(0.001)
    if GPIO.input(comp) == 0:
        v = t

    t = v + 4
    GPIO.output(dac, dec2bin(t))
    sleep(0.001)
    if GPIO.input(comp) == 0:
        v = t

    t = v + 2
    GPIO.output(dac, dec2bin(t))
    sleep(0.001)
    if GPIO.input(comp) == 0:
        v = t
        
    t = v + 1
    GPIO.output(dac, dec2bin(t))
    sleep(0.001)
    if GPIO.input(comp) == 0:
        v = t
    return v

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)


try:
    while True:
        start = time()
        a = adc()
        end = time()
        v = a/256*3.3
        print(a, round(v, 3), int((end - start)*1000))
        sleep(0.01)
        s = round(a/256*8) * "1" + (8-round(a/256*8)) * "0"
        s = [int(i) for i in s] 
        GPIO.output(leds, s)
            
finally:
    GPIO.output(leds, 0)


