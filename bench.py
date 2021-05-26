#!/usr/bin/env python3
import platform
import os
import subprocess
import time
import exiftool

# we only read from this folder
INPUT_FOLDER="videos/"

# if you do a lot of write operation you may wanto to use an hard disk,
# in order to preserve your SSD TBW
# OUTPUT_FOLDER="/run/media/yuri/Dati/hw_bench/"
OUTPUT_FOLDER="./output/"

def main():
    current_platform = platform.system()
    handbrake_path = "HandBrakeCLI"

    if(current_platform == "Windows"):
        print("You are on Windows")
    elif(current_platform == "Linux"):
        print("You are on Linux")
        print("Turning fans on...")
        #os.system("sudo fan_up.sh")

    input_metadata_array =  []
    output_metadata_array =  []
    times = []

    for i, filename in enumerate(os.listdir(INPUT_FOLDER)):

        input_path = INPUT_FOLDER + filename
        output_path = OUTPUT_FOLDER + filename[:-5] + "enc1_.mkv"

        f = open(OUTPUT_FOLDER + "log/"+filename[:-5] + ".log", "w+")
        # TODO: tweak verbosity level
        print("Processing file " + str(i + 1) + "/" + str(len(os.listdir(INPUT_FOLDER))) + " : " + filename)

        t0 = time.time()

        res=subprocess.call(
        [ handbrake_path , '--preset-import-file','HB_presets/swdef.json', 
                '-i', input_path, '-o', output_path]
                # important log messages are in stderr, we can throw away stdout
                ,stderr=f, stdout=subprocess.DEVNULL)

        t1 = time.time()
        f.close()

        delta = t1 - t0
        print("Time elapsed: " + str(delta))
        times.append(delta)

            # (video duration, time needed, starting dimension, ending dimension, avg framerate)
        # in csv or json format
        with exiftool.ExifTool() as et:
                input_metadata_array.append(et.get_metadata(input_path))
                output_metadata_array.append(et.get_metadata(output_path))

    if(current_platform == "Linux"):
        print("Shutting fans down...")
        #os.system("sudo fan_down.sh")


if __name__ == "__main__":
    main()