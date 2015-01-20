#! /usr/bin/python
import functools

def fun(x,y):
    return x+y

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]


print(list(filter(lambda x: x % 3 == 0, foo)))


print(list(map(lambda x: x * 2 + 10, foo)))

# will generate one output by keep on go on to other parameters
print(functools.reduce(lambda x,y: x+y ,range(10)))
