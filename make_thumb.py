#! /usr/bin/env python
# -*- coding: utf-8 -*-import os
import os
import sys
from moviepy.editor import VideoFileClip

def main() :
    if (len(sys.argv)<4) :
        print("Error argument "+str(len(sys.argv)))
    else :
        #print(sys.argv[1])
        #print(sys.argv[2])
        #print(sys.argv[3])
        video_path = os.path.join(sys.argv[1], sys.argv[2])
        image_path = os.path.join(sys.argv[1], sys.argv[3], sys.argv[2] + ".png")
        dir_thumb = os.path.join(sys.argv[1], sys.argv[3])
        if (not os.path.isdir(dir_thumb)) :
            os.mkdir(dir_thumb) 
        print(video_path) 
        print(image_path) 
        clip1 = VideoFileClip(video_path)
        clip1.save_frame(image_path, t = clip1.duration / 2)
    
if __name__ == "__main__":
    main()    