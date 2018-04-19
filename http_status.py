import httplib
import threading
from grovepi import *

# Check status web site
host = "blog.piesso.com"
path = "/"

# connect the led to digital ports
led_3 = 3    # red led
led_4 = 4    # green led


def led_blink(led_x):
    pinMode(led_x, "OUTPUT")
    digitalWrite(led_x, 1)

def led_close(led_x):
    digitalWrite(led_x, 0)

def get_status_code():
    try:
        conn = httplib.HTTPSConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status

    except StandardError:
        return None

def http_ok():
    led_blink(led_4)

def http_fail():
    led_blink(led_3)



def main():
    threading.Timer(10, main).start()
    code = get_status_code()

    if (code == 200):
        led_close(led_3)
        http_ok()

    else:
        led_close(led_4)
        http_fail()


main()