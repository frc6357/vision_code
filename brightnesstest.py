import numpy as np
import cv2
import time
import os

os.system('v4l2-ctl -d /dev/video0 -c exposure_auto=1 -c exposure_auto_priority=0 -c exposure_absolute=0.1')

cap = cv2.VideoCapture(0)
#for i in range (0,30):
#    j = cap.get(i)
#    print (j)
#print ("set exposure")
#time.sleep(2)
print (cap.set(10, 0.05))
#cv2.waitKey(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #cv2.imshow('frame',gray)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
