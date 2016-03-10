__author__ = 'gary'
import cv2
import numpy as np
import math


cap = cv2.VideoCapture(0)
scale_down = 1
while(1):

    _, image = cap.read()


    orig_img = image
    img = cv2.GaussianBlur(orig_img, (5,5), 0)
    img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2HSV)
    img = cv2.resize(img, (len(orig_img[0]) / scale_down, len(orig_img) / scale_down))
    red_lower = np.array([0, 120, 0],np.uint8)
    red_upper = np.array([10, 200, 255],np.uint8)
    red_binary = cv2.inRange(img, red_lower, red_upper)
    dilation = np.ones((15, 15), "uint8")
    red_binary = cv2.dilate(red_binary, dilation)
    #gray = cv2.bilateralFilter(red_binary,11,17,17)
    gray = red_binary
    edged = cv2.Canny(gray,30, 200)
    image, cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]

    max_area = 0
    largest_contour = None
    for idx, contour in enumerate(cnts):
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            largest_contour = contour

    screenCnt = None
    box = None
    box1 = None
    center = (0, 0)
    radius = 0
    #for c in cnts:
    # approximate the contour
    if largest_contour != None:
        peri = cv2.arcLength(largest_contour, True)
        approx = cv2.approxPolyDP(largest_contour, 0.08 * peri, True)

        # if our approximated contour has four points, then
        # we can assume that we have found our screen
        #if len(approx) == 4 :
        screenCnt = approx * scale_down
        #break

        #print "scren cnt",approx

        #if screenCnt != None:
            #print "scren cnt", screenCnt
            #print "scren cnt1", screenCnt[0][0][0],screenCnt[0][0][1],screenCnt[1][0][0],screenCnt[1][0][1],screenCnt[2][0][0],screenCnt[2][0][1],screenCnt[3][0][0],screenCnt[3][0][1]

        rect = cv2.minAreaRect(largest_contour)
        box1 = cv2.boxPoints(rect)
        box1 = np.int0(box1)

    #cv2.circle(orig_img,center,radius,(0,0,255),2)
    cv2.drawContours(orig_img,[box1],0, (0,255,0),3)
    cv2.drawContours(orig_img, [screenCnt], -1, (0, 0, 255), 3)
    cv2.imshow("output",orig_img)
    cv2.imshow("gray",gray)
    cv2.imshow("edged",edged)
    k = cv2.waitKey(5)
    if k ==27:
        break

cv2.destroyAllWindows()



'''_, img = cap.read()
    ret,thresh = cv2.threshold(img,127,255,0)
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    M = cv2.moments(cnt)
    #cx = int(M['m10']/M['m00'])
    #cy = int(M['m01']/M['m00'])
    epsilon = 0.1*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    cv2.imshow('output',epsilon)'''
'''   image, contours, hierarchy = cv2.findContours(red_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    max_area = 0
    largest_contour = None
    for idx, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            largest_contour = contour
    if largest_contour == None:
        q.put([orig_img, []])

    if not largest_contour == None:
        moment = cv2.moments(largest_contour)
        if moment["m00"] > 1000 / scale_down:
            rect = cv2.minAreaRect(largest_contour)
            rect = ((rect[0][0] * scale_down, rect[0][1] * scale_down), (rect[1][0] * scale_down, rect[1][1] * scale_down), rect[2])
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            q.put([orig_img, box])

'''
'''
        if x1 >= x2:
            x1 = xl
            x2 = xs
        else:
            x2 = xl
            x1 = xs
        if y1 >=y2:
            y1 = yl
            y2 = ys
        else:
            y1 = ys
            y2 = yl

        box = ( (xl, yl),  (xs, yl),  (xs, ys),  (xl, ys) )'''
''' xl =1000000
    xs = -1
    yl = 1000000
    ys = -1
    box=[]'''


'''
s=screenCnt
        x1=s[0][0][0]
        y1 = s[0][0][1]
        x2 = s[1][0][0]
        y2 = s[1][0][1]
        x = (x1+x2)/2
        y = (y1+y2)/2
        center = (int(x),int(y))
        radius = int(math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2)))
        '''