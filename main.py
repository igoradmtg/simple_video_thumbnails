#! /usr/bin/env python
# -*- coding: utf-8 -*-import os
import os
import hashlib
path = 'z:/upl1' # Dir name Videos
path_thumb = 'thumb' # Subdir thumbs
python_scrypt = 'python make_thumb.py ' # Windows

def main(): 
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            
            if ('.mp4' in file) or ('.mpg' in file) or ('.avi' in file) or ('.wmv' in file) or ('.webm' in file)  or ('.mkv' in file):
                files.append([os.path.join(r, file) , file])
    for fileinfo in files:
        fname = fileinfo[0]
        bname = fileinfo[1]
        str_exec = python_scrypt + "\"" + path + "\" \"" +bname+ "\" \"" + path_thumb + "\"" # form a string for execution - формируем строку для выполнения
        print("Execute ",str_exec) # Displaying - Выводим на экран
        os.system(str_exec) # Run the script for execution - Запускаем скрипт на выполнение
    
if __name__ == "__main__":
    main()    