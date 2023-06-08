# Load moviepy
from moviepy.editor import VideoFileClip, vfx

# Define clips
clip1 = VideoFileClip("horse.mp4")

# Apply effects
clip1 = clip1.fx( vfx.crop, x1=550, x2=640, y1=200, y2=300)

# Write output video
clip1.write_videofile("result.mp4")
 
