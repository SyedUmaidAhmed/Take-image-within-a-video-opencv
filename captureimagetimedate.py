import cv2
import numpy as np
from datetime import datetime

camera = cv2.VideoCapture(0)
i = 0
while True:
    ret, image = camera.read()
    cv2.imshow('Capturing', image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss') + '.jpg', image)
        break

camera.release()
cv2.destroyAllWindows()

