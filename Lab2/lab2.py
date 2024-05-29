############################################################
# Name: Breona Pizzuta
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
# CS115 Lab 2
#  
############################################################

def dot(L, K):
    """ Output the dot product of the lists L and K."""
    if L==[]: # if empty
        return 0.0
    if K==[]: #if empty
        return 0.0
    else:
        return L[0]* K[0]+ dot(L[1:],K[1:])
    #always do the first two- [0] and contine with the list [1:]

    
def explode(S):
    """ Take a string S as input and should return a list of the characters (each of 
which is a string of length 1) in that string. """
    if S== "": #empty string
        return []
    else:
        return [S[0]]+ explode(S[1:]) #take list of first letter and continue with list [1:]

def ind(e, L):
    """ Return the index at which e is first found in L."""
    if L==[] or L== "":
        return 0 #meaning it is empty

    elif e==L[0]: # if e is first
        return 0
    else: 
        rec= ind(e, L[1:])
        return 1+rec

def removeAll(e, L):
    """Returns another list that is identical to L except that all elements identical to e have been removed. Notice 
that e has to be a top-level element to be removed"""
    if L == []: #if empty 
        return []
    if L[0]==e: #if first is =, remove
        return removeAll(e, L[1:])
    else:
        return [L[0]]+ removeAll(e, L[1:])
  

def even(X):
    if X % 2 == 0 :
        return True
    else:
        return False

def myFilter(f,L):
    """Returns a new list that contains all of the elements of L for which the predicate returns True (in the same order as in the 
original list L)"""
    if L== []: #if empty 
        return []
    if f(L[0])==True:
        return [L[0]] + myFilter(f, L[1:])
    else:
        return  myFilter(f, L[1:])


def deepReverse(L):
    """Returns the reversal of the list where, additionally, any element that is 
a list is also deepReversed."""
    if L== []: #if L is empty 
        return []
    if isinstance(L[0], list): #if True you will end up here
     return deepReverse(L[1:]) + [deepReverse(L[0])]
    else: #if False you will end up here
     return deepReverse(L[1:])+[L[0]]
    
