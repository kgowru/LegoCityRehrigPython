import RPi.GPIO as GPIO
import time
import os
import signal
import sys
import requests

IR_SENSORS = [6]
prev_val = [0]

def callChris():
    r = requests.post("https://requestb.in/rhmo87rh", data={'number': 12524, 'type': 'issue', 'action': 'show'})
    print(r.status_code, r.reason)
    print("worked")

def checkMail():
    global prev_val
    for index, sensor in enumerate(IR_SENSORS):
        val = GPIO.input(sensor)
        print("[*] {}: prev_val: {} value: {}".format(IR_SENSORS[index], prev_val[index], val))
        if val != prev_val[index] and val == 0:
            prev_val[index] = val
            callChris()
        prev_val[index] = val

def setup():
    GPIO.setmode(GPIO.BCM)
    print("[*] Set board to GPIO.BCM")
    for sensor in IR_SENSORS:
        print("[*] Setting up sensor on pin {}".format(sensor))
        GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    setup()
    while True:
        checkMail()
        #Waits one second before submitting another checkMail request
        time.sleep(1)

main()
