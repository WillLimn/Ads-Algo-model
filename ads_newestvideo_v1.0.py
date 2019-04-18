import json, os, sys
import collections
import datetime


starttime = datetime.datetime.now()




# --- open all files under the directory -------------- ##

#path = "C:/Users/user/Desktop/ads_algo/"
#files = os.listdir(path)
#s =[]
#for file in files:
#    if not os.path.isdir(file): #it's a file, not a directory
#        filename = path+file
#        s.append(filename)
## s is a filename list


filename = "video_desc_upload.json"
# ------ reading json file -------------------------- ##
try:
    with open(filename, "r") as f:
        jf = json.loads(f.read())
except IOError:
    print("Could not read file: ",filename)
    sys.exit()



result_dict = collections.defaultdict(list)
for i in range(4):
    result_dict[jf['video'][i]['video_id']]=jf['video'][i]['upload_time']



# ------ writeing json output file -------------------- ##

with open("newest_video.json","w") as output:
    json.dump(result_dict,output,indent=4)

output.close()


print("The first four newest videos are: ",list(result_dict.items())[:4]) #print the first four newest videos


if os.path.exists("newest_video.json"):
    print("Sucessfully")

else:
    print("Could not create newest_video.json")

endtime = datetime.datetime.now()
print("Running time is :",(endtime-starttime).seconds," sec")

with open("running_time_newsest_log","a") as f:
    sen="Running time of ["+filename+"] to [newest_video.json] is  "+str((endtime-starttime).seconds)+" sec\n"
    f.write(sen)
f.close()
