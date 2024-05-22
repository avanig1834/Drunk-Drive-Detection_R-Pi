import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
mtr=21
white_led=27
yellow_led=17
GPIO.setup(mtr, GPIO.OUT)
GPIO.output(mtr,GPIO.HIGH)
GPIO.setup(white_led,GPIO.OUT)
GPIO.setup(yellow_led,GPIO.OUT)
GPIO.setup(4,GPIO.IN)
try:
    while True:
        if True:
            print(“Alcohol Not detected")
                      GPIO.output(mtr,GPIO.HIGH)
      GPIO.output(yellow_led,GPIO.HIGH)
            GPIO.output(white_led,GPIO.LOW)
        else:
            print("Alchol Detected")
            GPIO.output(mtr,GPIO.Low)
            GPIO.output(yellow_led,GPIO.LOW)
            GPIO.output(white_led,GPIO.HIGH)
            break
    print(GPIO.input(4))
    sleep(5)
finally:
    GPIO.cleanup()
