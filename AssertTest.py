print(" this is exceptional check code ")
name ='jitu yadav '
try :
    print("name is = \t  %s"%name)
except(NameError,IOError,FloatingPointError) as e:
    print("this is the error = \t "+str(e))
else:
    print("now exception is  catch ")
finally:
    print("this is will excute  at least one time ")
age =int(input("Enter your age  = \t "))
if(age<18):
    raise ArithmeticError("are you not elgible ")
else:
    print("yes are your aligible ")