import cv2

#capturing video
video = cv2.VideoCapture(0)
check, frame1 = video.read()    #Defining two frames as motion is based the difference in two frames
check, frame2 = video.read()

while True:
    diff = cv2.absdiff(frame1, frame2)  #absolute difference of two frames
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)   #converting diff to grayscale
    blur = cv2.GaussianBlur(gray,(5,5),0)
    (_,thresh) = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)    #every pixel value is compared to threshold value. If value is < threshold, it will be 0. Else 255(max value)
    dilated = cv2.dilate(thresh, None, iterations=3)    #increases the size of foreground object and hence reducing noise.
    (contours,_) = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)    #create a shape around the object

