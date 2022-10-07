# %%
import numpy as np
import cv2
cap = cv2.VideoCapture('./g.mp4')
while True:
    ret, frame = cap.read()
    if type(frame) == None:
        break
    frame = frame[0:720,0:1280]
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
# cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
