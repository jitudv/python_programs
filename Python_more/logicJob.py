print("this is logical task for amitansh ")
data  =""" hii this Is jitu yadav From khargone
and Jitu is a Software developer """

# first task we must have to break it into words 
list = list() 
# this is my empty list 

for w in data.split(" "):
    #print(w)
    for c in w:
        #print(c)
        if c.isupper():
            list.clear()
            #all list remove
            list.append(c)
            for uc in w:
                print("")
                list.clear()
                if uc.isupper():
                    list.append(uc)
                else:
                    list.append(uc)
    print("list is = \t %s"%(str(list)))


print("now we are at the end of the programm ")
