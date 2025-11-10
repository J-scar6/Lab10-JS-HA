"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a==0:
        raise ZeroDivisionError ("Can't divide by zero")
    else:
        return b/a

def log(a,b):
    if a<=0:
        raise ValueError ("a has to be positive")
    if b<=0 or b==1:
        raise ValueError ("b has to be positive and can't be 1")
    return math.log(b,a)

def exp(a,b):
    return a**b






