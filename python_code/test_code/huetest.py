import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#imagelist = [{"image": "/home/pi/OpencvTestPgms/FRC TEST 1.jpg", "range": 1}]
#If geany is complaining, make sure you have all tabs or all spaces for indentation 
while(True):
    #for i, entry in enumerate(imagelist):
      # Capture frame-by-frame
      ret, frame = cap.read()
      #frame = cv2.imread(entry['image'])
      cv2.imshow("frame", frame)
      cv2.waitKey(0)
      exposure = cap.set(10, 0.05)
      #change color scale ot HSV
      #frame[:, :, 2] = 0
      #frame[:, :, 0] = 0 
      hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      cv2.imshow("hsv", hsv)
      cv2.waitKey(0)
      #set hue limit values
      lower_hue_limit = 20
      upper_hue_limit = 80
      mask = cv2.inRange(hsv, np.array([lower_hue_limit, 90, 20]), np.array([upper_hue_limit, 255, 255]))
      hue_plane = cv2.split(cv2.cvtColor(cv2.bitwise_and(hsv, hsv, mask=mask), cv2.COLOR_HSV2BGR))[1]
      threshold, thresh_image = cv2.threshold(hue_plane, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
      cv2.imshow("thresh image", thresh_image)
      cv2.waitKey(0)
      #find canny edges
      canny_edges = cv2.Canny(thresh_image, 100, 150)
      cv2.imshow("canny_edges", canny_edges)
      cv2.waitKey(0)
      #find sobel x-coordinates
      #sobelx = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)
      #cv2.imshow("sobelx", sobelx)
      #cv2.waitKey(0)
      #find sobel y-coordinates
      #sobely = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
      #cv2.imshow("sobely", sobely)
      #cv2.waitKey(0)
      #show thresh image      
      #find hough lines
      #lines = cv2.HoughLines(canny_edges, 1, np.pi/180, 200)
      #cv2.imshow("lines", lines)
      #cv2.waitKey(0)
      
      
    
    
      if cv2.waitKey(0) & 0xFF == ord('q'):
          break

# When everything done, release the capture
#cap.release()
cv2.destroyAllWindows()
