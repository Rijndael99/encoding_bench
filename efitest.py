#!/usr/bin/env python3
import os
import json
size=os.popen("exiftool bench.py").read()
print(size)
#with open("test.json", "w") as out:
 #   json.dump(met,out )