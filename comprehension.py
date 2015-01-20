#! /usr/bin/python
import collections
import functools
S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
print(S); print (V); print(M)

list = [1,2,3,4,5,6,7,8,9,10]

for i in list:
    print(i,end='')

print("")
# now if we want to multiply the list by val 2 and store it in new list using comprehension


powertwo= [2*x for x in range(0,15,1)]
print("multiplication by 2 all elements:",powertwo)


# with additional operation
newlist = [2*x for x in range(0,15,1) if x%2 == 0]
print("Just skip all even values:",newlist)

#
#noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print(primes)

# make combinations of two array elements
print([(x, y) for x in [1,2,3] for y in [4,5,6] if x != y])

## map lambda
g = lambda x: x**2
print(g(10))
#squares = map(lambda x: print(x**2), range(10))
#print(squares)

def make_incrementor(n): return lambda x: x + n
print(make_incrementor(22)(33))
