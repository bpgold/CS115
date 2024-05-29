'''
Created on 10/19/23
@author:   Breona Pizzuta
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2 !=0
#Base 2 representation of 42 is 101010.
#In an odd base 10 number the least significant bit will be 1 in base 2 because odd numbers have binary representation ending in one.
#In an even base 10 the least significant bit will be 0 in base 2 because even numbers have binary representation ending in zero.
# when we remove the value to the right the number is divided in half.
# if N/2 is even, add 0 and if N/2 is odd, add 1.



def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ""
    elif isOdd(n):
        return numToBinary(int(n/2)) +'1'
    else:
        return numToBinary(int(n/2)) + '0'



def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=="":
        return 0
    return binaryToNum(s[:-1])*2 + int(s[-1])



def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    incremented= binaryToNum(s) + 1 #decimal incremented
    binary= numToBinary(incremented) #back to binary 
    return ("0" * 8 + binary )[-8:] #adds zeros and then take only 8 characters



def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n ==0:
        return #when 0, nothing
    return count(increment(s), n-1)
    


def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ""
    return numToTernary(int(n/3)) + str(n%3) #remainder helps create the string
# ternary representation of 59 would be 20012 because 2*27= 54+ (1*3)= 57+ (2*1)=59.  

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=="":
        return 0
    return ternaryToNum(s[:-1])*3 + int(s[-1])
# same idea as binary but using 3







