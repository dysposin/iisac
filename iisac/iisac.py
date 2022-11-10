import os
from typing import Union
from pprint import pprint
from colorama import Back
import time
import operations as ops
import images
COLORS = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
#SCREEN_WIDTH, SCREEN_HEIGHT = os.get_terminal_size()
SCREEN_WIDTH, SCREEN_HEIGHT = (80, 24)


FILL=' '
TRANSPARENT = [' ', None]


def move_by(image, x, y):
    """
    Moves image by given amounts in either direction
    """

    negative = [0, 0]
    positive = [0, 0]
    if x < 0:
        negative[0] = abs(x)
    else:
        positive[0] = x
    if y < 0:
        negative[1] = abs(x)
    else:
        positive[1] = y
    image = ops.crop(image, *negative, *ops.size(image))
    image = ops.expand(image, *positive)
    image = ops.translate(image, *positive)

    return image


def demo():
    logo = [[Back.BLUE + 'd', 'v', 'd' + Back.RESET],
            [Back.BLUE + '<', 'o', '>' + Back.RESET]]

    canvas = images.box(SCREEN_WIDTH, SCREEN_HEIGHT, fill='.')

    coordinates = [int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)]
    speed = [-1, 1]
    logo = ops.expand(logo, *coordinates)
    logo = ops.translate(logo, *coordinates)

    while True:
        if not 1 < coordinates[0] < SCREEN_WIDTH-4:
            speed[0] *= -1
        if not 1 < coordinates[1] < SCREEN_HEIGHT-3:
            speed[1] *= -1
        coordinates = [sum(x) for x in zip(coordinates, speed)]
        logo = move_by(logo, *speed)
        final = ops.add(canvas, logo, FILL, TRANSPARENT)
        ops.draw(final, Back.RESET)
        time.sleep(.1)
        ops.clear_console()


if __name__=="__main__":
    demo()