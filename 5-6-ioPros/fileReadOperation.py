print("this is file read ")
file = None
try:
     #file  = open("/home/jays/Desktop/Abhishek/jitu.txt",'r+')
    with open("/home/jays/Desktop/Abhishek/jitu.txt", 'rb') as f:
        contents = f.read()
        data = contents.decode('ascii')
        print(contents)
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
