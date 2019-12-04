from gpiozero import LED
from time import sleep

ledg = LED(16)
ledy = LED(20)
ledr = LED(21)
ledG = LED(17)
ledY = LED(27)
ledR = LED(22)

delay1 = 0.5
delay2 = 0.5

while True:
    ledg.on()
    ledR.on()
    sleep (delay1)
    ledg.off()
    ledR.off()
    ledy.on()
    ledY.on()
    sleep (delay2)
    ledy.off()
    ledY.off()
    ledr.on()
    ledG.on()
    sleep (delay1)
    ledr.off()
    ledG.off()
    ledy.on()
    ledY.on()
    sleep (delay2)
    ledy.off()
    ledY.off()