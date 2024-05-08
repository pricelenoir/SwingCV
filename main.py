import sys
from src import analyze_swing

if len(sys.argv) < 2:
    print("Usage: python main.py <video_file>")
    sys.exit()

video_file = sys.argv[1]

analyze_swing.apply_pose_estimation(video_file)