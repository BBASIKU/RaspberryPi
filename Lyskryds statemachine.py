from gpiozero import LED
from time import sleep

ledg = LED(16) #NS
ledy = LED(20) #NS
ledr = LED(21) #NS
ledG = LED(17) #ØV
ledY = LED(27) #ØV
ledR = LED(22) #ØV

delay1 = 2.0 #Rødt lys
delay2 = 1.0 #Gult lys
delay3 = 4.0 #Grønt lys

y=0
z=0
q=0


def Rød(x):
    
    global y
    
    y=y+1
    print("Der har været rødt lys "+str(y),"gange")
    
    if x=="NS":
        print ("Lyskryds Rødt")
        
        ledr.on()
        ledR.on()
        sleep(delay1)
        
        return NS(x)
    
        
    elif x=="ØV":
        print ("Lyskryds Rødt")
        
        ledr.on()
        ledR.on()
        sleep(delay1)
        
        return ØV(x)

    
def NS(x):
    
    global z
    z=z+1
    print("Der har været grønt lys nord-syd på "+str(z), "gange")
    
    if x=="NS":
        x="ØV"
        print ("Lyskryds NS kører")
        
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
        
        return Rød(x)
    
    
def ØV(x):
    
    global q
    q=q+1
    print("Der har været grønt lys øst-vest på "+str(q), "gange")
    
    if x=="ØV":
        x="NS"
        print ("Lyskryds ØV kører")
        
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
        
        return Rød(x)
    
    
state=Rød(x="NS")
while state: state=Rød(x="NS")