print("this is my bitwise test operator ")
no  =10;
# 000001010 
no = no>>2
print(' this is the value of  after = \t  %d'%no)
no  = no<<5
print(' this is the value of  after = \t  %d'%no)
no=~no
print("this is my no  = \t %d"%no)
no =10 
no1  =8
res  = no^no1
print(" this the  value of res  = \t  %d"%res)
res = no | no1
print("this is the  result  || op = \t  %d"%res)
res = no & no1
print("this is the  result  & op = \t  %d"%res)