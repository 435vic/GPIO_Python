import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
f = 50
dc = 0
p = GPIO.PWM(16,f)
p.start(dc)


try:
	while True:
		for x in range (100):
			p.ChangeDutyCycle(x)
			time.sleep(.02)
		for x in range (100):
			p.ChangeDutyCycle(100 - x)
			time.sleep(.02)
		p.ChangeDutyCycle(0)
except KeyboardInterrupt:
	p.stop
	GPIO.cleanup()
	print ""
	exit()



