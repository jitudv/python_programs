tuple = tuple()
# this is my empty tuple 
tuple=("jitu","amit","sumit",252,252j,252,12452.252,"indore")
print(tuple)
item =252
for i in  tuple:
    if item == i:
        print(" yes item found ")
        break
  
print(" we are at  0 ")
print(" data  = %s "%str(tuple[3]))
for j in tuple[2:6]:
    print(j)
for k in  tuple[-6:-3]:
    print(k)
print("size  = \t  %d"%len(tuple))