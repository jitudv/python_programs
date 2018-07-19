import io
import os
import sys
import pickle
dname = str(input("Enter name for dir \t "))
path  ="/home/jays/Desktop/"+dname
os.mkdir(path,777)
print("current working directory  = \t %s"%(os.getcwd()))
try:
    filename = str(input("Eneter filename "))
    file = open(path+"/"+filename,"w")
    if file != None:
        print("yes file created enter data for file write  ")
        data =sys.__stdin__.readline()
        file.write(data)
    else:
        print("file not created ")
except IOError as err:
    print(err)
finally:
    try:
        file.close()
    except IOError as ierr:
        print(ierr)
print("we are  at 0 ident ")


