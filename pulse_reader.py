from smbus import SMBus
from time import sleep
import RPi.GPIO as GPIO

# compatibility for different versions of RasPi
# rev 2 or 3 will use bus address 1
# rev 1 will use bus address 0
rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
	b = SMBus(1)
else:
	b = SMBus(0)

GPR_I2C_DEV_ID = 0x50


# test to see if this is always I2C-1
address = 0x50

# Pulse will return -1 in case of immediate IOError
pulse = -1

while True:
	# handling IOError incase Grove decides to go on a walk
	try:
		pulse = b.read_byte(address)
	except IOError:
		print("there was an IO Error")
	# print the pulse otherwise
	print(pulse)
	# wait two seconds
	sleep(2)
