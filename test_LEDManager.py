import time

from LEDManager import LEDManager


man = LEDManager()

time.sleep(2)

#Blinks the LEDs in 3 different patterns
man.setLEDs(0, 0, 0)
time.sleep(1)
man.setLEDs(1, 0, 0)
time.sleep(1)

man.setLEDs(0, 1, 0)
time.sleep(1)
man.setLEDs(1, 1, 0)
time.sleep(1)

man.setLEDs(0, 0, 1)
time.sleep(1)
man.setLEDs(1, 0, 1)
time.sleep(1)

man.setLEDs(0, 1, 1)
time.sleep(1)
man.setLEDs(1, 1, 1)
time.sleep(1)
