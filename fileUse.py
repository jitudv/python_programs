import io 
import os 
import sys
f =open("/home/jays/Desktop/python_programms/dictTest1.py","r")
try:
    
    line=f.readlines()
    #clarprint(line)
    l= f.readlines(2)
    print(l)
except:
    print("error occured")
finally:
    f.close()
print('yes file read is working ')