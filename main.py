import sys
from src import pose_estimation
from src import obj_detection

if len(sys.argv) < 2:
    print("Usage: python main.py <video_file>")
    sys.exit()

video_file = sys.argv[1]

# Perform object detection on golf club
obj_detection.apply_obj_detection(video_file)

# Perform pose estimation on edited video
pose_estimation.apply_pose_estimation(video_file)

# Save and output final video