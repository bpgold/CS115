'''
Created on 10/23/23
@author: Breona Pizzuta
Pledge: "I pledge my honor that I have abided by the Stevens Honor System."

CS115 - Hw 4
'''

#Task 1

def pascal_add(row):
    ''' outputs the list of elements of a certain row.'''
    if len(row) <= 1:
        return [] #base
    return [row[0] + row[1]] + pascal_add(row[1:]) #takes first two and adds in rest

def pascal_helper(n, row):
    '''finds nth row'''
    if n == 0:
        return row # when n=0 we reached the end
    return pascal_helper(n - 1, [1] + pascal_add(row) + [1]) #calcs current row based on row above
    #new row is taking what we have and the [1] are added to front and end.
    
def pascal_row(n):
    '''    outputs the list of elements of a certain row.'''
    return pascal_helper(n, [1])
    # have to call the helper with row 1
    


#Task 2
def pascal_triangle(n):
    '''returns a list of lists containing the values of the all the rows up to and including row n.'''
    if n<0:
        return []
    return pascal_triangle(n-1) +[pascal_row(n)] #makes one list


#Task 3
def test_pascal_row():
    ''' tests fuction'''
    assert pascal_row(0)==[1]
    assert pascal_row(1)==[1,1]
    assert pascal_row(2)==[1,2,1]
    assert pascal_row(5)== [1,5,10,10,5,1]

def test_pascal_triangle():
    '''tests function'''
    assert pascal_triangle(0)==[[1]]
    assert pascal_triangle(1)==[[1], [1,1]]
    assert pascal_triangle(2)== [[1],[1,1],[1,2,1]]
    assert pascal_triangle(5)==[[1],[1,1],[1,2,1], [1,3,3,1], [1,4,6,4,1], [1,5,10,10,5,1]]

    
