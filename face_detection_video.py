import cv2

cap = cv2.VideoCapture(0)  # Use 0 for the default camera
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
def detect_faces(frame):
    video_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
    if video_gray is None:
        print("Error: Could not convert frame to grayscale.")
        return frame
    # Detect faces  
    faces = face_cascade.detectMultiScale(video_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces: 
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return frame

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    frame_with_faces = detect_faces(frame)
    cv2.imshow('webcam Live', frame_with_faces)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()