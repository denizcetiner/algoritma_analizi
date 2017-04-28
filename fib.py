# -*- coding: utf-8 -*-
"""
Created on Thu May  4 08:43:44 2017

@author: BM
"""

FibArray = [0,1]


def fibonacci_dynamic(n):
    if n<0:
        print("Incorrect input")
    elif n<=len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci_dynamic(n-1)+fibonacci_dynamic(n-2)
        FibArray.append(temp_fib)
        return temp_fib


print(fibonacci_dynamic(9))

def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
 
print(Fibonacci(9))
