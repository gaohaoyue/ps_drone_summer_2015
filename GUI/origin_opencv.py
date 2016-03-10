__author__ = 'gary'
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
scale_down = 4
while (1):

    _, image = cap.read()
    orig_img = image
    img = cv2.GaussianBlur(orig_img, (5,5), 0)
    img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2HSV)
    img = cv2.resize(img, (len(orig_img[0]) / scale_down, len(orig_img) / scale_down))
    red_lower = np.array([0, 125, 0],np.uint8)
    red_upper = np.array([3, 255, 255],np.uint8)
    red_binary = cv2.inRange(img, red_lower, red_upper)
    dilation = np.ones((15, 15), "uint8")
    red_binary = cv2.dilate(red_binary, dilation)
    image, contours, hierarchy = cv2.findContours(red_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    largest_contour = None
    for idx, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            largest_contour = contour

    if not largest_contour == None:
        moment = cv2.moments(largest_contour)
        if moment["m00"] > 1000 / scale_down:
            rect = cv2.minAreaRect(largest_contour)
            rect = ((rect[0][0] * scale_down, rect[0][1] * scale_down), (rect[1][0] * scale_down, rect[1][1] * scale_down), rect[2])
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(orig_img, [box], 0, (0, 0, 255), 2)

    cv2.imshow("HSV Display",orig_img)
    k = cv2.waitKey(5)
    if k ==27:
        break

cv2.destroyAllWindows()