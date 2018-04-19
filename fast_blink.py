#!/usr/bin/env python

import time
from grovepi import *

# Connect the LED to digital port D3
led = 3

pinMode(led, "OUTPUT")


count = 0

while count < 60 :
    count += 1
    try:
       digitalWrite(led, 1)    # Send HIGH to switch on LED
       time.sleep(0.2)         # sleep 0.2 second
       digitalWrite(led, 0)    # Send LOW to switch on LED
       time.sleep(0.2)         # sleep 0.2 second

    except KeyboardInterrupt:
       digitalWrite(led, 0)
       break

    except IOError:
       print ("Error")
