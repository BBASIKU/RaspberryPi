from gpiozero import LED
from DesignSpark.Pmod.HAT import createPmod
import time
import smtplib
import config

#De virker modsat saa:
#on  = Off
#off = On
rele1 = LED(5)
rele2 = LED(6)
rele3 = LED(13)
rele4 = LED(19)
therm = createPmod('TC1','JBA')

x=0

def start():
	global x
	x=x+1

	if x == 20:
		x = 0
		return clear

	cel = therm.readCelcius()
	time.sleep(1)

	if cel <= 24:
		cel = therm.readCelcius()
		print("Normal drift: "+str(cel)+" grader.")
		rele1.on()
		rele2.on()
		rele3.on()
		rele4.on()

		return start()

	elif cel >= 25 and cel < 30:
		return ventilator()

	elif cel >= 30:
		return vindue()

	else:
		return start()


def ventilator():
	global x
	x=x+1

	if x == 20:
		x = 0
		return clear

	cel = therm.readCelcius()
	time.sleep(1)

	if cel <= 24:
		return start()

	elif cel >= 25 and  cel <30:
		print("Ventilator: "+str(cel)+" grader.")
		rele1.off()
		rele2.off()
		rele3.on()
		rele4.on()

		return ventilator()

	elif cel >= 30:
		return vindue()

	else:
		return start()


def vindue():
	global x
	x=x+1

	if x == 20:
		x = 0
		return clear

	cel = therm.readCelcius()
	time.sleep(1)

	if cel < 25:
		return start()

	elif cel >= 25 and cel < 30:
		return ventilator()

	elif cel >= 30:
		print("Vindue og Ventilator: "+str(cel)+" grader.")
		rele1.off()
		rele2.off()
		rele3.off()
		rele4.off()

		return vindue()

	else:
		return start()


def clear():
	therm.clearup()
	return start()


state = start()
while state: state = start()
