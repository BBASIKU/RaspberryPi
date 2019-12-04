from gpiozero import LED
from time import sleep

ledg = LED(16)
ledy = LED(20)
ledr = LED(21)
ledG = LED(17)
ledY = LED(27)
ledR = LED(22)

delay1 = 0.5 #Start tid inden lyskrydset begynder og kører.
delay2 = 1.5 #Bestemmer hvor lang tid der skal være gult.
delay3 = 3.0 #Bestemmer hvor lang tid der skal være grønt.
delay4 = 2.0 #Bestemmer hvor lang tid der skal gå inden den anden "lyskegle" skal begynde.

while True:
    ledr.on()
    ledR.on()
    sleep(delay1)
    
    ledy.on()
    sleep(delay2)
    ledr.off()
    ledy.off()
    ledg.on()
    sleep(delay3)
    ledg.off()
    ledy.on()
    sleep(delay2)
    ledy.off()
    ledr.on()
    sleep(delay4)
    
    ledY.on()
    sleep(delay2)
    ledR.off()
    ledY.off()
    ledG.on()
    sleep(delay3)
    ledG.off()
    ledY.on()
    sleep(delay2)
    ledY.off()
    ledR.on()
    sleep(delay4)
    