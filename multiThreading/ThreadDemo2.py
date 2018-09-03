import threading 
import os 
import time

def showInfo():
    print("get current thread id = \t  %d"%threading.get_ident())

def  showThread():
    showInfo()
    for i in range(5):
        #time.sleep(10)
        if(i ==3 ):
            #os.wait()
            pass
        print("current Thread name = \t  %s"%threading.current_thread.__name__)

print(" now start Thread wrinting ")
t1  = threading.Thread(target=showThread ,name="firstThread")
t2  = threading.Thread(target=showThread,name="secondThread ")
t3  = threading.Thread(target=showThread,name="Third Thread")
t1.start() # start thread for running state 
t2.start()
t3.start()