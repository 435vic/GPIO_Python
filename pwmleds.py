import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
f = 50
dc = 0
p1 = GPIO.PWM(12,f)
p2 = GPIO.PWM(13,f)
p3 = GPIO.PWM(16,f)
p1.start(dc)
p2.start(dc)
p3.start(dc)

try:
	while True:
		for x in range (100):
			p1.ChangeDutyCycle(x)
			time.sleep(.02)
		for x in range (100):
			p1.ChangeDutyCycle(100 - x)
			time.sleep(.02)
		p1.ChangeDutyCycle(0)
		for x in range (100):
			time.sleep(.02)
			p2.ChangeDutyCycle(x)
		for x in range (100):
			p2.ChangeDutyCycle(100 - x)
			time.sleep(.02)
		p2.ChangeDutyCycle(0)
		for x in range (100):
			p3.ChangeDutyCycle(x)
			time.sleep(.02)
		for x in range(100):
			p3.ChangeDutyCycle(100 - x)
			time.sleep(.02)
		p3.ChangeDutyCycle(0)
except KeyboardInterrupt:
	pass
	p1.stop
	p2.stop
	p3.stop
	GPIO.cleanup()
	print("Script has stopped.")


