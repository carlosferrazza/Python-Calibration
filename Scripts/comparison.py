# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 11:38:41 2017

@author:    Carlo Sferrazza
            PhD Candidate
            Institute for Dynamics Systems and Control
            ETH Zurich
            
Compares the calibration and undistortion methods of OpenCV and OCamLib
"""

import sys
import os
sys.path.append(os.path.abspath('../functions'))

import pickle
from ocam_functions import get_ocam_model, create_perspective_undistortion_LUT
from auxiliary_functions import undistortedStream

# Change here the index that corresponds to your camera
idx = 1

# Change here the path of the calibration file that contains the parameters obtained through opencv_calibration.py
PIK_opencv = "Data/opencv_calibration.dat"

# Change here the path of the calibration file that contains the parameters obtained through ocam_calibration.py
path_ocam = "Data/ocam_calibration.txt"

# Change here the number of internal corners that have to be detected on the chessboard in each dimension
m = 9
n = 6

# Parameter that affect the result of Scaramuzza's undistortion. Try to change it to see how it affects the result
sf = 4.0

# You don't need to change anything else below
with open(PIK_opencv, "rb") as f:
    data = pickle.load(f)
    ret, mtx, dist, rvecs, tvecs = data
    
o = get_ocam_model(path_ocam)
mapx_persp, mapy_persp = create_perspective_undistortion_LUT(o, sf)
mapx_persp_32 = mapx_persp.astype('float32')
mapy_persp_32 = mapy_persp.astype('float32')

undistortedStream(idx, mtx, dist, mapx_persp_32, mapy_persp_32)