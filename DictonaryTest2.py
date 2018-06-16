print("this  is my dictonary test programm")
dict  = dict()
list =list()
# this is my emtpy list 
# this is my empty dictonary 
dict={
    "name":"jitu",
    "lastname ":"yadav",
    "salary":252525,
    "address":"khargeone",
    "mob_no":[7566447017,252,525,235252]
}
empname = dict["name"]
print("this is the name of emp  = \t %s"%str(empname))
for liskey  in dict.keys():
    if type(list) is type(dict[liskey]):
        for j in dict[liskey]:
            print(j)
    print(" key  = \t  %s and  value =- \t  %s "%(liskey ,str(dict[liskey]))) 
print("now we are at  0 ident ")
if dict.has_key("email"):
    print("yes we have ")
else:
    print("we dont have ")