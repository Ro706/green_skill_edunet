import cv2

img1 = cv2.imread('img/original_image.png')
img2 = cv2.imread('img/image.png')

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))  # Resize img2 to match img1 dimensions
blended = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)  # Blend the images
cv2.imshow('Blended Image', blended)
cv2.waitKey(0)
cv2.destroyAllWindows()