# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 11:42:23 2017

@author:    Carlo Sferrazza
            PhD Candidate
            Institute for Dynamics Systems and Control
            ETH Zurich
"""

import cv2
import sys


""" Shows three parallel video streams (original, undistorted through opencv, 
                                        undistorted through Scaramuzza's toolbox) """
def undistortedStream(idx, mtx, dist, mapx_persp_32, mapy_persp_32):
    cap = cv2.VideoCapture(idx)

    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1)


    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
    
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        
        # undistort
        dst = cv2.fisheye.undistortImage(gray, mtx, dist, None, newcameramtx)
        dst_scaramuzza = cv2.remap(gray, mapx_persp_32, mapy_persp_32, cv2.INTER_LINEAR)
        
        # Display the resulting frame
        cv2.imshow('undistorted opencv',dst)
        cv2.imshow('undistorted scaramuzza',dst_scaramuzza)
        cv2.imshow('original',gray)
    
        q = cv2.waitKey(1)
    
        if q & 0xFF == ord('q'):
            break
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    
""" Acquires images and returns them for calibration """
def acquireImages(idx):
    cap = cv2.VideoCapture(idx)
    images = []
    count = 0
    
    print("Press t for acquiring a new image, q to stop acquisition and proceed to calibration. "\
    "Try to collect at least 15 images from different viewpoints, and as close as possible "\
    "to the chessboard")
    sys.stdout.flush()
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
    
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # Display the resulting frame
        cv2.imshow('frame',gray)
    
        q = cv2.waitKey(1)
    
        if q & 0xFF == ord('t'):
            images.append(gray)
            print "Images acquired: ", count
            sys.stdout.flush()
            count+=1
        elif q & 0xFF == ord('q'):
            break
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    
    return images
    
