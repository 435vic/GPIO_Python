import RPi.GPIO as GPIO
import time
led = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
time.sleep(1)
print ("Led on")
GPIO.output(16,True)
time.sleep(1)
print ("Led off")
GPIO.output(16,False)
GPIO.cleanup()
