import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.output(14,True)
time.sleep(0.2)
GPIO.output(14,False)
time.sleep(0.2)
GPIO.output(18,True)
time.sleep(0.2)
GPIO.output(18,False)
time.sleep(0.2)
