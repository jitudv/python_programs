import string
print("String Test  process test ")
name ="jitu"
print("id of name befor update  = \t %d"%id(name))
name =name.join("yadav")
print("the value of  name  = \t "+name)
print("id of name after  update  = \t %d"%id(name))
list =["jitu"]
print("id of list  = \t %d"%id(list))
list.append("yadav")
print("id of list  = \t %d"%id(list))
var ="shantnu "
if(var.islower()):
    print("yes it is ")
else:
    print("no it is not ")
var = "123"
if(var.isdigit()):
    print("yes")
else:
    print("no it does not contain any digit ")
for i in string.ascii_uppercase:
    print(" %s ascki of  =\t  %d"%((str(i)),(i)))
