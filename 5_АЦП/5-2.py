
import RPi.GPIO as GPIO
from time import sleep

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
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)


try:
    while True:
        a = adc()
        v = a/256*3.3
        print(a, round(v, 3))
        sleep(0.01)
            
finally:
    GPIO.output(dac, 0)
    




