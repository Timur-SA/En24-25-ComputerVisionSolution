import cv2 as cv
#import numpy as np
import os
from InitConfig import *
from RobotCommunicate import NetControl as nc
from CameraInput import CaptureImage as ci
from ImageProcessing import ImageProcessor as ip
from MovementControl import MovementController as mc

image = ci.GetImage()
lines = ip.findLines(image)
robotPos, robotDir = ip.findRobot(image)
for line in lines:
    mc.MoveToTarget(robotPos, robotDir, list(lines[2], lines[3]))

nc.MoveForward()