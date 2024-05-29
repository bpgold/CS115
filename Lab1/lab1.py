############################################################
# Name: Breona Pizzuta
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
# CS115 Lab 1
#  
############################################################

from math import factorial
from functools import reduce

def add(x, y):
    '''returns x + y '''
    return x + y

def inverse(x):
    '''Takes a number n as input and returns its reciprocal. This function should always return a floating point number, even if the input is an integer.  '''
    return float(1/x)

def e(n):
    '''Approximates the mathematical value e using a Taylor expansion. e can be expressed as the sum 1 + 1/1! + 1/2! + 1/3! + ... We'll approximate e by adding up just the first n terms of this sequence (after the leading 1) where n is some positive integer provided by the user.'''
    list= range(1, n+1)
    newList= map(factorial, list)
    newList2= map(inverse, newList)
    return 1 + reduce(add, newList2)
    
    


