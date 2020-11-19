#!/usr/bin/env python3

from tree import RGBXmasTree
from time import sleep
from colorzero import Color, Hue

tree = RGBXmasTree(brightness=0.05)

# Bottom layer
bottom_layer = [0, 6, 7, 12, 15, 16, 19, 24]

# Middle layer
middle_layer = [1, 5, 8, 11, 14, 17, 20, 23]

# Uper layer
uper_layer = [2, 4, 9, 10, 13, 18, 21, 22]

# top star
top_star = 3

# speed
speed = 0.5

# start color
random_color = Color('red')
color_off = (0, 0, 0)

def lights_going_up():

    global random_color
    global color_off

    # Bottom layer on green
    for i in bottom_layer:
        tree[i].color = random_color
    sleep(speed)

    # Bottom layer off
    for i in bottom_layer:
        tree[i].color = color_off

    # Middle layer on green
    for i in middle_layer:
        tree[i].color = random_color
    sleep(speed)

    # Middle layer off
    for i in middle_layer:
        tree[i].color = color_off

    # Top layer on green
    for i in uper_layer:
        tree[i].color = random_color
    sleep(speed)

    # top layer off
    for i in uper_layer:
        tree[i].color = color_off

    # star on
    tree[3].color = random_color
    sleep(speed)

    # star off
    tree[3].color = color_off

    random_color += Hue(deg=20)


try:
    while True:
        lights_going_up()
except KeyboardInterrupt:
    tree.close()
