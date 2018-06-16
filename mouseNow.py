#! python3
# mouseNow.py - Displays the mouse cursor's current position BOY
import pyautogui
print('Press Ctrl-C to quit.')

try:
    while True:
        # TODO: Get and print the mouse coordinates.
        # Get and print the mouse coordinates.

        # getes x,y mouse coordinates, stores them in
        # multiple variables x and y
        x, y = pyautogui.position()

        # converts coordinate values to a string,
        # then Right Justifies them by 4
        # to print them all nice and pretty :}
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

        # now were adding RGB bitchness
        # NOTE: But it's uhh...not really working.
        # Doesnt seem to be getting correct values
        # pixelColor = pyautogui.screenshot().getpixel((x, y))
        # positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        # positionStr += ', ' + str(pixelColor[1]).rjust(3)
        # positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'

        # prints coordinates. end parameter is used to exclude
        # the newline character generated at end of string (print adds this)
        print(positionStr, end='')

        # prints a backspace character, essentially deleting the most recently
        # printed line (while loop constantly prints)
        # so only one line is shown
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')
