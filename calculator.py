"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#https://github.com/J-scar6/Lab10-JS-HA.git
#Partner 1: Jack Scarlett
#Partner 2: Hanan Alaiti
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
    if b==0:
        raise ZeroDivisionError ("Can't divide by zero")
    else:
        return b/a

def logarithm(a,b):
    if a<=0 or a==1:
        raise ValueError ("a has to be positive and can't be 1")
    if b<=0:
        raise ValueError ("b has to be positive")
    return math.log(b,a)

def exp(a,b):
    return a**b



