print(" this is my for programm ")
list =[2,2,252525,256252,24245,22,4224522422,452252425,"jitu ","amit"]
print("len of  list  = \t %d"%len(list))
for i in list:
    print(i)
    print(type(i)) 
print(" now we are  at 0 ident ")

for j in range(23):
    print(j)
print("now we are re 0 ")

no = int(input("Enter no  you want to  get table \t "))
for k in range(1,11):
    print("%d"%((k*no)))

for m in range(1,11):
    print(" roor of  %d and root =\t %d"%(m,(m**2)),end="")
    print("")
print("now  we are in  main block ")