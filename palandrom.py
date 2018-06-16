print(" this is pallendrom no  ")
no = int(input("Enter any no   \t "))
res =0
temp =no
while(no >0):
    res =res*10
    res =res+(no%10)
    no =no/10
print(" now  we are  out of loop  ")
print("res = \t  %d"%res)
print("the value  of   no = \t  %d"%no)
if( temp== res):
    print("yes no is palandrom  ")
else:
    print("no no is not palandrom ")