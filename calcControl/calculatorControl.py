# Requires python3

import pyautogui
import os

# NOTE: Mac OS X Calculator squares seem to be 60x50 in pixel size (x=60, y=50)
right = 60
left = -60
up = -50
down = 50

# clicks a calculator button based off png name


def clickBttnRetina(bttnName):
    xCor, yCor = pyautogui.locateCenterOnScreen(bttnName + '.png')

    # Have to reduce by 50% due to retina display (which doubles resolution)
    xCor = xCor * 0.5
    yCor = yCor * 0.5

    print(bttnName + 'bttn clicked at ' + str(xCor), str(yCor))
    pyautogui.click(xCor, yCor)


# check if button is detected
def checkBttnExistsRetina(bttnName):
    os.chdir("/Users/cmaloney/Desktop/PythonProjects/automatedDrawBot-py/calcControl/calcPics")
    if pyautogui.locateCenterOnScreen(bttnName + '.png'):
        print(bttnName + " found")
        return True
    else:
        return False


# check if calculator value is 0, then reset calculator to 0 by clicking C/AC
def resetCalc():

    # if value is not 0, reset
    if checkBttnExistsRetina('calcValue0') is False:
        if checkBttnExistsRetina('calcC'):
            clickBttnRetina('calcC')
            clickBttnRetina('calcAC')
    # else
    else:
        print("Value assumed to be zero")
        return


# add 2 + 2
# Hardcoded actions
def twoPlustwo():
    resetCalc()
    clickBttnRetina('calc2')
    clickBttnRetina('calcPlus')
    clickBttnRetina('calc2')
    clickBttnRetina('calcEquals')
    print("Answer should be 4")


resetCalc()
twoPlustwo()
