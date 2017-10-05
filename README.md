# PyCalibration
This repository provides a Python translation of the undistortFunctions that are part of the Scaramuzza's OCamCalib for fisheye cameras. It contains sample code for comparing this Toolbox to the builtin OpenCV fisheye library.
This repo's objective is providing sample code for calibrating a fisheye camera with two different methods. The code regarding the OCamLib is only a translation and adaptation from C++ to Python. 

Information about the OpenCV calibration procedure for fisheye camera can be found at: http://docs.opencv.org/3.0-beta/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html
Information about the OCamCalib calibration procedure for fisheye camera can be found at: https://sites.google.com/site/scarabotix/ocamcalib-toolbox

----------------------
-----INSTRUCTIONS-----
----------------------

1. Run opencv_calibration.py to extract (and save to a .dat file) the camera calibration parameters using opencv, and save the images for doing the same with the OCamLib Matlab Toolbox.

2. Use the images saved in the previous step to obtain (and save to a .txt file through the export data option) the camera calibration parameters with the OCamLib Matlab Toolbox.

3. Run comparison.py to load the files generated in the previous steps to show a parallel view of the results obtained with the calibration and undistortion methods of OpenCV and OCamLib.