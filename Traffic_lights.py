import RPi.GPIO as GPIO
import time
import signal
import sys

red_led_a = 22
yellow_led_a = 24
green_led_a = 26
#print "Hello-A"
red_led_b = 32
yellow_led_b = 31
green_led_b = 16
#print "Hello-B"
red_led_c = 50
yellow_led_c = 50
green_led_c = 50
#print "Hello-C"
red_led_d = 40
yellow_led_d = 38
green_led_d = 37
#print "Hello-D"
#--------- high low logic
HIGH=1
LOW=0
#------------------ Rpi Config
RUNNING= True
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#------------------ pin config
GPIO.setup(red_led_a,GPIO.OUT)
GPIO.setup(yellow_led_a,GPIO.OUT)
GPIO.setup(green_led_a,GPIO.OUT)

GPIO.setup(red_led_b,GPIO.OUT)
GPIO.setup(yellow_led_b,GPIO.OUT)
GPIO.setup(green_led_b,GPIO.OUT)

GPIO.setup(red_led_c,GPIO.OUT)
GPIO.setup(yellow_led_c,GPIO.OUT)
import RPi.GPIO as GPIO
import time
import signal
import sys

red_led_a = 22
yellow_led_a = 24
green_led_a = 26
#print "Hello-A"
red_led_b = 32
yellow_led_b = 31
green_led_b = 16
#print "Hello-B"
red_led_c = 15
yellow_led_c = 13
green_led_c = 11
#print "Hello-C"
red_led_d = 40
yellow_led_d = 38
green_led_d = 37
#print "Hello-D"
#--------- high low logic
HIGH=1
LOW=0
#------------------ Rpi Config
RUNNING= True
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#------------------ pin config
GPIO.setup(red_led_a,GPIO.OUT)
GPIO.setup(yellow_led_a,GPIO.OUT)
GPIO.setup(green_led_a,GPIO.OUT)

GPIO.setup(red_led_b,GPIO.OUT)
GPIO.setup(yellow_led_b,GPIO.OUT)
GPIO.setup(green_led_b,GPIO.OUT)

GPIO.setup(red_led_c,GPIO.OUT)
GPIO.setup(yellow_led_c,GPIO.OUT)
GPIO.setup(green_led_c,GPIO.OUT)

GPIO.setup(red_led_d,GPIO.OUT)
GPIO.setup(yellow_led_d,GPIO.OUT)
GPIO.setup(green_led_d,GPIO.OUT)

#---------------------------- all def
'''
    Def for only one Lane Green On other low
'''
def Greenon(red, yellow, green):
    GPIO.output(green, HIGH)
    GPIO.output(red, LOW)
    GPIO.output(yellow, LOW)
    red_on(red)
    all_green_low(green)
    all_yellow_low()


'''
 Def for all red Signal on Except current Green On
'''
def red_on(r):
    GPIO.output(red_led_a, HIGH)
    GPIO.output(red_led_b, HIGH)
    GPIO.output(red_led_c, HIGH)
    GPIO.output(red_led_d, HIGH)
    GPIO.output(r, LOW)
  
def all_green_low(g):
    GPIO.output(green_led_a, LOW)
    GPIO.output(green_led_b, LOW)
    GPIO.output(green_led_c, LOW)
    GPIO.output(green_led_d, LOW)
    GPIO.output(g, HIGH)

def all_yellow_low():
    GPIO.output(yellow_led_a, LOW)
    GPIO.output(yellow_led_b, LOW)
    GPIO.output(yellow_led_c, LOW)
    GPIO.output(yellow_led_d, LOW)

def yellow_high(y):
    GPIO.output(yellow_led_a, LOW)
    GPIO.output(yellow_led_b, LOW)
    GPIO.output(yellow_led_c, LOW)
    GPIO.output(yellow_led_d, LOW)
    GPIO.output(y, HIGH)

    
# Main loop
try:
    while RUNNING:
        # Green for 13 seconds LA other LB LC LD RED
        #---------- LA
        Greenon(red_led_a,yellow_led_a,green_led_a)
        time.sleep(5.1); #green time 
        yellow_high(yellow_led_a)
        time.sleep(3.1);
        #---------- LB
        Greenon(red_led_b,yellow_led_b,green_led_b)
        time.sleep(7.0);
        yellow_high(yellow_led_b)
        time.sleep(3.0);
        #---------- LC
        Greenon(red_led_c,yellow_led_c,green_led_c)
        time.sleep(5.2);
        yellow_high(yellow_led_c)
        time.sleep(3.1);
        #---------- LD
        Greenon(red_led_d,yellow_led_d,green_led_d)
        time.sleep(7.0);
        yellow_high(yellow_led_d)
        time.sleep(5.1);
# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RUNNING = False
    print("\Quitting")
 
# Actions under 'finally' will always be called
finally:
    # Stop and finish cleanly so the pins
    # are available to be used again
    GPIO.cleanup(c,GPIO.OUT)
GPIO.setup(green_led_c,GPIO.OUT)

GPIO.setup(red_led_d,GPIO.OUT)
GPIO.setup(yellow_led_d,GPIO.OUT)
GPIO.setup(green_led_d,GPIO.OUT)

#---------------------------- all def
'''
    Def for only one Lane Green On other low
'''
def Greenon(red, yellow, green):
    GPIO.output(green, HIGH)
    GPIO.output(red, LOW)
    GPIO.output(yellow, LOW)
    red_on(red)
    all_green_low(green)
    all_yellow_low()


'''
 Def for all red Signal on Except current Green On
'''
def red_on(r):
    GPIO.output(red_led_a, HIGH)
    GPIO.output(red_led_b, HIGH)
    GPIO.output(red_led_c, HIGH)
    GPIO.output(red_led_d, HIGH)
    GPIO.output(r, LOW)
  
def all_green_low(g):
    GPIO.output(green_led_a, LOW)
    GPIO.output(green_led_b, LOW)
    GPIO.output(green_led_c, LOW)
    GPIO.output(green_led_d, LOW)
    GPIO.output(g, HIGH)

def all_yellow_low():
    GPIO.output(yellow_led_a, LOW)
    GPIO.output(yellow_led_b, LOW)
    GPIO.output(yellow_led_c, LOW)
    GPIO.output(yellow_led_d, LOW)

def yellow_high(y):
    GPIO.output(yellow_led_a, LOW)
    GPIO.output(yellow_led_b, LOW)
    GPIO.output(yellow_led_c, LOW)
    GPIO.output(yellow_led_d, LOW)
    GPIO.output(y, HIGH)

    
# Main loop
try:
    while RUNNING:
        # Green for 13 seconds LA other LB LC LD RED
        #---------- LA
        Greenon(red_led_a,yellow_led_a,green_led_a)
        time.sleep(3); #green time 
        yellow_high(yellow_led_a)
        time.sleep(2);
        #---------- LB
        Greenon(red_led_b,yellow_led_b,green_led_b)
        time.sleep(3);
        yellow_high(yellow_led_b)
        time.sleep(2);
        #---------- LC
        Greenon(red_led_c,yellow_led_c,green_led_c)
        time.sleep(3);
        yellow_high(yellow_led_c)
        time.sleep(2);
        #---------- LD
        Greenon(red_led_d,yellow_led_d,green_led_d)
        time.sleep(3);
        yellow_high(yellow_led_d)
        time.sleep(2);
# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RUNNING = False
    print("\Quitting")
 
# Actions under 'finally' will always be called
finally:
    # Stop and finish cleanly so the pins
    # are available to be used again
    GPIO.cleanup()