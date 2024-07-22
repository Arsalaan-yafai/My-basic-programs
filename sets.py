"""
from typing import Set, Any

s: set[Any]= set()
l= [1,2,3,4,5,6,7,8,9,10]
s= set(l)
s2 = ()
l2= [2,4,7,4,1,11,44,67]
s2= set(l2)
#print(s,s2.union())
#print(s,s2.intersection())
#s2.intersection(s)
print(s2)
s2.intersection(s2)
print(s2)
"""
l1= [12,2,3,4,5,6,7,8,1,2,99, "arsalaan"]
for item in l1:
    if str(item).isnumeric() and item>2:
        print(item)