print(" this is my function test program")
def hello():
    print(" this  hello funtion ")
def add(var ,var1):
    print(" it will return  addition of two variables ")
    return var+var1
print(" now function calling ")
print(" this is my addtion   = \t %d"%add(90,90))
hello()
def msg(msg):
    print(msg)
msg("his kjsfjsdkjsklj ksdfksklj sfjksjfls fkdsjflks kskdjfk skkfdjkj dkfsjjfs ksfkljs jklfjs ")
msg(1232)
def seriseadd(*var):
    global res
    res=0
    for i in var:
        res  = int(res)+int(i)
    return res
print(" this is my serise add function ")
res =seriseadd(12,252,1252,1225,212,5212,5212,5212,212,521,2,52,2,2,2,12,1,2,12)
print(" %d  \t the  value of res "%res)
def facto(var):
    if(facto(var)<1):
        print("%d"%1)
    return facto*facto(var=var-1)
print(" this is my factorial  = %d"%facto(5))

