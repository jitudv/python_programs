class MyException(Exception):
    def __init__(self,arg="get out "):
        self.msg =arg

age = int(input("Enter  your age  \t "))
if age>=18:
    print("wel-come sir ")
else:
    try:
        raise MyException()
    except MyException as e:
        print(e.msg)

print("we are at the end ")

