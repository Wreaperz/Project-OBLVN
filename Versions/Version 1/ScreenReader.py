# Project OBLVN - ScreenReader.py
# Screen Reading functions for OBLVN AI

##### Imports #####
import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui as pag
import time
import math
###################

# Define the pixel regions for Player Stat Values
##health_region = frame[1000:1045, 575:645]
##armor_region = frame[1000:1050, 535:573]
##mag_region = frame[1010:1045, 1275:1330]
##reserves_region = frame[1013:1036, 1352:1378]

##### Light and Dark PURPLE (Purple Enemy Highlights) #####
light_color = np.array([145,80,80])
dark_color = np.array([170,255,255])

##light_color = np.array([28,80,80])
##dark_color = np.array([32,255,255])

##### Get Screen Width and Height #####
screen_width, screen_height = pag.size()
midX = screen_width / 2
midY = screen_height / 2

##### Grab the Screen and Find Enemies #####
def GrabFrame():
    ##### Grab screen, blur, and get contours #####
    # 'Targets' array holds all information about ENEMIES
    targets = []
    # Grab the screen (full dimensions)
    img = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height)) #x, y, w, h
    # Convert to NumPy Array
    img_np = np.array(img)
    # Convert the image to HSV
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
    # Get the image mask for the PURPLE color range (enemy outlines)
    mask = cv2.inRange(frame, light_color, dark_color)
    # Get the output (just purple outlines)
    output = cv2.bitwise_and(frame,frame, mask=mask)
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (17, 17), 0)
    _, threshold = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bounding_rects = []
    ##### For every contour, draw bounding rects #####
    for contour in contours:
        rect = cv2.boundingRect(contour)
        x, y, w, h = rect

        ##### Determine the most extreme points along the contour #####
        extLeft = tuple(contour[contour[:, :, 0].argmin()][0])
        extRight = tuple(contour[contour[:, :, 0].argmax()][0])
        extTop = tuple(contour[contour[:, :, 1].argmin()][0])

##        ##### Draw Rectangles Around Contour'd Enemies #####
##        cv2.rectangle(output,(x,y),(x+w,y+h),(255, 124, 0), 1)
##
##        ##### Draw Extreme Points and Connect Left/Right Sides #####
##        cv2.line(output, extLeft, extRight, (0, 128, 255), 1) # Orange #####
##        cv2.circle(output, extLeft, 3, (0, 255, 0), -1) # Green #####
##        cv2.circle(output, extRight, 3, (0, 255, 0), -1) # Green #####
##        cv2.circle(output, extTop, 3, (255, 0, 0), -1) # Blue #####

        ##### Get the average height between left and right and find the diff from top #####
        chest = (int((extLeft[0] + extRight[0]) / 2), int((extLeft[1] + extRight[1]) / 2))
        h1 = int((((extLeft[1] + extRight[1]) / 2) - extTop[1]) / 2)
        head = (extTop[0], int(extTop[1] + h1))

##        ##### Draw circle on midpoint of Left-Right Line (CHEST) and HEAD #####
##        cv2.circle(output, chest, 3, (0, 0, 255), -1)
##        cv2.circle(output, head, 3, (0, 0, 255), -1)

        ##### Get Area of BoundingBox to Determine Largest #####
        area = w * h

        temp_rect = []
        temp_rect.append(extLeft)
        temp_rect.append(extRight)
        temp_rect.append(extTop)
        temp_rect.append(chest)
        temp_rect.append(head)
        temp_rect.append(area)

        targets.append(temp_rect)

##        ##### Get current time, take screenshot, and save OUTPUT window #####
##        timestr = time.strftime("%m-%d-%Y-%H-%M-%S")
##        cv2.imwrite("overlay_images/overlay_" + timestr + ".png", output)

    # Get the closest target to the mouse
    target = GetClosest(targets)

    # Return the closest target
    return target


# Function to calculate distance between mouse and targets
def distance(x1, x2, y1, y2):
    return int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

# Function to get the target closest to the current mouse position
def GetClosest(targets):
    dist = 9999
    ind = 0
    # For every target, get the closest (using the DISTANCE function)
    for target in targets:
        head = target[4]
        d = distance(midX, head[0], midY, head[1])
        # If the distance is the smallest yet, make that target the closest
        if d < dist:
            dist = d
            ind = targets.index(target)
    # Return the closest target
    return targets[ind]


###############################################################################
###### Used to Run GrabFrame outside of Controller.py (self-sufficiently) #####
###############################################################################

time.sleep(2)
GrabFrame()
