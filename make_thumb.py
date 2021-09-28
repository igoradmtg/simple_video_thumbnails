#! /usr/bin/env python
# -*- coding: utf-8 -*-import os
import os
import sys
from moviepy.editor import VideoFileClip

def main() :
    if (len(sys.argv)<3) :
        print("Error argument "+str(len(sys.argv)))
        print("Use:")
        print("make_thumb.py dir_name file_name_video [thumb_dir]")
        print(" dir_name ")
        print(" file_name_video ")
        print(" thumb_dir ")
    else :
        #print(sys.argv[1])
        #print(sys.argv[2])
        #print(sys.argv[3])
        video_path = os.path.join(sys.argv[1], sys.argv[2])
        if (not os.path.isfile(video_path)) :
            print("Not found file")
            sys.exit(0)
        if len(sys.argv)>=4:
            image_path = os.path.join(sys.argv[1], sys.argv[3], sys.argv[2] + ".png")
            dir_thumb = os.path.join(sys.argv[1], sys.argv[3])
            if (not os.path.isdir(dir_thumb)) :
                os.mkdir(dir_thumb) 
        else:
            image_path = os.path.join(sys.argv[1], sys.argv[2] + ".png")
        if os.path.isfile(image_path):
            print("File exists:",image_path)
            return False
        print("Video: " + video_path) 
        print("Image: " + image_path) 
        clip1 = VideoFileClip(video_path)
        clip1.save_frame(image_path, t = clip1.duration / 2)
    
if __name__ == "__main__":
    main()    