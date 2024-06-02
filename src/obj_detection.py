import sys
import cv2 as cv

def apply_obj_detection(video_file):
    cap = cv.VideoCapture(video_file)

    if not cap.isOpened():
        sys.exit("Error: Could not open video file")

    cap.release()
    cv.destroyAllWindows()