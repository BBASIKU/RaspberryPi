from gpiozero import LED
from time import sleep

ledg = LED(16)
ledy = LED(20)
ledr = LED(21)
ledG = LED(17)
ledY = LED(27)
ledR = LED(22)

delay1 = 0.05

while True:
    ledr.on()
    ledR.on()
    sleep(delay1)
    ledr.off()
    ledR.off()
    
    ledy.on()
    ledY.on()
    sleep(delay1)
    ledy.off()
    ledY.off()
    
    ledg.on()
    ledG.on()
    sleep(delay1)
    ledg.off()
    ledG.off()