print("thi is my  if test  ")
no = int(input(" Enter  an no "))
no1 = int(input(" Enter  an no1 "))
no2 = int(input(" Enter  an no2 "))

if no< no2 and no <no1:
    print("no smallest from both ")
elif no1 <no and no1 <no2:
    print("no1 is smallesst  from both ")
elif  no2 < no and no2 <no1:
    print("no2 is smallesst no from both ")
print("now we are  ate  0 indent ")

if no <no2:
    if no<no1:
        print("yes no is less then  both ")
    else:
        if no1 <no:
            if no1 <no2:
                print(" ys no1 ia less then both ")
            else:
                if no2 <no :
                    if no2< no1:
                        print(" yes no2 is  smallest form both ")
                    else:
                        print("both condition is false ") 
                else:
                    print("condition false")
else:
    print("condition false ")