"this  is my main method test program "
import sys
print("this is my show program ")
var =0
def show(var):
    print("hello")
    var =var+1
    if(var <10):
        show(var)
#show(0)       
def main():
    show(0)
    print("%s"%__doc__)
    
    __doc__
show(2)
def TesPro():
    global var 
    print("value of global  befor use = \t %d"%var)
    var =var+1
    print("the value of  global var  after changes  \t %d"%var)
TesPro()
print("this is my first argument   = \t %s  "%sys.argv[1])
print("this  is my second argument   =\t %s"%sys.argv[2])
print(" this is my script name   = \t %s"%sys.argv[0])
print("this is my show functio")
print("after show ")
if __name__ =='main':
    print("this is my main pro ")
    
    main()


