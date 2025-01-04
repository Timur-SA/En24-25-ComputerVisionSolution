import cv2 as cv

class CaptureImage:
    def CamError(self):
        raise RuntimeWarning("Camera")
    
    def __init__(self):
        self.cam = cv.VideoCapture(1)
        #self.cam.release() #???

    def GetImage(self):
        isCaptured, self.srcImg = self.cam.read()
        
        if(not isCaptured):
            self.CamError()

        self.mainImg = cv.cvtColor(self.srcImg, cv.COLOR_RGB2HSV)
        #Обработка изображения
        return self.mainImg

if __name__ == "__main__":
    ci = CaptureImage()
    img = ci.GetImage()

    print(ci)
    print(img)
    input()




# Постобработка Image
# def ImageProcess(sorceImage):
#     brightness = -10
#     contrast = 1.2

#     sorceImage = cv.cvtColor(sorceImage, cv.COLOR_RGB2HSV)  
#     return cv.addWeighted(sorceImage, contrast, 0, brightness, 0) 


# def CameraTest():
#     while True:
#         ret, image = camera.read() # Читаем камеру
        
#         if not ret:
#             print("ОШИБКА: Камера не распознана")
#             break

#         cv.imshow("CameraTest", image)

#         cv.waitKey(0)

# def CameraCapture():
#     ret, image = camera.read()
#     if not ret:
#         print("ОШИБКА: Камера не распознана.")
#         raise RuntimeWarning("Camera")

#     return ImageProcess(image)