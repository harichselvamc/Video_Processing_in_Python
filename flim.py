from moviepy.editor import*
# # clip=ColorClip(size=(1908,1080),color=[61,94,16])
# # clip=clip.set_duration(10)
# # clip.fps=120
# # clip.write_videofile("120fps.mp4")

# clip=VideoFileClip("120fps.mp4")
# # #width
# # print(clip.w)
# # #height
# # print(clip.h)
# # #size
# # print(clip.size)
# # #duration
# # print(clip.duration)
# # #frame rate
# # print(clip.fps)


# clip=ImageSequenceClip(['1.jpg','2.jpg','3.jpg'],fps=0.6)

# clip.write_videofile("imagetovideo.mp4")


# video=VideoFileClip("horse.mp4").rotate(90)
# # video.write_videofile("rotate.mp4")
# video.write_gif("videotogif.gif")

# clip=VideoFileClip("horse.mp4")
# clip=clip.subclip(0,3)
# clip.write_gif("subclip.gif")


clip1=VideoFileClip("horse.mp4")
clip2=VideoFileClip("boat.mp4")

result=concatenate_videoclips([clip1,clip2])
result.write_videofile("mergedvideo.mp4")