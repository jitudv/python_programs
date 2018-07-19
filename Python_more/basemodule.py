import moduleTest as mod 
from  module2 import add,mul,div 
print("this is our basemodule ")
mod.hello()
mod.hii()
mod.go()
adres = add(12,12)
dres = div(12,3)
mres = mul(12,3)
print("this  addres = \t %d"%adres)
print(" this is  divide  =\t %d"%dres)
print(" this multiplication  = \t  %d"%mres)
if __name__ == '__main__':
  print(" this my executable code ")
