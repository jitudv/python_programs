from recursionTest import TesPro ,var
print(" this is default  argument test pro ")
def show( msg='this is show default value '):
    print("%s"%msg)
def msg(msg1):
    print("%s"%msg1)
print("now this is call of function ")
show()
msg(" this  is msg  argment pas by us  ")
show("agrumetn replace with defaunt argument ")
var =0
def globvar():
    global var
    var=var+10
    print("%d"%var)
print(" var at 0 ident %d "%var)
globvar()
TesPro()