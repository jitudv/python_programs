print(" this  is while loop Test programm ")
no =0
while no <=10:
    print(no)
    no =no+1 # increment  in python 
print("now   we are  in main block ")
innercount =0
outercount =0
k=j=0 # multipule assingment 
while k <5:
    while j<5:
        innercount =innercount+1
        j=j+1
    outercount =outercount+1
    k=k+1
print(" this is the value  of  outercount  = \t  %d"%outercount)
print("this is my innercount   =  \t  %d"%innercount)
while True: # this is infinite while loop 
    print("this is infinate ")
print(" we are at last ")