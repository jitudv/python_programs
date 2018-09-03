
import re 
import sys 
import os 

print("this is regular expression ")

data = 
""" jitudv09@gmail.com  Matches the end of the string or 
just before the newline at the end of the string, 
and in MULTILINE mode also matches before a newline. 
foo matches both ‘foo’ and ‘foobar’, while the regular 
expression foo$matches only ‘foo’. More interestingly, 
searching for foo.$ in 'foo1\nfoo2\n' matches ‘foo2’ 
normally, but ‘foo1’ in MULTILINE mode; searching for 
a single $ in 'foo\n' will find two (empty) matches:

one just before the newline, and one at the end of the string"""

robject  = re.compile(r'[^@]+@[^@]+\.[^@]+')
if robject != None:
    print("yes your expression is right ")
else:
    print(" your expressio does not right ")
sobject = re.search(robject,data)
if sobject != None:
    print("yes  you fond  \t "+str(sobject))
else:
    print(" your dont have this  type of string ")



