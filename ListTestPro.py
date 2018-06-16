print(" this  is list Test  program ")
list  =list() # empty list created 
m =list
print("id of m  \t  %d"%id(m))
print(" id of  list = \t  %d"%id(list))
print(list)
list=[152,252,526,25,2252,4525,252,52,52,525,[1541,25,1254,14,2151,2,512,1]]
print(list)
for i in list:
    print(i)
    
    if type(i) is type(list):
        for j in i:
            #print("yes list found ")
            print(j)
print("operation complited ")
list.insert(1,250)
print(list)
list.remove(152)
print(list)
item = int(input("Enter item your want to  serch "))
count =0
for  k in list:
     if k == item:
         print("yes found item  at location ")
         break
     if type(k) is type(list):
        for n in k:
            if item == n:
                print(" out item found at innser list  ")
                break
     count =count+1
print(" this is my  main block ")

 