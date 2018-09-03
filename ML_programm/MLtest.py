import pandas as pd 
import numpy as np 
import sklearn as skl

print("yes we have all of the that ")
list =[x+1   for x in range(10)]
print(list)
array = np.array([12,25,28,452,525,52,85,6,98,685,75],[45,857,58,57,558,545,85,25,25,452,5,25])
absvalue  = np.abs(array)
avarage = np.average(array)
print(absvalue)
maxvalue= np.max(array)
minvalue = np.min(array)
print(array[:3])  # it will slice the data 
print(array[1:5:4])
print("this is  min  value  = \t  %d"%minvalue)
print("this is max value = \t  %d"%maxvalue)
print(" this is avrage value  %f"%avarage)
print(array)