# how to read an image
import cv2
# read the image
image = cv2.imread('img/original_image.png')
# check if the image was loaded successfully
cv2.imshow('original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# save the image to a file
cv2.imwrite('img/new_image.png', gray)
cv2.imshow('GrayScale Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# canny edge detection
edges = cv2.Canny(gray, 100, 200)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()