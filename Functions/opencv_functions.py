# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 12:02:33 2017

@author:    Carlo Sferrazza
            PhD Candidate
            Institute for Dynamics Systems and Control
            ETH Zurich
            
Calibration routine using the provided fisheye opencv libraries
"""

import numpy as np
import cv2

def opencvCalibrate(m,n,criteria,calibration_flags,images):
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((1,m*n,3), np.float32)
    objp[0,:,:2] = np.mgrid[0:m,0:n].T.reshape(-1,2)
    
    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    
    for gray in images:
    
        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (m,n),None)
    
        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)
    
            cv2.cornerSubPix(gray,corners,(3,3),(-1,-1),criteria)
            imgpoints.append(corners)
            # Draw and display the corners
            gray = cv2.drawChessboardCorners(gray, (m,n), corners,ret)
            cv2.imshow("img",gray)
            cv2.waitKey(0)
    
    cv2.destroyAllWindows()
    
    try:
        return cv2.fisheye.calibrate(objpoints, imgpoints, gray.shape[::-1],None,None,flags=calibration_flags)
    except:
        raise ValueError("Calibration failed: try to load new images")