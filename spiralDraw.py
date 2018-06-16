# python3

import pyautogui
import time

print('Taking control in 5 seconds...)')
time.sleep(5)

pyautogui.click()  # click to put drawing program in focus
distance = 200

# DO NOT FUCK AROUND WITH DISTANCE IT WILL GO OUT OF THE BOX

# FURTHERMORE, YOU CANT CTRL-C OUT OF IT BECAUSE YOURE IN ANOTHER PROGRAM

# HOLY FUCK HOMIE THIS IS COOL BUT ALSO VERY DANGEROUS
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)   # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2)   # move down
    pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2)  # move up

print('\nDrawing complete.')
