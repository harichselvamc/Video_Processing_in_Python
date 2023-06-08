# Load moviepy
from moviepy.editor import VideoFileClip, vfx

# Define clips
clip1 = VideoFileClip("face.mp4")
clip2 = VideoFileClip("face.mp4")

# Apply effects
clip1 = clip1.fx( vfx.colorx, 0.5)
clip2 = clip1.fx( vfx.fadeoutx, 0.5)
clip2 = clip1.fx( vfx.fadeinx, 0.5)
clip2 = clip1.fx( vfx.mirror_y)
clip2 = clip1.fx( vfx.blackwhite)

# Write output video
clip1.write_videofile("result.mp4")
 
