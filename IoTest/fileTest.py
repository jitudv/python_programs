import sys
import os
import io
print("this is file Test pro")

try:
    #os.mkdir("jitu" ,777)
    #os.chmod("/jitu",777)
    print(" this is my current location  = \t %s"%str(os.getcwd()))
    f = open(os.getcwd()+"/jitu/jasy.txt" ,'a+')
    if f != None:
        print("yes file is created ")
        data = str(input("enter your text to write in file "))
        f.write(data)
    else:
        print("file does not created ")
    
except:
    print(" this is exceptional errro ")
finally:
    print("this is finnaly block ")
    #os.chmod(os.getcwd()+"/jitu/jasy.txt",777)
    print("yes permission granted to file ")