# we will detect movement from a webcam and send an email of that image
# cv2 is a good library for this, and built on Numpy to handle arrays!
import cv2
import time
import glob
import os
from emailing import send_email

# Video, input 0 to select the native macOS camera
video = cv2.VideoCapture(0)

# Provide webcam time to load
time.sleep(1)

# Define variable for baseline frame
first_frame = None
status_list = []
count = 1

# clean out images folder before sending
def clean_folder():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)

while True:
    status = 0
    check, frame = video.read()

    # Convert to greyscale to process less color data/arrays
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2. GaussianBlur(gray_frame, (21, 21), 0)

    # Output our video
    #cv2.imshow("My video", gray_frame_gau)

    # Assign first frame on first run through loop to first frame variable
    if first_frame is None:
        first_frame = gray_frame_gau

    # Get Delta of frames we are comparing
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    # Output delta frame
    cv2.imshow("My video", delta_frame)

    # Classify pixel value of 30 or higher, set to 255. [1] --> get second item in the list
    # We want to avoid getting lots of white areas in the output to make this simpler so adjust as needed
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    # More iterations, more processing
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("My video", dil_frame)

    # Draw contours around our image so we can outline a box image we will capture
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Run loop again if fake object
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            # Change status value when one rectangle detected so we don't keep sending tons of emails
            status = 1
            # Store images we capture
            cv2.imwrite(f"images/{count}.png", frame)
            count = count + 1
            # Grab middle image, assuming that is the best one
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)
            image_object = all_images[index]

    # status_list is so we can detect when an object leaves
    status_list.append(status)
    # Grab only last two items/if they are changing/if object exited frame
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        send_email(image_object)
        clean_folder()

    print(status_list)

    cv2.imshow("Video", frame)

    key = cv2.waitKey(1)
    # Press q to end the program from your keyboard!
    if key == ord("q"):
        break

video.release()
