import cv2
import numpy as np

cap = cv2.VideoCapture()

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600,800))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    alt = np.array([18,94,140],np.uint8)
    ust = np.array([98,255,255],np.uint8)

    mask = cv2.inRange(hsv,alt,ust)
    kenar = cv2.Canny(mask,75,250)
    cizgi = cv2.HoughLinesP(kenar,1,np.pi/180,50,maxLineGap=5)

    for i in cizgi:
        x1,y1,x2,y2 = i[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)

    cv2.imshow("a",frame)




    if ret == 0:
        break
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()