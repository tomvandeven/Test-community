# Import all required functions

import machine
import d1_mini
import neopixel
import time
import random


# Number of the LEDs on the shield

NumberOfLeds = 7


# Seconds between turning ON and OFF the LED

NumberOfSecondsToWait = 0.005

# time the dicerolls
dicerollTimeGone = 1
# create random number for each dice roll to last
dicerollTime = NumberOfLeds*random.getrandbits(4)
print('randnr: ', dicerollTime, '\n')
# or use fixed number to test   dicerollTime = = 16


# Create the colours

RED = (25, 0, 0)

GREEN = (0, 25, 0)

BLUE = (0, 0, 25)

YELLOW = (25, 25, 0)

PURPLE = (25, 0, 25)

WHITE = (25, 25, 25)

PINK = (25, 5, 10)

# Create a list of colours

Colours = [RED, GREEN, BLUE, YELLOW, PURPLE, WHITE, PINK]


# Initialise the board

np = neopixel.NeoPixel(machine.Pin(d1_mini.D4), 7)
np.fill((0,0,0))
np.write()

# Create a loop

while dicerollTimeGone < dicerollTime:

    # Create a for loop to go through the colours and the LEDs

    for counter in range(NumberOfLeds):
        # Turn the specific LED with a specific colour
        np[counter] = Colours[counter]
        np.write()
        # Wait for some time
        time.sleep(NumberOfSecondsToWait)
        # Turn the LED OFF
        np[counter] = (0, 0, 0)
        np.write()
    # slow down the light cycle
    NumberOfSecondsToWait = NumberOfSecondsToWait + 0.01
    # count until stop
    dicerollTimeGone = dicerollTimeGone + 1
    print(dicerollTimeGone/NumberOfLeds)
# Finalize with one led turned on
for counterFinal in range(dicerollTimeGone/NumberOfLeds):
    # Turn the specific LED with a specific colour
    np[counterFinal] = Colours[counterFinal]
    np.write()
    # Wait for some time
    time.sleep(NumberOfSecondsToWait)
    # Turn the LED OFF
    np[counterFinal] = (0, 0, 0)
    np.write()
np[counterFinal] = Colours[counterFinal]
np.write()
