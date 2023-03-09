# Project OBLVN - Controller.py
# Main file for controlling input to OBLVN AI

import time
import serial
import pyautogui as pag
import math

import keyboard

from ScreenReader import *
from Extras import *
from Weapon import *
from Movement import *
from Abilities import *

# Get Screen Width and Height
screen_width, screen_height = pag.size()

# Disable PyAutoGUI Mouse-Past-Corner Failsafe - BE CAREEFUL
pag.FAILSAFE = False

# Setup Arduino Serial Port Connection
arduino = serial.Serial('COM5', 115200)

# Set Headshot Bool
headshot = True

def mousemove(x, y):
    if x < 0: 
        x = x + 256
    if y < 0:
        y = y + 256
    pax = [int(x)]
    pay = [int(y)]
    arduino.write(pax)
    arduino.write(pay)

def distance(x1, x2, y1, y2):
    return int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

def GetTargets(targets):
    midX = screen_width / 2
    midY = screen_height / 2
    dist = 9999
    ind = 0
    for target in targets:
        head = target[4]
        d = distance(midX, head[0], midY, head[1])
        if d < dist:
            dist = d
            ind = targets.index(target)
    extLeft, extRight, extTop, chest, head, area = targets[ind]
    # Ensure BoundingBox from Team Bars isn't being used
    if (extTop[1] >  75):
        # Get the head and chest (X, Y), as well as relative coords
        HeadX = int(head[0])
        HeadY = int(head[1])
        ChestX = int(head[0])
        ChestY = int(head[1]) 
    # Set mouse speed and get distance from center to head (at speed with remainder)
    speed = 15
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    targetX = 0
    targetY = 0
    if (headshot):
        targetX = HeadX
        targetY = HeadY
    else:
        targetX = ChestX
        targetY = ChestY
    # Calculate distance and move mouse
    currentX = midX
    currentY = midY
    while currentX != targetX or currentY != targetY:
        xSpd = 0
        ySpd = 0
        if (currentX < targetX):
            if (targetX - currentX >= speed):
                xSpd = speed
            else:
                xSpd = targetX - currentX
        elif (currentX > targetX):
            if (currentX - targetX >= speed):
                xSpd = -abs(speed)
            else:
                xSpd = -abs(currentX - targetX)
        if (currentY < targetY):
            if (targetY - currentY >= speed):
                ySpd = speed
            else:
                ySpd = targetY - currentY
        elif (currentY > targetY):
            if (currentY - targetY >= speed):
                ySpd = -abs(speed)
            else:
                ySpd = -abs(currentY - targetY)
        currentX += xSpd
        currentY += ySpd
        mousemove(xSpd, ySpd)
    sleep(75)
    tap_fire()

def Search():
    targets = GrabFrame()
    if len(targets) > 0:
        GetTargets(targets)
        
sleep(2000)
for t in range(50):
    Search()

