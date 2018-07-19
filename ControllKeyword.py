print("controll keyword check")
for i in range(10):
    if i == 5:
        continue
    print(" this is i = \t %d"%i)
print("now we are at  main block ")
def hello():
    pass
    #this is my hello block 
print("this is my main block ")   
if True:
    if True:
        if True:
            if True:
                if True:
                    print(" this  inner most blok ")
                    #break
                    
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass
else:
    pass
print("now are again in main  block ")   
for j in range(20):
    if j <= 10:
        if j == 5:
            print("this is the value of j= \t %d"%j)
            break
        else:
            pass
    else:
        pass
print("this is main block  at the end ")