############################################################
# Name: Breona Pizzuta
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
# CS115 Lab 4
#  
############################################################
'''similar to original knapsack, but we want to return the value and the items we are taking'''

def knapsack(capacity, itemsList):
    ''' The first number in each of the pairs represents the weight of the item. The second number in each pair 
represents the value of the item. Returns both the maximum value and the list of items that make this value, without exceeding 
the capacity of your knapsack. '''
    if capacity<=0 or itemsList ==[]:
        return [0,[]]

    elif itemsList[0][0]> capacity:
        #first item does not fit.
        return knapsack(capacity, itemsList[1:])

    else:
        use_it = knapsack(capacity - itemsList[0][0], itemsList[1:]) #keep item, go to next
        
        lose_it = knapsack(capacity, itemsList[1:]) #drop the item

        #still part of the else
        if  itemsList[0][1] + use_it[0] > lose_it[0]: #determines if use it is max 
            return [itemsList[0][1] + use_it[0]] + [[itemsList[0]] + use_it[1]]
            # new list, combines item val with use it and the item with use it. basiclly max and the rest of the list
        else:
            return [lose_it[0]] + [lose_it[1]]
            #takes max in lose it if it is greater, basically same as returning lose it 
        
