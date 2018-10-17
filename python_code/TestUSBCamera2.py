import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    blue_plane, green_plane, red_plane= cv2.split(frame)
    green_plane = frame[:, :, 1]
    #frame[:, :, 2] = 0
    # Display the resulting frame
    cv2.imshow('frame', frame)
    # cv2.waitKey=(0)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
