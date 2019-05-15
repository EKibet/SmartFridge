import cv2
import numpy as np
import numpy as np
import cv2
import random
import time
from uuid import uuid4

cap = cv2.VideoCapture(1) # video capture source camera (Here webcam of laptop) 
# ret,frame = cap.read() # return a single frame in variable `frame`

while True:
    ret,frame = cap.read() # return a single frame in variable `frame`

    # generate a random time between 120 and 300 sec
    random_time = random.randrange(10,20)

    # wait between 120 and 300 seconds (or between 2 and 5 minutes)


    cv2.imshow('img1',frame) #display the captured image
    outfile = 'fridge_screenshots/%s.jpg' % (str(uuid4()))

    cv2.imwrite(outfile,frame)
    print ("Next picture in: %.2f minutes" % (float(random_time) / 60))

    cv2.destroyAllWindows()
    

cap.release()