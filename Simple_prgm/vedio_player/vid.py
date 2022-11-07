import cv2 
cap=cv2.VideoCapture("vl.mkv")
while (cap.isOpened()):
    ret,frame =cap.read()

    cv2.imshow("video",frame)
  
    if cv2.waitKey(1) & 0xFF==ord('d'):
        break
cap.release()

cv2.destroyAllWindows()