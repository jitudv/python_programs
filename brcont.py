print(" this is break and continue test programm ")
no = int(input("Enter  any nu "))

while(no <100):
    if(no %10 == 0):
        print("yes  its divide by two %d "%no)
        break
        
    print(" no is not divide by  2 ")
    no =no+1
print("now we are  at 0 ident ")

for i in range(10):
    
    if( i == 5  ):
        continue
        print("%d"%i)
    print(" %d "%i)      
print("now we are  out of loop ")
for k in range(12):
    pass
print(" this is pass statement ")
