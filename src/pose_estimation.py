import sys
import cv2 as cv
import mediapipe as mp

def apply_pose_estimation(video_file):
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    cap = cv.VideoCapture(video_file)

    if not cap.isOpened():
        sys.exit("Error: Could not open video file")

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # Convert to RGB and process pose
            frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            results = pose.process(frame_rgb)

            # Render pose on each frame
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(
                    frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0,0,0), thickness=2, circle_radius=1),
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(255,255,255), thickness=2, circle_radius=1))

            cv.imshow('Video', frame)

            # Exit loop if 'q' is pressed
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv.destroyAllWindows()