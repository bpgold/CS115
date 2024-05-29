############################################################
# Name: Breona Pizzuta
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System.”
# CS115 Lab 1
#  
############################################################

def same(word):
    '''Docstring- Checks if a string has the same first and last letters, not case sensitive. '''
    return word[0].lower() == word[-1].lower()
        
    
    
    
    
def consecutiveSum(x, y):
    '''Docstring- Finds the sum of consecutive integers between two numbers, x and y.'''
    return ((x+y)/2)* (y-x-1)
