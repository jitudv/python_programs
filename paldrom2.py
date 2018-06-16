print(" this is the palandrom 2 py")
no =int(input("Enter any no \t "))
rew =0
i=10
while(True):
    rew=rew*10
    rew=rew+((no%i)/(i/10))
    if((no/i)==0):
        break
    i=i*10
if(rew == no):
    print("palandrom ")
else:
    print(" no is not pallandrom ")    
