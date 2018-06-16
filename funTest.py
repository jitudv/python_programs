print(" this  is my function test programm ")
def hello(): # function prototype 
    #body of function 
    print(" hello jitu  call by function ")
print(" now we are call  our writed function ")
hello()
#function call 
print(" now we are again in main  block ")
hello()
hello()
def sinter(p,r,t=3):
    res =((p*r*t)/100)
    print(" this is the interst = \t %d"%res)
    print("and the  data given is  = \t %d \t %d, \t %d"%(p,r,t))
print("this is my sinter calling ")
sinter(20000,10,2)
print("\n\n this is my main block ")
sinter(4000,20,3)
sinter(2000,3)
def empsal(ems ,r=10):
    return ((ems*r)/100)
empsalary = empsal(20000)
print("salary of employee  with tax cutting  = \t %d"%empsalary)
def texcutbyemp(tx):
    print("")