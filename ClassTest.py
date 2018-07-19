import constant
outvar=99090
class Test:
    constant.MAXVALUE=1000 # this is constant 
    statvar=94090  #static variable 
    def __init__(self,name,lastname ,address , age ):
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
if __name__ =='__main__':
    ob = Test("jitu","amit","khargone",25)
    secob = Test("amit","yadav","indore ",23)
    ob.outvar =909090
    print("this is my our var   = \t  %d"%ob.outvar)
    secob.outvar=75874787 
    ob.show()
    secob.show()
    secob.MAXVALUE=67676767
    print("this is constant value = \t %d"%secob.MAXVALUE)
    print("now we are main block ")