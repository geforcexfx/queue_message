import queue
import threading
import time
import random
#open a file in read mode
f= open("newfile.txt","r")
#read each line from that file
fl= f.readlines()
#open a file in write mode
ws = open("remote_file.txt","w")
q = queue.Queue()

def sender():
    n = 0
    
    for i in fl:
        n = n+1
        print(n)
        print("Sender: ") 
        print(i)
        #sleep thread for
        time.sleep(random.random())
        #put each line of the content in newfile.txt in queue service
        q.put(i)
    #put end indicator in order to end get queue service from sender
    q.put("/end")
    
def receiver():
    a=q.get()
    while a!="/end":
        print("Receiver: ")    
        print(a)
        time.sleep(random.random())
        #write each line from queue to remote_file.txt
        ws.write(a)
        a=q.get()
    #save the file
    ws.close()
t = threading.Thread(name='sender', target=sender)
w = threading.Thread(name='receiver', target=receiver)

t.start()
w.start()
t.join()
w.join()
