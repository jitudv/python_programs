print("this  test programm ")
glob_var = "create first "
def hello():
    global glob_var
    glob_var = "this is global varibals"
    local_var="this is localvariable "
    nonLocalvar  = " "
    
    def hii():
        local_var=" this is hii localvar "
        nonlocal nonLocalvar 
        nonLocalvar =" use between hello to  hii scope "
    hii() # this is hii function 
    print("\n\n this is my non local variable = \t %s \n\n"%(nonLocalvar))
print("\n\n now call your code  \n\n")
if __name__ =='__main__':
    hello()
    print(" \n\n this is my globla variable \t  %s \n\n"%(glob_var))