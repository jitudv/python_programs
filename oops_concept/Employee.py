class Employee:
    def __init__(self,name,salary,id):
        # this is my costructor 
        self.ename =name
        self.esalary = salary
        self.eid =id
    def etex(self,salary):
        #it will calculated text of employee
        tax =((salary*10)/100)
        return tax
        #global member  always access with object 
# class body end 
emp1  = Employee("jitu",25000,"dev101")
ctax = emp1.etex(emp1.esalary)
print("salary of employee %s is  = \t  %d"%(emp1.eid,ctax))
emp2  = Employee("amit",50000,"dev102")
ctax = emp1.etex(emp1.esalary)
print(" salary of employee %s is  = \t  %d"%(emp2.eid,ctax))