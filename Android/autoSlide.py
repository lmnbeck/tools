import subprocess
import time

#   MIX2 eb606528 
while(True):
    os.system("adb -s eb606528 shell input swipe 540 1300 540 900 220")
    time.sleep(2)
