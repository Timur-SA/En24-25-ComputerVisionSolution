import cv2

cap=cv2.VideoCapture(0)

def findC():
    #вместо названия цветов, названия предметов

    def nothing(x):
        pass

    cv2.namedWindow('result')

    cv2.createTrackbar('minh', 'result', 0, 255, nothing)
    cv2.createTrackbar('mins', 'result', 0, 255, nothing)
    cv2.createTrackbar('minv', 'result', 0, 255, nothing)

    cv2.createTrackbar('maxh', 'result', 0, 255, nothing)
    cv2.createTrackbar('maxs', 'result', 0, 255, nothing)
    cv2.createTrackbar('maxv', 'result', 0, 255, nothing)
    #создание ползунков

    while(True):
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('hsv', hsv)

        minh = cv2.getTrackbarPos('minh', 'result')
        mins = cv2.getTrackbarPos('mins', 'result')
        minv = cv2.getTrackbarPos('minv', 'result')

        maxh = cv2.getTrackbarPos('maxh', 'result')
        maxs = cv2.getTrackbarPos('maxs', 'result')
        maxv = cv2.getTrackbarPos('maxv', 'result')
        #сбор инфы с ползунков

        mask = cv2.inRange(hsv, (minh, mins, minv), (maxh, maxs, maxv))
        cv2.imshow('mask', mask)
            
        result = cv2.bitwise_and(frame, frame, mask = mask)
        cv2.imshow('result', result)

        if cv2.waitKey(1) == 27:
            break
#вывод значений

findC()
    
cap.release()
cv2.destroyAllWindows()
        
