import sys
import os
import getpass
import getopt 
print(" max recursion limit  =\t %d"%sys.getrecursionlimit())
print("function type = \t  %s"%type(sys.getrecursionlimit))
sys.setrecursionlimit(2000)
print(" max recursion limit  =\t %d"%sys.getrecursionlimit())
no = int(sys.argv[1])
no1 = int(sys.argv[2])
print("addtion of the command line argument  = \t %d "%((no+no1)))
print("max limit of int  = \t  %d"%(sys.maxint))
print("write for data ")
data = sys.__stdin__.readline()
sys.__stdout__.write(data)
sys.__stderr__.write(" this my eroor Stream  \n ")
print("currunt user  %s "%(str(getpass.getuser())))
print("Enter password ")
passdata = getpass.getpass()
print(passdata)
print(sys.path)