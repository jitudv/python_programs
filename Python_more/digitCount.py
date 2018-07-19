print("this is my digit count programm ")
res =0
rem =0
no = int(input("Enter any no \t "))
while no !=0:
    rem =no%10 # to get last degit of no 
    res =res +rem # this is for digit addtion 
    no =no//10 # to remove last digit from  no 
print("this is the  result of gigit count \t %d"%res)