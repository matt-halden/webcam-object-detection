# we will detect movement from a webcam and send an email of that image
# cv2 is a good library for this, and built on Numpy to handle arrays!
import cv2
import time

# Video, input 0 to select the native macOS camera
video = cv2.VideoCapture(0)

# Provide webcam time to load
time.sleep(1)

while True:
    check, frame = video.read()

    # Output our video
    cv2.imshow("My video", frame)
    print(frame)

    key = cv2.waitKey(1)

    # Press q to end the program from your keyboard!
    if key == ord("q"):
        break

video.release()

"""
# Add in a one-second pause with time.sleep. 
# Without it, not enough time to capture image (outputs all 0s)
# Also, helps emulate a video/longer capture using webcam
check1, frame1 = video.read()
time.sleep(1)

check2, frame2 = video.read()
time.sleep(1)

check3, frame3 = video.read()
time.sleep(1)
"""

print(frame3)