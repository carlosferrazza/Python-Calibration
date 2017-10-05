# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 11:51:44 2017

@author:    Carlo Sferrazza
            PhD Candidate
            Institute for Dynamics Systems and Control
            ETH Zurich
            
Extracts the camera calibration parameters using opencv, and saves the images for
doing the same with the OCamLib Matlab Toolbox
"""

import sys
import os
sys.path.append(os.path.abspath('../functions'))
import cv2
from auxiliary_functions import acquireImages
from opencv_functions import opencvCalibrate
import pickle
from datetime import datetime

# Change here the index that corresponds to your camera
idx = 1

# Change here the path of the calibration file that you want to generate
PIK = "Data/opencv_calibration.dat"

# Change here the folder where you want to save the images
path = "Images"

# Change here the number of internal corners that have to be detected on the chessboard in each dimension
m = 9
n = 6

# termination criteria and calibration flags (see opencv documentation if you need to adapt them)
criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 30, 1e-6)
calibration_flags = cv2.fisheye.CALIB_RECOMPUTE_EXTRINSIC+cv2.fisheye.CALIB_CHECK_COND+cv2.fisheye.CALIB_FIX_SKEW


# You don't need to change anything else below
images = acquireImages(idx)

now = datetime.now()
path += now.strftime("/%Y%m%d-%H%M%S")
os.mkdir(path)
count = 0
for img in images:
    cv2.imwrite(os.path.abspath(path+"/im"+str(count)+".jpg"), img)    
    count += 1

ret, mtx, dist, rvecs, tvecs = opencvCalibrate(m,n,criteria,calibration_flags,images)

with open(PIK, "wb") as f:
        data = [ret,mtx,dist,rvecs,tvecs]
        pickle.dump(data, f)