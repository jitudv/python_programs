print("oops first ")
class Student:
    school_id="sc1235"
    # this is my static variable 
    def __init__(self,name=None,lastname=None,address=None):
        self.sname=name
        self.slastname =lastname
        self.saddress =address
    def getsname(self):
        return self.sname
        #sname is global variable 
    def getlastname(self):
        return self.slastname
    def getaddress(self):
        return self.saddress
    def (data1,date2):
        return data1+data2
stud1 = Student("amit","yadav","khargone")
print("name of the student %s "%(stud1.getsname()))
print("lastname %s"%(stud1.getlastname()))
print("address = \t %s"%(stud1.getaddress()))
print("school id is  = \t %s "%(Student.school_id))
stud2 = Student("sumit","sharma","indore ")
print("name of the student %s "%(stud2.getsname()))
print("lastname %s"%(stud2.getlastname()))
print("address = \t %s"%(stud2.getaddress()))
print("school id is  = \t %s "%(Student.school_id))
stud3 = Student()
#this  is my emtpy objet 
stud3.sname="rajesh"
print("name is for stud3 = \t %s"%(stud3.getsname()))
