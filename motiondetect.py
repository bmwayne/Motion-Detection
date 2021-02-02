import cv2

#capturing video
video = cv2.VideoCapture(0)
check, frame1 = video.read()    #Defining two frames as motion is based the difference in two frames
check, frame2 = video.read()