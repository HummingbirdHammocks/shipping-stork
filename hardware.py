####
## Hardware
####

#!/usr/bin/env python3

import config

from gpiozero import Button, LED
from time import sleep
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import (
    proportional,
    CP437_FONT,
    TINY_FONT,
    SINCLAIR_FONT,
    LCD_FONT,
)

# Initialize matrix
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=8, block_orientation=-90)
print("Display Init")

# Pin Definitions

green = LED(17)
yellow = LED(27)
red = LED(22)


def updateLights(status):
    if status == 0:
        green.on()
        yellow.off()
        red.off()
        return
    elif status == 1:
        green.off()
        yellow.on()
        red.off()
        return
    elif status == 2:
        green.off()
        yellow.off()
        red.on()
        return
    else:
        green.off()
        yellow.off()
        red.off()
        return


def updateDisplay(revenue, count):

    # Display on matrix display
    msg_revenue = "$" + str(revenue)
    # print(msg)
    with canvas(device) as draw:
        text(draw, (0, 0), msg_revenue, fill="white")
        text(draw, (48, 0), str(count), fill="white")
