import cv2 as cv
#import numpy as np
import os
from InitConfig import *
from RobotCommunicate import NetControl
from CameraInput import CaptureImage
from ImageProcessing import ImageProcessor
from MovementControl import MovementController

nc = NetControl()
ci = CaptureImage()
ip = ImageProcessor()
mc = MovementController()


image = ci.GetImage()
lines = ip.findLines(image)
robotPos, robotDir = ip.findRobot(image)
for line in lines:
    command = mc.MoveToTarget(robotPos, robotDir, list(lines[2], lines[3]))
    nc.SendCommand(command)

nc.MoveForward()