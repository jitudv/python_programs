print("this is exception handling ")
def devno(no,dno):
    return no//dno
try:
    print(" call divide zero  \t  %d"%(devno(10,2)))
    print("this is name error  = \t %s"%(name))
    try:
        print("Inner try")
        try:
            print("inner most try")
        except:
            print("innner most except ")
    except:
        Print("Inner Except")
except(NameError,ZeroDivisionError) as (e):
    print("error is \t  {0}  occured  and  ".format(e))
else:
    print(" this is my else part ")
finally:
    try:
        print("this is finnaly ")
    except:
        print("this finnnaly block except ")
    print("this is finnaly block statement ")
print("we are ate the end ")