import cv2

cap=cv2.VideoCapture(1)

def findC():
    #вместо названия цветов, названия предметов

    def nothing(x):
        pass
    
    ret, frame = cap.read()
    x, y, _ = frame.shape
    print(x)
    print(y)
    cv2.namedWindow('result', cv2.WINDOW_FREERATIO)

    cv2.createTrackbar('H_min', 'result', 0, 255, nothing)
    cv2.createTrackbar('S_min', 'result', 0, 255, nothing)
    cv2.createTrackbar('V_min', 'result', 0, 255, nothing)

    cv2.createTrackbar('H_max', 'result', 0, 255, nothing)
    cv2.createTrackbar('S_max', 'result', 0, 255, nothing)
    cv2.createTrackbar('V_max', 'result', 0, 255, nothing)

    cv2.createTrackbar('Rot', 'result', 0, 3, nothing)

    cv2.createTrackbar('x0', 'result', 0, x, nothing)
    cv2.createTrackbar('y0', 'result', 0, y, nothing)
    cv2.createTrackbar('x1', 'result', 0, x, nothing)
    cv2.createTrackbar('y1', 'result', 0, y, nothing)


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

        rot = cv2.getTrackbarPos('Rot', 'result')

        x0 = cv2.getTrackbarPos('x0', 'result')
        y0 = cv2.getTrackbarPos('y0', 'result')
        x1 = cv2.getTrackbarPos('x1', 'result')
        y1 = cv2.getTrackbarPos('y1', 'result')


        mask = cv2.inRange(hsv, (minh, mins, minv), (maxh, maxs, maxv))
        cv2.imshow('mask', mask)

        for i in range(rot):
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            hsv = cv2.rotate(hsv, cv2.ROTATE_90_CLOCKWISE)
            mask = cv2.rotate(mask, cv2.ROTATE_90_CLOCKWISE)

        if(x0 != x1 and y0 != y1):
            frame = frame[x0:x1, y0:y1]
            hsv = hsv[x0:x1, y0:y1]
            mask = mask[x0:x1, y0:y1]
            
            
        result = cv2.bitwise_and(frame, frame, mask = mask)
        cv2.imshow('result', result)

        if cv2.waitKey(1) == 27:
            break
#вывод значений

findC()
    
cap.release()
cv2.destroyAllWindows()
        
