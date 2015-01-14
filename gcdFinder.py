#! /usr/bin/python
from fractions import gcd

def findGCDFromListOfNumbers(numbersList):
    result = numbersList[0];
    for num in numbersList[1:]:
        result = gcd(result,num)
    return result


numbers = [9,3,15,4,93]
print findGCDFromListOfNumbers(numbers)

numbers = [25,10,15,50,65,75]
print findGCDFromListOfNumbers(numbers)

numbers = [8, 16,4, 2, 20]
print findGCDFromListOfNumbers(numbers)

numbers = [9,3,15,21,93]
print findGCDFromListOfNumbers(numbers) 

numbers = [112, 160, 180, 240, 288, 32, 480, 96, 60, 72]
print findGCDFromListOfNumbers(numbers) 
