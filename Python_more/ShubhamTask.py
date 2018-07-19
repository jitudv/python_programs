print("this  is my string count job ")
data =""" hii this this jitu yadav from 
khargone and jitu is  python developer
some time ago he is working on android 
but after some time jitu switched on data science"""
def addword(word):
    dict=dict()
    list =list()
    count=0
    
    

wordlist = list();
counter = 0
for line in data.splitlines():
    print(line)
    print("******* ")
    for word in line.split():
        global counter
        counter =0
        print(" my word is   = \t  %s"%word)
        for c in word:
            global wordlist
            wordlist.append(c)
            print(c)
print("we are at 0 ident ")
print(wordlist)