############################################################
# Name: Breona Pizzuta
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System.”
# CS115 HW 1
#  
############################################################

from functools import reduce

def mult(x, y):
 """Returns the product of x and y"""
 return x * y

def factorial(n):
    """ Takes a positive integer n and returns n!, aka returns the factorial which is the product of an integer and all the integers below it. """
    return reduce(mult, range(1, n+1))

def sum(one,two):
    """ returns the sum of one and two"""
    return one + two

def mean(L):
    """ Takes a list as input and returns the mean (average) value in that list """
    length= len(L)
    return (reduce(sum,(L)))/length
    
