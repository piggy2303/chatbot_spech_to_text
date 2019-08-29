# import os, sys

# # Open a file
# path = "./DATA/dong/chat/"
# dirs = os.listdir(path)

# # This would print all the files and directories
# for file in dirs:
#     print(file)

from pydub import AudioSegment

audio = AudioSegment.from_file('./test1.m4a', format='m4a')
