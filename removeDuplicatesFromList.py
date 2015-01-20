#! /usr/bin/python
from collections import OrderedDict
lst = list(range(1,10))
lst1=list(range(1,20))
lst2=list(range(1,30))

lst += lst1 +lst2
print(lst)

#######
uniqueListUsingDict = OrderedDict.fromkeys(lst)
#######
uniqueListUsingSet = set(lst)
print(uniqueListUsingSet)

####### Traditional Logic with set
seen = set()
for i in lst:
    if i not in seen:
        seen.add(i)

print(seen)

