print("this is var argumetn test ")
def addSeris(*ar):
    res =0
    for i in ar:
        res =res+i
    return res
print("now call ")
result  = addSeris(252,1,522,2,52,22,52,5,25,25,2)    
print(" this is result  = \t %d"%result)
def add(var=200 ,var2=100):
    return var+var2
result =add() # now the result of  add is 300
res = add(4747,43737) #addition of passed arguemtn  
print("resuls is = \t  %d"%result)
print(" the value of res  =  \t  %d"%res)
def keyArg(**ar):
    for listkey in ar.keys():
        print(" this is item passed by keyword arguemtn = \t %s"%str(ar[listkey]))
print(" this si key word argument ")
keyArg(name="jitu",latname="yadav")