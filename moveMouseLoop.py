# python 3

import pyautogui
import time
import random

print('Taking control in 5 seconds...)')
time.sleep(5)
distance = 200
pyautogui.click()  # click to put drawing program in focus

while True:
    pyautogui.moveRel(distance, 0, duration=random.randint(1,5))   # move right
    time.sleep(5)
    # distance = distance - 5
    pyautogui.moveRel(0, distance, duration=random.randint(1,5))   # move down
    time.sleep(5)
    pyautogui.moveRel(-distance, 0, duration=random.randint(1,5))  # move left
    time.sleep(4)
    # distance = distance - 5
    pyautogui.moveRel(0, -distance, duration=random.randint(1,5))  # move up
    time.sleep(3)