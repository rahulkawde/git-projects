# import os
# import pydub
# import glob

# mp4_files = glob.glob('downloads/*.mp4') 
# print(mp4_files)

# audio video converter √√
import moviepy.editor as mp

clip = mp.VideoFileClip(r'video/text.mp4')
clip.audio.write_audiofile(r'video/text.mp3')

