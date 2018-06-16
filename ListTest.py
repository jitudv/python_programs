print(" this  is my list Test py pro")
list = list()
# this is  also empty list 
slist=[]
# this is my empty list 
print(list)
print(slist)
no = int(input("Enter any item you want  to search \t "))
list=[12,25,125,225,52,12,52,520,52,5,5,20,152.25]
print(list)
for i in list:
    if i == no:
        print("yes found ")
        break
    if type(list) is type(i):
        for m in i:
            if m == no:
                print(" yes fond no  in inner list ")
                break


print(" now we are at 0 ident ")
print(" this  is the type of any list = \t %s"%type(list))
print(" this  is the type of any list = \t %s"%type(slist))
if(type(list) is  type(slist)):
    print("yes both are list ")
else:
    print("both are not list")
item = int(input("Entet item for insert  \t "))
list.insert(2,item)
print(list)
list.sort()
print(list)
namlist=["jitu","amit","rajesh","vikash","viren"]
namlist.sort()
print(namlist)
nolist =[454,45,12,4551,42,4815,82,1,521,8,151]
list.append(nolist)
print(list)
list.remove(5)
print(list)
print(" this  is list count = \t  %d"%list.count(125))
print(" no of items  =  \t  %d"%len(list))
#slicing 
sliceTest = list[2:10]
for  k in sliceTest:
    print(k)
print("now are  ate 0 ident")
minslice = list[-10:-2]
for  n in minslice:
    print(n)
print(" we are  ate  0 indent ")