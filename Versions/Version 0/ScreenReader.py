# Project OBLVN - ScreenReader.py
# Screen Reading functions for OBLVN AI

import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui as pag
import time

# Light and Dark PURPLE (Purple Enemy Highlights)
light_color = np.array([145,80,80])
dark_color = np.array([170,255,255])

# Get Screen Width and Height
screen_width, screen_height = pag.size()

def GrabFrame():
#while True:
    # Grab screen, blur, and get contours
    targets = []
    img = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height)) #x, y, w, h
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame, light_color, dark_color)
    output = cv2.bitwise_and(frame,frame, mask=mask)
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (17, 17), 0)
    _, threshold = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bounding_rects = []
    # For every contour, draw bounding rects
    for contour in contours:
        rect = cv2.boundingRect(contour)
        x, y, w, h = rect

        # Draw Rectangles Around Contour'd Enemies
        #cv2.rectangle(output,(x,y),(x+w,y+h),(255, 124, 0), 1)

        # Determine the most extreme points along the contour
        extLeft = tuple(contour[contour[:, :, 0].argmin()][0])
        extRight = tuple(contour[contour[:, :, 0].argmax()][0])
        extTop = tuple(contour[contour[:, :, 1].argmin()][0])
        
        # Draw Extreme Points and Connect Left/Right Sides
        #cv2.line(output, extLeft, extRight, (0, 128, 255), 1) # Orange
        #cv2.circle(output, extLeft, 3, (0, 255, 0), -1) # Green
        #cv2.circle(output, extRight, 3, (0, 255, 0), -1) # Green
        #cv2.circle(output, extTop, 3, (255, 0, 0), -1) # Blue

        # Draw circle on midpoint of Left-Right Line (CHEST)
        chest = (int((extLeft[0] + extRight[0]) / 2), int((extLeft[1] + extRight[1]) / 2))
        #cv2.circle(output, chest, 3, (0, 0, 255), -1)

        # Draw circle on HEAD
        # Get the average height between left and right and find the diff from top
        h1 = int((((extLeft[1] + extRight[1]) / 2) - extTop[1]) / 2)
        head = (extTop[0], int(extTop[1] + h1))
        #cv2.circle(output, head, 3, (0, 0, 255), -1)

        # Get Area of BoundingBox to Determine Largest
        area = w * h
        
        temp_rect = []
        temp_rect.append(extLeft)
        temp_rect.append(extRight)
        temp_rect.append(extTop)
        temp_rect.append(chest)
        temp_rect.append(head)
        temp_rect.append(area)
        
        #print("Extreme Left: ", str(extLeft))
        #print("Extreme Right: ", str(extRight))
        #print("Extreme Top: ", str(extTop))
        #print("HEAD: ", str(head))
        #print("CHEST: ", str(chest))
        #print("AREA: ", str(area))
        #print()
        
        targets.append(temp_rect)

        # Get current time, take screenshot, and save OUTPUT window
        #timestr = time.strftime("%m-%d-%Y-%H-%M-%S")
        #cv2.imwrite("overlay_images/v1_" + timestr + ".png", output)
        
    #cv2.imshow("Color Recognition", output)
    #if cv2.waitKey(1) & 0Xff == ord('q'):
        #break
    return targets
#cv2.destroyAllWindows()

time.sleep(2)
GrabFrame()
