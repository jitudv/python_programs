print("this is function test programm \n  ")

def hell():
    print("\t hello \n ")
print("now  we are call our hello function ")
hell()
print("we ar after hello  \n")
def per(balance , time , rate):
    res = ((balance*time*rate)/100)
    return res
balance = int(input("Enter the balance  \t "))
rate = int(input("Enter rate  =\t "))
time =int(input("Enter time "))
print(" this  is my result of simle interest  = \t %d"%per(balance,time,rate))
print("now we are  at 0 ident ")

def pers(balance , time , rate):
    print(" simple intrest  =\t %d "%((balance*rate*time)/100))
print("now we are call pers  ")
pers(1200,2,10)
 
def seradd(*a):
    res =0
    for i in a:
        res =res+i
    return res

print(" this is my serise addtion  = \t %d"%seradd( ))
