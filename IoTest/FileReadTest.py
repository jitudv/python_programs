import io
import os
import sys
file  = None #  this is global context 
try: 
    # start try block 
    file = open("/home/jays/Desktop/Abhishek/jitu.txt","r")
    # this is initializtion of  file 
    data =file.read(100) # data read with byte limit 
    print("this is my file data  = \t %s "%(data))

except IOError  as  er :
    print(er)
finally:
    try:
        file.close() # now file stream closed 
        if file.closed: # to ensure 
            print("yes closed ")
        else:
            print("does not closed ")
    except IOError as ier :
        print(ier)
print("this my file read programm ")



