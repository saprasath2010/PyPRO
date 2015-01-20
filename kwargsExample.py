#! /usr/bin/python

def defaultArgs( a,b,x=5,y=6):
    print(a,b,x,y)

print("C++ equal Default Args...")
defaultArgs(1,2)

def readArgsDynamically( *args):
    for i in args:
        print(i)

print("C++ equal Default Args...")
readArgsDynamically(1,2)


def myfunc(**kwargs):
    # kwargs is a dictionary.
    for k,v in kwargs.items():
         print("%s = %s" % (k, v))

myfunc(key1="val1",key2="val2")

def myfunc2(*args, **kwargs):
   for a in args:
       print("ARGS",a)
   for k,v in kwargs.items():
       print("KEY: %s = VAL:%s" % (k, v))

myfunc2(1, 2, 3, banan=123,newkey="ARUN")