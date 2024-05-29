############################################################
# Name: Breona Pizzuta
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
# CS115 Lab 3
#  
############################################################

''' Given an amount of money and a list of coin types, find the least 
number of coins that makes up that amount of money. '''
def change(amount, coins):
    if amount==0:
        return 0 #base case
    
    elif coins==[]:
        return float("inf")
    
    elif coins[0]> amount:
        return change(amount, coins[1:])
    
    else:
        use_it= 1+ change(amount-coins[0], coins)# saying you used 1 coin, keeps
        lose_it= change(amount, coins[1:]) #drops it
        return min(use_it, lose_it) 
        
