# https://github.com/J-scar6/Lab10-JS-HA
# Partner 1: Jack Scarlett
# Partner 2: Hanan Alaiti

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError

def hypotenuse(a, b):
    return math.hypot(a, b)

# First example
def add(a, b): 
    return a+b

def subtract(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a==0:
        raise ZeroDivisionError ("Can't divide by zero")
    else:
        return b/a

def logarithm(a,b):
    if a<=0:
        raise ValueError ("a has to be positive")
    if b<=0 or b==1:
        raise ValueError ("b has to be positive and can't be 1")
    return math.log(b,a)

def exp(a,b):
    return a**b



