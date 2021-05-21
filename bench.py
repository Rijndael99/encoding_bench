#!/usr/bin/env python3
import io
# from os import PathLike, close, path
import os
import subprocess
from datetime import datetime
import exiftool
# from os import listdir, system


#TODO: add check for operating system
os.system("sudo fan_up.sh")
for filename in os.listdir("videos/"):
    f = open("log/"+filename+"_LOG.txt", "w")

    # TODO: tweak verbosity level
    res=subprocess.call(
        ['HandBrakeCLI', '--preset-import-file','HB_presets/x264_MKV_1080p30_med_24.json', 
            '-i', "videos/"+filename, '-o', "encoded/"+filename[:-5]+"enc_.mkv"],
        stdout = None, stderr = None)
    # TODO retrieve size using exiftool
    # os.path.getsize
    metadata = exiftool.ExifTool().get_metadata(filename)
    metadata['framerate']
os.system("sudo fan_down.sh")