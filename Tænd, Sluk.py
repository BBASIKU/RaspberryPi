#Lyset tænder modsat af hvad man sætter det til:
#Off = tændt.
#On = slukket.
from gpiozero import LED, Button
from time import sleep
from signal import pause

ledg = LED(16)
ledy = LED(20)
ledr = LED(21)
ledG = LED(17)
ledY = LED(27)
ledR = LED(22)

button1 = Button(2)
button3 = Button(3)

delay1 = 1

#def tænd():
    #ledr.off
    #ledy.off
    #ledg.off

#def sluk():
    #ledr.on
    #ledy.on
    #ledg.on


while True:
    button1.when_pressed = ledr.off(), ledy.off(), ledg.off()
    #button1.when_pressed = ledy.off
    #button1.when_pressed = ledg.off
    
    button1.when_released = ledr.on
    #button1.when_released = ledy.on
    #button1.when_released = ledg.on


    button3.when_pressed = ledY.on
    button3.when_released = ledY.off