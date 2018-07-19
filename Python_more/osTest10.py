import sys 
import os 
import os.path
print("this is  sysTest10 ")
curdir = os.getcwd()
# it will return curent workint directory
print(" this is current directory  = \t %s"%(curdir))
pardi = os.pardir
# parent directory of  working  directory 
relpath ="\n c:\\usar\\jays\\text"
curdir =str( os.chdir(os.path.pardir))
print("type of  curdir = \t  %s"%type(curdir))
print("this is current directory   = \t %s"%(os.getcwd()))
print("absolute path of  \t  %s"%(os.path.abspath(relpath)))
print("this is my parrent directory = \t  %s"%(pardi))
if  os.path.isdir("/home/jays/Desktop/Abhishek/jitu.txt"):
    print("yes it is directory ")
elif os.path.isfile("/home/jays/Desktop/Abhishek/jitu.txt"):
    print("yes it is file ")
else:
    print("both are wrong ")
print("path seprator  = \t %s"%(os.path.sep))
os.mkdir(os.getcwd()+os.path.sep+"Python_more"+os.path.sep+"Temp22",777)
print(" your directory is created ")
os.chmod(os.getcwd()+"/Python_more/Temp",777)
print("permission granted ")