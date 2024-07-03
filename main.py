import sys
from src import pose_estimation as pest
from src import instance_segmentation as iseg

if len(sys.argv) < 2:
    print("Usage: python main.py <video_file>")
    sys.exit()

video_file = sys.argv[1]

# Perform instance segmentation on golf club
iseg.apply_instance_segmentation(video_file)

# Perform pose estimation on edited video
#pest.apply_pose_estimation(video_file)

# Save and output final video