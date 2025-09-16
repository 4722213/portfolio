#import numpy as np
import cv2
#サポートパッチのインポート
from google.colab.patches import cv2_imshow

img = cv2.imread('namakemono.jpg')

cv2.circle(img, (178, 110), 50, (0, 0, 255), thickness = 5)
cv2.arrowedLine(img, (120, 210), (140, 160), (0, 0, 0), thickness = 5)
#.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'sleeping', (50, 240), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), thickness = 2)

cv2_imshow(img)
