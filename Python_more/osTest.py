import os
import sys
print("platform is  = \t %s"%(sys.platform))
print("version is  = \t %s"%(sys.version))
dirname = str(input("Enter directory name "))
path = "/home/jays/Desktop/"+dirname
try:
    if os.mkdir(path,777):
        print("yes created")
    else:
        print("not created")
except Exception as e:
    print(e)
finally:
    print("this is exception ")
print("we are at end ")
