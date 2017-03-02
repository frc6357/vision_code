import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#imagelist = [{"image": "/home/pi/OpencvTestPgms/FRC TEST 1.jpg", "range": 1}]
#If geany is complaining, make sure you have all tabs or all spaces for indentation 
loopcount = 0
while(loopcount < 1):
    exposure = cap.set(10, 0.05)
    ret, frame = cap.read()
    #imagelist = [{"image": "original_image.jpg", "range":24}]
    #frame = cv2.imread(imagelist[0]['image'])
    #cv2.imwrite('original_image.jpg', frame)
    #frame = cv2.imread(entry['image'])
    #cv2.imshow("frame", frame)
    #cv2.waitKey(0)
    
    #change color scale ot HSV
    #frame[:, :, 2] = 0
    #frame[:, :, 0] = 0 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #cv2.imshow("hsv", hsv)
    #cv2.waitKey(0)
    #set hue limit values
    lower_hue_limit = 64
    upper_hue_limit = 84
    mask = cv2.inRange(hsv, np.array([lower_hue_limit, 90, 20]), np.array([upper_hue_limit, 255, 255]))
    hue_plane = cv2.cvtColor(cv2.cvtColor(cv2.bitwise_and(hsv, hsv, mask=mask), cv2.COLOR_HSV2BGR), cv2.COLOR_BGR2GRAY)
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

    #maxLineGap = 500
    #minLinelength = 10
    x_list = []
    y_list = []
    theta_list = []
    lines = cv2.HoughLines(canny_edges, 1, np.pi/180,50)

        
        
    if lines is not None:
        print(len(lines))
        for line in lines:
            print ("line is")
            print (line)
            for rho,theta in line:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho              
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                print("================================")
                print(" a     b    x0   y0   x1   y1   x2   y2")
                print(a,b ,x0, y0, x1,y1,x2,y2)
                print("================================")
                #cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),1) 
                #cv2.imshow("lines 1", frame)
                #cv2.waitKey(0)

                
            theta_list.append(theta)
            
            print 
            #if (88/57.295) < theta < (92/57.295)
            if (np.abs((theta*57.295)-90) < 4.0 ) or (np.abs((theta*57.295)-270) < 4.0) or (  (np.abs((theta*57.295)-360) < 4.0 ) or (np.abs(theta*57.295)-180)< 4.0  ):   
               print ("INSIDE FIRST IF")
               # if (np.abs((theta*57.295)-90) < 4.0 ) or (np.abs((theta*57.295)-270)<4.0):
               if (np.abs(1-np.abs(b))<.1):
                    #x_list.append(theta)
                   # if (int((x1+x2)/2)):
                        
                        y_list.append(int((y1+y2)/2))
                        # y_list.append(y2)
                        print ("theta is (y side)")
                        print (theta)
                        print(y_list)
                        print ("y list added ===========================================================")
               #if (  (np.abs((theta*57.295)-360) < 4.0 ) or (np.abs(theta*57.295)-180)  <4.0):
               if (np.abs(1-np.abs(a))<.1):
                    #between 357 and 360 degrees
                    #y_list.append(theta)
                   # if (int((y2+y1)/2)):
                        print ("theta is (x side)")
                        print (theta)
                        x_list.append(int((x2+x1)/2))
                        #x_list.append(x2)
                        print(x_list)
                        print ("x list added ===========================================================")
                      
            else:
                print("No lines found")
                print("theta is")
                print (theta)
        cv2.imwrite('houghlines3.jpg', frame)
            
        cv2.imshow("lines", frame)
        cv2.waitKey(0)
    else:
        print("No lines Found")
    print("theta_list follows")
    print(theta_list)
    print("max_theta", max(theta_list))
    print("min_theta", min(theta_list))
    print("y_list follows")
    print(y_list)
    print("")
    print("x_list")
    print(x_list)
    print("")
    y_max = max(y_list)
    y_min = min(y_list)
    x_max = max(x_list)
    x_min = min(x_list)
    print ("max x ", x_max)
    print ("max y ", y_max)
    print ("min x ", x_min)
    print ("min y ", y_min)
    
    #cv2.line(frame,(0,y_max),(10000,y_max),(255,255,0),2)  # top line
    #cv2.line(frame,(0,y_min),(10000,y_min),(255,255,0),2)   # bottom line 
    #cv2.line(frame,(x_max,0),(x_max,10000),(255,255,0),2)   # right line 
    #cv2.line(frame,(x_min,0),(x_min,10000),(255,255,0),2)    # left line assuming bottom left originq
        
    cv2.line(frame,(x_min,y_min),(x_max,y_min),(255,255,0),2)   # top line
    cv2.line(frame,(x_min,y_min),(x_min,y_max),(255,255,0),2)   # bottom line 
    cv2.line(frame,(x_min,y_max),(x_max,y_max),(255,255,0),2)   # right line 
    cv2.line(frame,(x_max,y_max),(x_max,y_min),(255,255,0),2)    # left line assuming bottom left originq
    
    cv2.imshow("big_box",frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    loopcount = 1
    
    
    #pixel_h = (y_max - y_min)
    #angle = math.atan(780/(pixel_h*d)
    #print(angle)
    
    x_center = (x_max - x_min)/2
    y_center = (y_max - y_min)/2
    center_box = (x_center, y_center)
    print (center_box)
    
    
    
    #for x_center in center_box:
		#if x_center != 0:
			
    
		
      
    
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

# When everything done, release the capture
#cap.release()
cv2.destroyAllWindows()

# yesterday I went to the store and bought some eggs. When I got home I discovered that out of the dozen eggs I purchased, 11 were in tact and
# 1 was broken. I immediately turned around and went back to the local HEB. Upon arrival, I asked the nearest employee to talk to his manager.
# I told the manager, "bro one of my eggs is broken, can i get a new one?" to which he replied with, "sir I am sorry for the inconvenience, here is a 
# new free dozen of eggs" as he handed me a package.

# moral of the story, don't freak out because Tom the Manager can give you a free dozen of eggs if yours break
