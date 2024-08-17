import cv2
import mediapipe as mp
import numpy as np


mp_face_detection = mp.solutions.face_detection
mp_face_detection = mp_face_detection.FaceDetection()

# Capture video 
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    # Convert the BGR frame to RGB
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
            
            # Create an elliptical mask
            mask = np.zeros_like(frame, dtype=np.uint8)

            # Define the center, axes, and angle of the ellipse (oval shape)
            center = (x + w // 2, y + h // 2)
            axes = (w // 2, h // 2)
            angle = 0

            # Draw the filled ellipse on the mask
            cv2.ellipse(mask, center, axes, angle, 0, 360, (255, 255, 255), -1)

            # Apply Gaussian blur to the entire frame
            blurred_frame = cv2.GaussianBlur(frame, (99, 99), 30)

            # Combine the blurred face using the mask
            frame = np.where(mask == 255, blurred_frame, frame)

    # Display the frame with blurred oval faces
    cv2.imshow("Face Blur", frame)
    
    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
