#!/user/bin/env python
#To use the program with gpio, be sure to
#install the RPi.GPIO library.
#Uncomment the first lines to use with gpio.
#The lines you can uncomment are marked with a #space.





#import the libraries
 #import RPi.GPIO as GPIO
import time

 #GPIO.setmode(GPIO.BOARD)
#Set a variable for the LED
 #LED = 
 #GPIO.setup(7,GPIO.OUT)
for x in range (10):
    time.sleep(1)
    print("LED on")
     #GPIO.output(7,1)
    time.sleep(1)
    print("LED off")
     #GPIO.output(7,0)
 #GPIO.cleanup()
time.sleep(2)

