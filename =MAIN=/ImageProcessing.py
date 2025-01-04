import cv2 as cv
import numpy as np

class ImageProcessor:
    def findLines(self, img):
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        lower_blue = np.array([90, 70, 30])
        upper_blue = np.array([140, 255, 255])
        mask = cv.inRange(hsv, lower_blue, upper_blue)
        edges = cv.Canny(mask, 50, 200)
        lines = cv.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=20, minLineLength=10, maxLineGap=5)
        
        return lines
    def findRobot(self, img):
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        return robotC, robotF 

# class HoughTransform:
#     def hough_lines(self, edges):
#         lines = cv.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=20, minLineLength=10, maxLineGap=5)
#         if lines is not None:
#             return lines
#         return None

# class CannyEdgeDetection:
#     def canny_edge_detection(self, mask):
#         edges = cv.Canny(mask, 50, 200)
#         return edges