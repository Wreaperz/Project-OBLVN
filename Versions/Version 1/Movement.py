# Project OBLVN - Movement.py
# Movement functions for OBLVN AI

import pyautogui as pag
from Extras import *
from Weapon import *
import random

# Function used to start moving in a direction
def start_move(direction):
    pag.keyDown(direction)

# Function used to stop moving in a direction
def stop_move(direction):
    pag.keyUp(direction)

# Function used to start shift-walking
def start_shift():
    pag.keyDown("shiftleft")

# Function used to stop shift-walking
def stop_shift():
    pag.keyUp("shiftleft")

# Function used to start crouching
def start_crouch():
    pag.keyDown("ctrlleft")

# Function used to stop crouching
def stop_crouch():
    pag.keyUp("ctrlright")

# Function used to move X units to FORWARD
def forward(units):
    pag.keyDown("w")
    sleep(units*100)
    pag.keyUp("w")

# Function used to move X units to BACKWARD
def backward(units):
    pag.keyDown("s")
    sleep(units*100)
    pag.keyUp("s")

# Function used to move X units to LEFT
def left(units):
    pag.keyDown("a")
    sleep(units*100)
    pag.keyUp("a")

# Function used to move X units to RIGHT
def right(units):
    pag.keyDown("d")
    sleep(units*100)
    pag.keyUp("d")

# Randomly choose whether to strafe LEFT or RIGHT, and then Re-Balance
def counter_strafe():
    r = random.choice([0, 1])
    if r == 0:
        left(2)
        sleep(50)
        right(2)
    else:
        right(2)
        sleep(50)
        left(2)
