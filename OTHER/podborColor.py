import cv2

cap=cv2.VideoCapture(1)

def findC():
    #вместо названия цветов, названия предметов

    def nothing(x):
        pass

    cv2.namedWindow('result')

    cv2.createTrackbar('H_min', 'result', 0, 255, nothing)
    cv2.createTrackbar('S_min', 'result', 0, 255, nothing)
    cv2.createTrackbar('V_min', 'result', 0, 255, nothing)

    cv2.createTrackbar('H_max', 'result', 0, 255, nothing)
    cv2.createTrackbar('S_max', 'result', 0, 255, nothing)
    cv2.createTrackbar('V_max', 'result', 0, 255, nothing)
    #создание ползунков

    while(True):
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('hsv', hsv)

        minh = cv2.getTrackbarPos('H_min', 'result')
        mins = cv2.getTrackbarPos('S_min', 'result')
        minv = cv2.getTrackbarPos('V_min', 'result')

        maxh = cv2.getTrackbarPos('H_max', 'result')
        maxs = cv2.getTrackbarPos('S_max', 'result')
        maxv = cv2.getTrackbarPos('V_max', 'result')
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
        
