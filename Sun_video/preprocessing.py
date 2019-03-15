import robust_cloud
from utilities import _input_,greetings,welcome
from utilities import *
from robust_cloud import Db
def video_read(video,status,path1):
    data=cv2.VideoCapture(video)
    present,image=data.read()
    os.system('cls')
    greetings()
    print("\nGathering images...\n",end='')
    print("Loading...Please wait\t")
    i=0
    j=0
    while present:
        present,image=data.read()
        j +=1
    print("\nStatus Update: {} Frames has been found in your video\n".format(j))
    time.sleep(1)
    print("Dividing Into frames\n")
    time.sleep(1)
    print("ETA:{} seconds\n".format(int((j/23)+5)))
    time.sleep(1)
    pbar=tqdm(total=j)
    data=cv2.VideoCapture(video)
    present,image=data.read()    
    while present: 
        cv2.imwrite(os.path.join(path2,"{}{}.jpg".format(status,i)),image)
        present,image=data.read()    
        i +=1
        pbar.update(1)
    pbar.close()
    print("\nCompleted\n\n\n")
j=str(input("Video of the Sun(Y/N):-"))
if j=='Y' or 'y':
    status='Sun'
    video,path1=_input_()
elif j=='N' or 'n':
    status='No_sun'
    video,path1=_input_()
else:
    print("Invalid Input")
data=robust_cloud.retrieve()
count=data[len(data)-1][1]
count +=1
database=Db(count)
database.store()
os.mkdir(path1+"\\Robust_idno_{}".format(count))
path2=path1+"\\Robust_idno_{}".format(count)
video_read(video,status,path2)
welcome(count,path1)