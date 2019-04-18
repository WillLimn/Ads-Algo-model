import json, os, sys
from sklearn import preprocessing
from collections import defaultdict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, date
import logging

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


filename = "video_desc_time.json"
try:
    with open(filename, "r") as f:
        jf = json.loads(f.read())
except IOError:
    print("Could not read file: ",filename)
    sys.exit()

watching_array=[]# watching time array
like=[]
visit=[]
video_item_len = len(jf['video']) # how many video in this json
for i in range(len(jf['video'])):
    watching_array.append([jf['video'][i]['watching_time']])
    like.append(jf['video'][i]['like'])
    visit.append(jf['video'][i]['like'])
watch_np_array=np.array(watching_array)  # convert to np array
watch_np_y = np.linspace(1,video_item_len,video_item_len) # y-label
f.close()


# --- Show watching time plot ---------------------  ##

#plt.scatter(watch_np_array, watch_np_y,alpha=.5)
#plt.xlabel("Watching time (s)")
#plt.ylabel("Items")
#plt.show()


# ---- normalize watching time ---------------------- ##

watch_np_array_normalized = preprocessing.normalize(watch_np_array, norm="l2")


# ---- counting weight ------------------------------ ##


weight = []
dic = defaultdict(list)
for i in range(len(visit)):
    weight.append(visit[i]+like[i]+watch_np_array[i][0]/1000) # the weight formula
    dic[jf['video'][i]['video_id']].append(visit[i]+like[i]+watch_np_array[i][0]/1000) # create unordered dict 

order_dic=defaultdict(list)
for key, value in sorted(dic.items(), key=lambda item: item[1], reverse=True):  # create order dict by value
    order_dic[key]=value
print("The first four hottest videos are: ",list(order_dic.items())[:4]) #print the first four hottest videos


# ------ writeing json output file -------------------- ##

with open("hottest_video.json","w") as output:
    json.dump(order_dic,output,indent=4)

output.close()


if os.path.exists("hottest_video.json"):
    print("Sucessfully")
else:
    print("Could not create hottest_video.json")

endtime = datetime.now()
print("Running time is :",(endtime-starttime).seconds," sec")

with open("running_time_hottest_log.txt","a") as f:
    sen="Running time of ["+filename+"] to [hottest_video.json] is  "+str((endtime-starttime).seconds)+" sec\n"
    f.write(sen)
f.close()

print("Hello World")
