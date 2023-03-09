# Project OBLVN - Extras.py
# Extra functions for OBLVN AI

import pyautogui as pag
import time

# Function that simplifies sleep calls (uses MS)
def sleep(sec):
    s = sec / 1000
    time.sleep(s)

# Function used to control messages sent to chat
def chat(msg):
    sleep(50)
    pag.keyDown("enter")
    sleep(50)
    pag.keyUp("enter")
    sleep(50)
    pag.write(msg)
    sleep(50)
    pag.keyDown("enter")
    sleep(50)
    pag.keyUp("enter")

# Function used to determine if mouse is on item in shop
def is_mouse_within_square(x1, y1, x2, y2):
    mouse_x, mouse_y = pag.position()
    if x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2:
        return True
    return False
