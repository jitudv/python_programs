dict = dict()
i = list()
dict ={"empname":"jitu",
 "empid":"123dev",
 "empadd":"khargone",
 "emp_exper":["ssi","javapoint","programers"],
 "empsal":1525252}
print(" this  si value of key %s and value = \t %s \n"%("empname",dict.get("empname")))

if dict.has_key("empname"):
    print("yes we have ")
else:
    print("we dont have ")
print("now  we are at 0 indent ")
i = dict.keys
print(type(i))
for  l in i:
    print(dict.get(l))
