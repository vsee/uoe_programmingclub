# Based on code from https://github.com/lzane/Fingers-Detection-using-OpenCV-and-Python
import sys
import traceback
import tellopy
import av
import cv2.cv2 as cv2
import numpy as np
import time
import copy
import math

# parameters
cap_region_x_begin=0.5  # start point/total width
cap_region_y_end=0.8  # start point/total width
threshold = 60  #  BINARY threshold
blurValue = 41  # GaussianBlur parameter
bgSubThreshold = 50
learningRate = 0
bgModel = cv2.createBackgroundSubtractorMOG2(0, bgSubThreshold)
# variables
triggerSwitch = False 

def printThreshold(thr):
    print("! Changed threshold to "+str(thr))


def removeBG(frame):
    fgmask = bgModel.apply(frame,learningRate=learningRate)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res


def calculateFingers(res,drawing):  
    hull = cv2.convexHull(res, returnPoints=False)
    if len(hull) > 3:
        defects = cv2.convexityDefects(res, hull)
        if type(defects) != type(None): 
            cnt = 0
            for i in range(defects.shape[0]):  # calculate the angle
                s, e, f, d = defects[i][0]
                start = tuple(res[s][0])
                end = tuple(res[e][0])
                far = tuple(res[f][0])
                a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
                if angle <= math.pi / 2:  # angle less than 90 degrees, treat as fingers
                    cnt += 1
                    cv2.circle(drawing, far, 8, [211, 84, 0], -1)
            return True, cnt
    return False, 0

cv2.namedWindow('trackbar')
cv2.createTrackbar('trh1', 'trackbar', threshold, 100, printThreshold)

def main():
    drone = tellopy.Tello()

    try:
        drone.connect()
        drone.wait_for_connection(60.0)

        retry = 3
        container = None
        while container is None and 0 < retry:
            retry -= 1
            try:
                container = av.open(drone.get_video_stream())
            except av.AVError as ave:
                print(ave)
                print('retry...')

        # skip first 300 frames
        frame_skip = 300
        
        while True:
            for frame in container.decode(video=0):
                if 0 < frame_skip:
                    frame_skip = frame_skip - 1
                    continue
                start_time = time.time()
                image = cv2.cvtColor(np.array(frame.to_image()), cv2.COLOR_RGB2BGR)
                f = image

                threshold = cv2.getTrackbarPos('trh1', 'trackbar')
                f = cv2.bilateralFilter(f, 5, 50, 100)  # smoothing filter
                f = cv2.flip(f, 1)  # flip the f horizontally
                cv2.rectangle(f, (int(cap_region_x_begin * f.shape[1]), 0),
                              (f.shape[1], int(cap_region_y_end * f.shape[0])), (255, 0, 0), 2)
                cv2.imshow('original', f)

                
                img = removeBG(f)
                img = img[0:int(cap_region_y_end * f.shape[0]),
                          int(cap_region_x_begin * f.shape[1]):f.shape[1]]  # clip the ROI
                cv2.imshow('mask', img)

                
                # convert the image into binary image
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (blurValue, blurValue), 0)
                cv2.imshow('blur', blur)
                ret, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)
                cv2.imshow('ori', thresh)

                # get the coutours
                thresh1 = copy.deepcopy(thresh)
                contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                length = len(contours)
                maxArea = -1
                if length > 0:
                    for i in range(length):  # find the biggest contour (according to area)
                        temp = contours[i]
                        area = cv2.contourArea(temp)
                        if area > maxArea:
                            maxArea = area
                            ci = i

                    res = contours[ci]
                    hull = cv2.convexHull(res)
                    drawing = np.zeros(img.shape, np.uint8)
                    cv2.drawContours(drawing, [res], 0, (0, 255, 0), 2)
                    cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3)

                    isFinishCal,cnt = calculateFingers(res,drawing)
                    print(f"Detected {cnt} fingers")                    

                cv2.imshow('output', drawing)

                
                cv2.waitKey(1)
                if frame.time_base < 1.0/60:
                    time_base = 1.0/60
                else:
                    time_base = frame.time_base
                frame_skip = int((time.time() - start_time)/time_base)
    
            k = cv2.waitKey(10)
            if k == 27:  # press ESC to exit
                break

    except Exception as ex:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        print(ex)
    finally:
        drone.quit()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
