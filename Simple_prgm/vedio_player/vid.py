<<<<<<< HEAD
import cv2 
cap=cv2.VideoCapture("vl.mkv")
while (cap.isOpened()):
    ret,frame =cap.read()

    cv2.imshow("video",frame)
  
    if cv2.waitKey(1) & 0xFF==ord('d'):
        break
cap.release()

=======
import cv2 
cap=cv2.VideoCapture("vl.mkv")
while (cap.isOpened()):
    ret,frame =cap.read()

    cv2.imshow("video",frame)
  
    if cv2.waitKey(1) & 0xFF==ord('d'):
        break
cap.release()

>>>>>>> a15de333f5cb5d803fb18660f02ece1595789616
cv2.destroyAllWindows()