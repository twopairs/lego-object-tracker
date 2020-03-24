import os
import sys
import time

sys.stdout = open(os.devnull, "w")
sys.stderr = open(os.devnull, "w")

while True:
    os.system('fswebcam -d /dev/video0 -r 3200*2400 -v -S 10 --no-banner test_image.jpg')
    time.sleep(5)
