from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import AngularServo,LED
import subprocess
import os
import time
os.system("sudo systemctl start pigpiod")
ledr = LED(17)
ledl = LED(27) 
ledr.on()
ledl.on()
#pi = pigpio.pi('pi', 8889)
factory = PiGPIOFactory()
s2 = AngularServo(12,pin_factory=factory,min_angle=0, max_angle=180)
for i in range(0,180):
      s2.angle= int(i)
      time.sleep(0.1)
for i in reversed(range(0,180)):
      s2.angle=int(i)
      time.sleep(0.1)
