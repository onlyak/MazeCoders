#!/usr/bin/env python3
import subprocess
import sys
import time
import os	


awaketime = int(float(sys.argv[1])*60)
sleeptime = int(float(sys.argv[2])*10)

message = "5 minutes remaining."
message1= "10 minutes remaining."
message2= "Your time will end in a minute. Please save your code!!!"

def take_a_break():
    get = subprocess.check_output(["xrandr"]).decode("utf-8").split()
    screens = [get[i-1] for i in range(len(get)) if get[i] == "connected"]
    for scr in screens:
        # uncomment either one of the commands below [1]
        # darken the screen, or...
        subprocess.call(["xrandr", "--output", scr, "--brightness", "1"])
        # turn it upside down :)
        # subprocess.call(["xrandr", "--output", scr, "--rotate", "inverted"])
    time.sleep(sleeptime)
    for scr in screens:
        # back to "normal"
        subprocess.call(["xrandr", "--output", scr, "--brightness", "1"])
        subprocess.call(["xrandr", "--output", scr, "--rotate", "normal"])
        
#while True:
time.sleep(awaketime-40)
subprocess.Popen(["notify-send", message1])
#while True:
time.sleep(awaketime-(awaketime-20))
subprocess.Popen(["notify-send", message])
time.sleep(awaketime-(awaketime-10))
subprocess.Popen(["notify-send", message2])
time.sleep(10)
os.system("gnome-screensaver-command -l")
take_a_break()
exit(0)
import os	



#python3 /path/to/takeabreak.py <uptime> <breaktime>