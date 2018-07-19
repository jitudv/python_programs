import os
import sys
import io
print(" this os last")
#pid = os.getpid()
#os.kill(pid,1)
pid = os.fork()
if pid >0:
    print("yes sub is created ")
    print("id of new created process = \t  %d"%(pid))
    os.kill(pid,7)
    if pid < 0:
        print("your process hasbean kill ")
        print("process is  after kill  = \t  %d"%(pid))
    else:
        print("your process does not kill ")
else:
    print("sub process is not created ")
print("we are at last ")
print("user id  = \t %d"%(os.getuid()))
print("user id  = \t %d"%(os.getgid()))
list = os.getgroups()
print(list)
list= os.environ.keys()
for l in list:
    print("key is %s \t vlaue is  =\t %s"%(l,os.environ[l]))
print("we are the end ")
# this is the way of envieorment set 

