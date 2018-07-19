outvar=99090
class Test:
    statvar=94090  #static variable 
    __init__(self,name,lastname ,address , age ):
        global outvar # this  is my global var 
        self.ename =name #ename is  gloabl varibale 
        self.elastaname=lastname
        self.address=address
        self.age =age
    def show(self):
        print("name  = \t %s"%self.ename) 
        print("lastname  = \t  %s"%self.elastaname) 
        print("age = \t %d"%self.age) 
        print("address  is  = \t  %s"%self.address) 
if__name__ =='__main__':
    ob = Test("jitu","amit","khargone",25)
    bo.show()
    print("now we are main block ")