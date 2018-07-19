import io
import os
import sys
import pickle
f = None
try:
    f  = open("/home/jays/Desktop/python_programms/Python_more/AAA.txt","w")
    print("name of file = \t %s"%f.name)
    #print(" file no   = \t  %d"% int(f.no))
    if f != None:
        print("your file is created or exist ")
    else:
        print("your file  does not created ")
except IOError as err:
    print(err)
finally:
    try:
        f.close()
        print(" \n yes f stream is closed ")
    except IOError as er:
        print(er)
print(" \n \n  now we are at last ")
