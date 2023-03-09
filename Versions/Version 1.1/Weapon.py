# Project OBLVN - Weapon.py
# Weapon functions for OBLVN AI

import pyautogui as pag
from Extras import *

# Function used to Tap-Fire (1 Bullet)
def tap_fire():
    pag.leftClick()

# Function used to Spray (for X time)
def spray_n_pray(time):
    pag.mouseDown()
    sleep(time)
    pag.mouseUp()

def scope_in():
    pag.mouseDown(button="right")

def scope_out():
    pag.mouseUp(button="right")

def equip_primary():
    pag.keyDown("1")
    sleep(50)
    pag.keyDown("1")

def equip_secondary():
    pag.keyDown("2")
    sleep(50)
    pag.keyDown("2")

def equip_knife():
    pag.keyDown("3")
    sleep(50)
    pag.keyDown("3")
