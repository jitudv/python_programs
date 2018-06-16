print(" this is my digit count ")
res =0
no = int(input("Enter any no  \t "))
rem =0
while(no !=0):
    rem = no%10
    res=res+rem
    no=no/10
print(" this is my addition of digits = \t %d"%res)