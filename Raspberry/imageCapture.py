import cv2
from datetime import datetime
import time

PATH = "images/"
count = 0
cam = cv2.VideoCapture(0)


while True:
    savestring = PATH + str(count) + ".png"
    ret, image = cam.read()

    if ret:
        cv2.imwrite(savestring, image)
        print("Image successfully saved " + savestring)
        time.sleep(5)
        count += 1

    else:
        print("No image detected. Please! try again")