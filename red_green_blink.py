#!/usr/bin/env python

import time
from grovepi import *

# Connect the RED and GREEN LED to digital ports D3 and D4
led_1 = 3    # RED LED
led_2 = 4    # GREEN LED

pinMode(led_1, "OUTPUT")
pinMode(led_2, "OUTPUT")
time.sleep(1)

while True:
    try:
        #Blink the LED
        digitalWrite(led_1, 1)		# Send HIGH to switch on RED LED
        print ("LED_RED ON!")
        time.sleep(1)

        digitalWrite(led_1, 0)		# Send LOW to switch off RED LED
        print ("LED_RED OFF!")
        time.sleep(1)

        digitalWrite(led_2, 1)      # Send HIGH to switch on GREEN LED
        print ("LED_GREEN ON!")
        time.sleep(1)

        digitalWrite(led_2, 0)      # Send LOW to switch off GREEN LED
        print ("LED_GREEN OFF!")
        time.sleep(1)



    except KeyboardInterrupt:	# Turn LEDs off before stopping
        digitalWrite(led_1, 0)
        digitalWrite(led_2, 0)
        break

    except IOError:				# Print "Error" if communication error encountered
        print ("Error")