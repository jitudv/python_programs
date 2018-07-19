import os
import sys 
import io
print("this  os test pro ")
file = None
path = None
try:
    #dirname = str(input("enter directory name \t "))
    path = "/home/jays/Desktop/Abhishek/amitansh"
    #print(path)
    #os.mkdir(path,777)
    if os.path.isdir(path):
        print("yes it is directry ")
    else:
        print("no its not directory ")
    os.chdir(path)
    print("current working directory  %s"%os.getcwd())
    path =os.getcwd()+"/amit.txt";
    file = open(path,'w')
    if file != None:
        print("yes your file is created success fully ")
    else:
        print("your file does not created because already created")
    #os.remove(path)
    #print("your file is  removed ok ")
    os.rename(path,"rajesh.txt")
    print(path)
    
except IOError as errr:
    print(errr)
finally:
    try:
        pass
    except IOError as err:
        print(err)
print(" yes we are done every thing ")

