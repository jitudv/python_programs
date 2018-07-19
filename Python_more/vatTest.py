
import sys
import os
import re
""" 
this is a simple module for variable testing 
and just used to show  id and type concept
"""
var  =90 # id allocate for 90 15784080
print(" this is id of var %d"%id(var))
print("this is type of var  %s"%type(var))
var ="jitu"
# var again initilize  

print(" this is id of var %d"%id(var))
print("this is type of var  %s"%type(var))

no =90 # now id should be same to  var 15784080 
print(" this  is id of no  = \t  %d"%id(no))
print("this is  type of no  = \t  %s"%type(no))
def Hello():
    print("hello")
    print("say hello ")
    if True :
        print("this si inner block ")
        if True:
            print("this is inner most block ")
Hello() # function call at 0 ident 
print("hii this is jitu yadav ")
print(" this is documentation of  module   = \n %s "%__doc__)
print("this is name   = \t  %s"%__name__)
if __name__ == '__main__':
    print("now  this is executable  moduel ")
