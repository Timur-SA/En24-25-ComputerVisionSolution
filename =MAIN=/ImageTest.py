from InitConfig import *
from CameraInput import CaptureImage
import cv2 as cv, numpy as np

class ImageTests:
    def __init__(self):
        self.ci = CaptureImage()
        self.img = self.ci.GetImage()

    def TestColor(self, min, max, isHybrid):
        if(not isHybrid):
            return cv.inRange(self.img, min, max)
        else:
            return self.compareImages(self.img, cv.inRange(self.img, min, max))
        
    def compareImages(self, img, mask):
        return cv.bitwise_and(img, mask)
    
    def UpdateImage(self):
        self.img = self.ci.GetImage()
        
        
def main():
    it = ImageTests()

    while True:
        nMin =int(input())
        nMax =int(input())

        if(input() == "q"):
            quit()
        it.UpdateImage()
        cv.imshow("TEST", it.TestColor(min=np.array([nMin, 0, 0]), max=np.array([nMax, 255, 255]), isHybrid=False))
        
        



if(__name__ == "__main__"):
    main()