import cv2
import numpy as np

image = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.line(image, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.rectangle(image, (100, 100), (400, 400), (0, 255, 0), 3)
cv2.circle(image, (256,256), 100, (0, 0, 255), -1)
cv2.putText(image, 'Ro706', (156, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
cv2.imshow('Drawing Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()