print(" this is dictionary test programm ")
dict ={
    "name":"amit",
    "lastname":"yadav", "address":"khargone","id":125232,
    "salary":252525,"designaation":"developer",
    "joiningdate":"12/25/18"
}
print(dict)
list = dict.keys()
print(" this is the keys os list  = \t %s "%list)
for i in list:
    print("key  %s \t have value  %s"%(i,dict[i]))
print("\n  we are at 0  ident ")

