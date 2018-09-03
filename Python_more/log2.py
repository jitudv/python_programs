line="""hiiii This Is aAmIt VerMa fRom Indore"""
list=list()
for w in line.split(" "):
    for c in w:
        if c.islower():
            list.append(c)
        else:
            print(str(list)+"\n")
            list.clear()
            list.append(c)
