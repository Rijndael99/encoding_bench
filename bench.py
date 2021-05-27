#!/usr/bin/env python3
import platform
import os
import subprocess
import time
import exiftool
import json

# we only read from this folder
INPUT_FOLDER="videos/"

# if you do a lot of write operation you may wanto to use an hard disk,
# in order to preserve your SSD TBW
# OUTPUT_FOLDER="/run/media/yuri/Dati/hw_bench/"
OUTPUT_FOLDER="./output/"

encoding = "SW" # CHANGE ACCORDINGLY

def main():
    current_platform = platform.system()
    handbrake_path = "HandBrakeCLI"

    if(current_platform == "Windows"):
        print("You are on Windows")
    elif(current_platform == "Linux"):
        print("You are on Linux")
        print("Turning fans on...")
        #os.system("sudo fan_up.sh")

    times = []

    for i, filename in enumerate(os.listdir(INPUT_FOLDER)):

        input_path = INPUT_FOLDER + filename
        output_path = OUTPUT_FOLDER + filename[:-5]

        metadata_filename = filename[:-5]


        encoding_check = ((encoding == "SW") | (encoding == "HW"))
        assert encoding_check, "Error: unknow encoding. Make sure you initialized the variable 'encoding' correctly."
        
        if(encoding == "SW"):
            output_path += "enc1.mkv"
            f = open(OUTPUT_FOLDER + "log/"+filename[:-5] + "enc1.log", "w+")
            metadata_filename +=  "1.json"

        elif(encoding == "HW"):
            output_path += "enc2.mkv"
            f = open(OUTPUT_FOLDER + "log/"+filename[:-5] + "enc2.log", "w+")
            metadata_filename +=  "2.json"

        # TODO: tweak verbosity level
        print("Processing file " + str(i + 1) + "/" + str(len(os.listdir(INPUT_FOLDER))) + " : " + filename)

        t0 = time.time()

        res=subprocess.call(
        [ handbrake_path , '--preset-import-file','HB_presets/hwdef.json', 
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
                metadata = et.get_metadata(output_path)

                with open(OUTPUT_FOLDER + "metadata/" + metadata_filename, "w") as outfile:
                    json.dump(metadata, outfile)

    if(current_platform == "Linux"):
        print("Shutting fans down...")
        #os.system("sudo fan_down.sh")


if __name__ == "__main__":
    main()