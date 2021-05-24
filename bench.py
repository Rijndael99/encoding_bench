#!/usr/bin/env python3
import io
# from os import PathLike, close, path
import os
import subprocess
from datetime import datetime
import exiftool
# from os import listdir, system

# if you do a lot of write operation you may wanto to use an hard disk,
# in order to preserve your SSD TBW
output_folder="/run/media/yuri/Dati/hw_bench/"

# we only read from this folder
input_folder="videos/"
#TODO: add check for operating system
#os.system("sudo fan_up.sh")
for filename in os.listdir(input_folder):
    f = open(output_folder+"log/"+filename[:-5]+".log", "w")
    # TODO: tweak verbosity level
    res=subprocess.call(
       ['HandBrakeCLI', '--preset-import-file','HB_presets/swdef.json', 
            '-i', input_folder+filename, '-o',output_folder+filename[:-5]+"enc1_.mkv"]
            # important log messages are in stderr, we can throw away stdout
            ,stderr=f, stdout=subprocess.DEVNULL)
    f.close()
    # TODO collect stats 
    #       (video duration, time needed, starting dimension, ending dimension, avg framerate)
    #       in csv or json format
    # TODO retrieve size using exiftool
    # os.path.getsize
    metadata = exiftool.ExifTool().get_metadata(filename)
    print("framerate="+metadata['Framerate'])
    print("framerate="+metadata['Dimensione'])
#os.system("sudo fan_down.sh")