#!/usr/bin/env python3
import io
from os import PathLike, close, path
import subprocess
from datetime import datetime
from os import listdir, system

system("sudo fan_up.sh")
for filename in listdir("videos/"):
    f = open("log/"+filename+"_LOG.txt", "w")
    res=subprocess.call(
        ['HandBrakeCLI', '--preset-import-file','HB_presets/x264_MKV_1080p30_med_24.json', 
            '-i', "videos/"+filename, '-o', "encoded/"+filename[:-5]+"enc_.mkv"],
        stdout=f, stderr=f)
system("sudo fan_down.sh")