import io
import sys
import os
mdata = """ hii this  amit yadav
and jitu is python developer  now  we are 
working on  a java project after some time jitu 
will meet your at bhanwarkua   """
bytedata = mdata.encode("utf-16") 
# this is conversion of string to byte
print(bytedata)


file = None
try:
    file = open("/home/jays/Desktop/Abhishek/jitu.txt",'wb')
    if file != None:
        print("you have file for write  \t ")
        #data = str(input(" enter date for file write "))
        #file.write(data)
        file.write(bytedata)
        print("your file right is completed ")
except IOError as err:
    print(" this is exception \t %s "%(err))
finally:
    try:
        file.flush()
        file.close()
    except IOError as er:
        print("this is   = er = \t %s"%(er))
print("my program is completed ")
     