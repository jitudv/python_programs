print("this is  my opps programm ")
class Emp:
    @staticmethod
    def hello(): # it is a method 
        print("hello")
    orgid =90909 # this is static  variable 
    def __init__(self,name,lastname,address,mobno, salary):
        self.ename=name
        #ename is global class variable 
        self.elastname =lastname
        self.eaddress =address
        self.emobno=mobno
        self.esalary =salary
    
    def getEname(self):
        return self.ename
    # getter method  this will return your string 
   
    def setEname(self,name):
        self.ename=name
    # this is my setter method  this  will return None 
    
    def showData(self):
        print("ename is  = \t  %s"%(self.ename))
        print("elastname is  = \t  %s"%(self.elastname))
        print("eaddress is  = \t  %s"%(self.eaddress))
        print("mobno is  = \t  %d"%(self.emobno))
        print("salary is =\t %d"%(self.esalary))
print(" now we at 0 ident ")
emp1 = Emp("amitansh","verma","indore",7566447017,15000)
emp1.showData() # this will show your data of  object emp1 
emp2 = Emp("jitu","yadav","khargone",254452545,125000)
emp2.showData() # this is my emp2s data 
emp3 = Emp("shubham","kanungo","barwani",3935854552,150500)
emp3.showData() # this si my emp3s data 
sal = emp2.getEname() # value of sal  to be jitu 
print("sal = \t  %s"%(sal))
print(emp2.getEname())
Emp.hello()
Emp.orgid

