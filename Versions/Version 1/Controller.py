# Project OBLVN - Controller.py
# Main file for controlling input to OBLVN AI

#------------- GENERIC IMPORTS -------------#
import serial
import pyautogui as pag
import keyboard
import random
from playsound import playsound
#-------------------------------------------#


#------------- IMPORTED LIBRARIES -------------#
from ScreenReader import *
from Extras import *
from Weapon import *
from Movement import *
from Abilities import *
import Vars
#----------------------------------------------#

# Disable PyAutoGUI Mouse-Past-Corner Failsafe - BE CAREEFUL
pag.FAILSAFE = False

# Setup Arduino Serial Port Connection
arduino = serial.Serial('COM5', 1200)

# Function that sends Mouse-Move Commands to Arduino Leonardo
def mousemove(x, y):
    while Vars.is_shooting:
        if x < 0:
            x = x + 256
        if y < 0:
            y = y + 256
        pax = [int(x)]
        pay = [int(y)]
        arduino.write(pax)
        arduino.write(pay)
    if x < 0:
        x = x + 256
    if y < 0:
        y = y + 256
    pax = [int(x)]
    pay = [int(y)]
    arduino.write(pax)
    arduino.write(pay)
    # Mouse acceleration
    dist = math.sqrt((x - midX)**2 + (y - midY)**2)
    speed = min(max(0.3 * dist, 1), 30)
    pag.moveTo(x, y, speed=speed/100, tween=pag.easeInOutQuad, duration=0.5)

# Function that gets closest target and shoots it
def Eliminate(target):
    extLeft, extRight, extTop, chest, head, area = target
    # Ensure BoundingBox from Team Bars isn't being used
    if (extTop[1] >  75):
        # Get the head and chest (X, Y), as well as relative coords
        HeadX = int(head[0])
        HeadY = int(head[1])
        ChestX = int(head[0])
        ChestY = int(chest[1])
        # Set mouse speed and get distance from center to head (at speed with remainder)
        speed = 10
        targetX = 0
        targetY = 0
        is_headshot = False
        # Determine the target location (with OBLVN_HAX or hs_percent)
        if Vars.OBLVN_HAX:
            targetX = HeadX
            targetY = HeadY
            is_headshot = True
        else:
            rand = random.random()
            if rand > Vars.hs_percent:
                targetX = ChestX
                targetY = ChestY
            else:
                targetX = HeadX
                targetY = HeadY
                is_headshot = True
        #print("(" + str(targetX) + ", " + str(targetY) + ")")
        # Get the Current Mouse Position (Center of Screen)
        currentX = midX
        currentY = midY
        # While the X or Y positions don't match up...
        while currentX != targetX or currentY != targetY:
            xSpd = 0
            ySpd = 0
            # If the target is to the LEFT...
            if (currentX < targetX):
                if (targetX - currentX >= speed):
                    xSpd = speed
                else:
                    xSpd = targetX - currentX
            # If the target is to the RIGHT...
            elif (currentX > targetX):
                if (currentX - targetX >= speed):
                    xSpd = -abs(speed)
                else:
                    xSpd = -abs(currentX - targetX)
            # If the target is DOWN...
            if (currentY < targetY):
                if (targetY - currentY >= speed):
                    ySpd = speed
                else:
                    ySpd = targetY - currentY
            # If the target is UP...
            elif (currentY > targetY):
                if (currentY - targetY >= speed):
                    ySpd = -abs(speed)
                else:
                    ySpd = -abs(currentY - targetY)
            # Add the movement to current location, and move the mouse
            currentX += xSpd
            currentY += ySpd
            mousemove(xSpd, ySpd)
        # Eliminate the target (tap for headshot or spray for body)
        sleep(100)
        if is_headshot:
            tap_fire()
            sleep(100)
        else:
            spray_time = 300
            start_time = time.time() * 1000
            pag.mouseDown()
            sleep(50)
            while (time.time() * 1000) - start_time < spray_time:
                mousemove(0, 3)
                sleep(10)
            pag.mouseUp()
            sleep(150)

def PlayAudio(loc):
    playsound(loc)

# Function that will eventually control screen-searching functions
def Search():
    while True:
        if keyboard.is_pressed('p'):
            PlayAudio("sounds/End.mp3")
            break
        else:
            target = GrabFrame()
            Eliminate(target)

def RunBot():
    # Endless loop where Keypress "P" Runs the Bot, and ESC Stops it
    while True:
        if keyboard.is_pressed('p'):
            PlayAudio("sounds/Start.wav")
            Search()
        if keyboard.is_pressed('h'):
            Vars.OBLVN_HAX = not Vars.OBLVN_HAX
            if Vars.OBLVN_HAX:
                PlayAudio("sounds/GunLoad.mp3")
            else:
                PlayAudio("sounds/PowerDown.wav")
        if keyboard.is_pressed('esc'):
            PlayAudio("sounds/Quit.mp3")
            arduino.close()
            break

RunBot()
