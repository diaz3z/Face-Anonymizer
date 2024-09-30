import cv2
import mediapipe as mp
import numpy as np


mp_face_detection = mp.solutions.face_detection
mp_face_detection = mp_face_detection.FaceDetection()

cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to detect faces
    results = mp_face_detection.process(frame_rgb)

    if results.detections:
        # Loop through all detected faces
        for detection in results.detections:
            # Get the relative bounding box of the face
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            # Convert relative bounding box to absolute pixel values
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            
            # Extract the region of interest (ROI) for the face
            face_roi = frame[y:y+h, x:x+w]

            # Apply Gaussian blur to the face ROI
            blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)

            # Replace the original face region with the blurred face
            frame[y:y+h, x:x+w] = blurred_face

    # Display the frame with blurred rectangular faces
    cv2.imshow("Mediapipe", frame)
    
    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
