from gpiozero import LED
from time import sleep

ledg = LED(16) #NS
ledy = LED(20) #NS
ledr = LED(21) #NS
ledG = LED(17) #ØV
ledY = LED(27) #ØV
ledR = LED(22) #ØV

delay0 = 1.0
delay1 = 1.5 
delay2 = 1.5 
delay3 = 3.0 
delay4 = 2.0 


def rød(x):
    
    if x=="NS":
        #x="ØV"
        print ("Lyskryds NS")
        sleep(delay1)
        return NS(x)
    
    elif x=="ØV":
        #x="NS"
        print ("Lyskryds ØV")
        sleep(delay1)
        return ØV(x)
    
    
def NS(x):
    
    if x=="NS":
        x="ØV"
        print ("Lyskryds NS kører")
        sleep(delay1)
        return rød(x)
    
    
def ØV(x):
    
    if x=="ØV":
        x="NS"
        print ("Lyskryds ØV kører")
        sleep(delay1)
        return rød(x)
    
    
state=rød(x="NS")
while state: state=rød(x="NS")