import os
import time
import subprocess

import cv2 as cv
from django.shortcuts import render


def VideoCapture():
    capture = cv.VideoCapture(0)
    count = 0 

    start_time = int(time.time())
    while True:
        isTrue, frame = capture.read()
        key = cv.waitKey(1)

        cv.imshow("Cam Video",frame)

        if key == ord('q'):
            break

        
        current_time = int(time.time())
        
        isTenSec = current_time - start_time

        if isTenSec >= 10:
            start_time = current_time
            print("Time difference : ",isTenSec)
            if count == 0:
                name = f'pages/images/saved_img.jpg'
                count += 1
            else:
                name = f'pages/images/saved_img{count}.jpg'
                count += 1
            cv.imwrite(filename=str(name), img=frame)
    capture.release()
    cv.destroyAllWindows()


def demo(request):
    data = {
        "username" : "Himanshu Gupta",
        "info" : "Camera is off"
    }
    return render(request, "index.html", data)

def CamOn(request):
    # exec(open('pages/cam_capture.py').read())
    # subprocess.call(" python pages/cam_capture.py", shell=True)
    os.system('python pages/cam_capture.py')
    # call(["python", "pages/cam_capture.py"])
    data = {
        "username" : "Himanshu Gupta",
        "info" : "Camera is on"
    }
    return render(request, "index.html", data)