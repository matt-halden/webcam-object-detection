# Webcam Object Detection App

When running this app, it will pull up your webcam & detect an object
coming into the frame. When the object leaves, it will capture the ideal frame
and send as an email attachment.

Libraries: cv2, threading, glob, time, smtplib, email.message, imghdr

Skills: Object detection, image processing, email sending (w/ attachment), 
threading