import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os, sys, logging, datetime, json
from sklearn import preprocessing

starttime = datetime.now()

log_filename = datetime.now().strftime("log\%Y%m%d-%H%M%S.log")

logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%m-%d %H:%M:%S',
            filename=log_filename)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


filename = "user_desc_time.json"
try:
    with open(filename, "r") as f:
        jf = json.loads(f.read())
except IOError:
    print("Could not read file: ",filename)
    sys.exit()











endtime = datetime.now()
print("Running time is :",(endtime-starttime).seconds," sec")

with open("running_time_usertailor_log.txt","a") as f:
    sen="Running time of ["+filename+"] to [usertailor_video.json] is  "+str((endtime-starttime).seconds)+" sec\n"
    f.write(sen)
f.close()
