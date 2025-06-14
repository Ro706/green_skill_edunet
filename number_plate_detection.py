import cv2

# Load the pre-trained Haar Cascade for license plate detection
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

# Load the input image
img = cv2.imread('img/car.jpg')  # Replace with your image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect license plates
plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

# Draw rectangles around detected plates
for (x, y, w, h) in plates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    plate_roi = img[y:y+h, x:x+w]  # Extract the plate region
    cv2.imshow("Plate", plate_roi)

# Show the full image with detected plates
cv2.imshow("License Plate Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()