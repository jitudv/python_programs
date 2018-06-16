print("this is my dictionary test programm ")
dict  =dict()
# this is my empty dictionary 
dict={"name":"jitu","lastname":"yadav","address":"khargene","compname":"ssi"}
print("this  is the name of = \t  %s"%dict["name"])
print("we are at 0 ident ")
keylist =dict.keys()
#now  key list have the list of all  keys of dictonary 
for i in keylist:
    print(" values of dictionary  = \t %s \t associat with key \t  %s"%(dict[i],i))
print("this is my  0 ident ")
dict1 ={
    "names":["jitu ",'vikash',"amit","ranu",'shubham '],
    "lastname":["yadav","sharma","verma","rathod","sibngh"],
    "address":["khargone","badwani","jhabua","alirajpur"]
    }
listkyes=dict1.keys()
for j in listkyes:
    #print(dict1[j])
    if type(keylist) is type(dict1[j]):
        for m in list(dict[j]):
       
        #print(m)
    print(" this is  at 0 ident ")
