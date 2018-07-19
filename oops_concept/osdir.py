import os
import sys 
import io
print("this  os test pro ")
file = None
path = None
try:
    dirname = str(input("enter directory name \t "))
    path = "/home/jays/Desktop/Abhishek/"+dirname
    print(path)
    os.mkdir(path,777)

except IOError as errr:
    print(errr)
finally:
    try:
        pass
    except IOError as err:
        print(err)

