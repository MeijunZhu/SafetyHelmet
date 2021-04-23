import time
import requests
import uuid
import os
import sys
import re
import commands
import datetime
import threading
import subprocess




def startWatch(m,s):
    timeLeft=60*m+s
    while timeLeft>0:
        time.sleep(1)
        timeLeft-=1
    playvoice()






def playvoice():
    os.system('omxplayer -o local jinbao.mp3')
       

def threadsingle():
    t1=threading.Thread(target=playvoice)
    t1.start()


def cameraphotos():
    t0=time.time()
    node=uuid.getnode()
    mac=uuid.UUID(int=node).hex[-12:]
    a=commands.getoutput("fswebcam --no-banner -r 640x480 "+mac+".jpg")
    print(a)
    #print(a)
    path=r'/home/pi/'+mac+'.jpg'
    
    if os.path.exists(path):
        url = "http://10.186.162.179:8080/test/"
        path_file0="/home/pi/"+mac+".jpg"
        files = {'file0':open(path_file0,'rb')}
        result = requests.post(url=url,files=files)
        existstr="no_helmet" in result.text
        if existstr:
            threadsingle()
        print('Done. (%.3fs)' % (time.time()-t0))
        






startWatch(0,30)
    
#ath1=cameraphotos() 

while 1:
    cameraphotos() 
    #path1=cameraphotos()
    #if str(path1)=="True":
     #   os.system('omxplayer -o local jinbao.mp3')
    #print(str(path1))
    #time.sleep(2)
    
    #print(result1)

# driver.find_element_by_id(".upload-pic").send_keys(path)