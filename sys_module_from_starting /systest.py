import sys
var =" hey this is jitu yadav" # var is varible and we 
# are going to  get refernce count  becuas it play  an
# important role in  mammory management
print(sys.getrefcount(0)) 
no_of_ref = sys.getrefcount(var)
print(sys.getrefcount(None))
print(" no of ref count  =\t %d "%no_of_ref)