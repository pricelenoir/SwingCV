import sys
import cv2 as cv
import torch
from ultralytics import YOLO

def apply_instance_segmentation(video_file):
    # Set the path to the YOLO model
    model_path = "model/dataset/results/128_epochs_test/weights/best.pt"
    
    # Load the YOLO model
    model = YOLO(model_path)

    # Open the video file
    cap = cv.VideoCapture(video_file)
    if not cap.isOpened():
        sys.exit("Error: Could not open video file")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        # Process results and draw them on the frame
        for result in results:
            box = result['xyxy']
            mask = result['masks']

            # Draw bounding box
            x1, y1, x2, y2 = map(int, box)
            cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Draw mask
            mask = mask.numpy()
            color = (0, 255, 0)  # Color for the mask
            frame[mask == 1] = color

        # Display the frame
        cv.imshow('YOLO Instance Segmentation', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv.destroyAllWindows()