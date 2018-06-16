count=-1
# this is my contuter 
def listTest(li,item):
    for i in li:
        global count
        count =count+1
        if item == i:
            print(" this is the value of count  = \t  %d"%count)
            print("yes found at location  ")
            break
        else:
            if type(i) is  type(li):
                
                listTest(i,item)
# now function body is end 
list =list()

list=[12,25,152,5,[1454,56,45,45,45,45,5,[75,858,585,5,55,4],8585,39,58,58],7858,69,55,5]
item = int(input("Enter item your want to serch  \t"))
for j in list:
    global count
    count =count+1
    if item == j:
        
        print(" this is the value of count  = \t  %d"%count)
        print("item found ")
        break 
    else:
        if type(j)  is type(list):
            listTest(j,item)
