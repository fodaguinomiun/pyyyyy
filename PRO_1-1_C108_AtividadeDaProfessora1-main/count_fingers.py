import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()

    cv2.imshow("controlador", image)

    key = cv2.waitKey(1)
    if key == 32: 
        break

cv2.destroyAllWindows()

