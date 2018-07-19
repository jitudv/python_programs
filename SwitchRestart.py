import sys
def disp():
    print("Enter  one for one ")
    print("Enter  two for two ")
    print("Enter  three for three ")
    print("Enter  four for one ")
    print("Enter  one for four ")
    print("Enter  exit for exit from  program ")
    choice =" "
    choice = str(choice)
    #choice  = input("Enter  your choice ")
    choice =raw_input(" Enter your choice ")
    print("the value of choice  = %s"%choice)
    if choice == 'one':
        print("this is  one ")
        disp()
    elif choice == 'two':
        print("this is two ")
        disp()
    elif choice == 'three':
        print("this is three ")
        disp()
    elif  choice == 'four':
        print("this is four ")
        disp()
    elif choice == 'exit':
        sys.exit()

    else:
        print("no choice match with  your choice ")
        disp()

print("now  call your  disp ")
disp() # usint this function call i will start my switch 