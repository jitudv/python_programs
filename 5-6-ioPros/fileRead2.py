print("this is file read ")
file = None
try:
     #file  = open("/home/jays/Desktop/Abhishek/jitu.txt",'r+')
    f = open("/home/jays/Desktop/Abhishek/jitu_yadav.txt", 'r')
        #contents = f.read()
    #line = f.readline(100)
    lines = f.readlines()
    for line in lines:
        #print(line)
        for w in line.split(line.upper()):
            print(w)
except IOError as err:
    print("error  is  = \t %s  "%(err))
finally:
    try:
        f.flush()
        f.close()
        if f.closed:
            print("yes your stream is closed properly ")
        else:
            print("your stream does not closed ")
    except IOError as er:
        print("er  = \t  %s "%(er))
print("your file read is end now")
