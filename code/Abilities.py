# Project OBLVN - Movement.py
# Ability functions for OBLVN AI

import pyautogui as pag
from Extras import *

def trigger_q():
    pag.keyDown("q")
    sleep(50)
    pag.keyDown("q")
    
def trigger_c():
    pag.keyDown("c")
    sleep(50)
    pag.keyDown("c")

def trigger_e():
    pag.keyDown("e")
    sleep(50)
    pag.keyDown("e")

def trigger_ult():
    pag.keyDown("x")
    sleep(50)
    pag.keyDown("x")
