
import threading
print("this is multiThreading task ")
def task():
    for i in range(5):
        print("hello  \t  %d"%(i))
t1 =  threading.Thread(target=task,name="first")
t1.start()
t1.join()
print("now we are at end ")