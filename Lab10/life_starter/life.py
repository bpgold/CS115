#
# life.py - Game of Life lab
# Lab 10- 11/16/23
# Name: Breona Pizzuta
# Pledge: " I pledge my honor that I have abided by the Stevens Honor System."
#

import sys
import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row


def createBoard(width, height):
 """ returns a 2d array with "height" rows and "width" cols """
 A = []
 for row in range(height):
     A += [createOneRow(width)] # What do you need to add a whole row here?
 return A


def printBoard( A ):
 """ this function prints the 2d list-of-lists
 A without spaces (using sys.stdout.write)"""
 for row in A:
     for col in row:
         sys.stdout.write( str(col) )
     sys.stdout.write( '\n' )


def diagonalize(width,height):
 """ creates an empty board and then modifies it
 so that it has a diagonal strip of "on" cells."""
 A = createBoard( width, height )
 
 for row in range(height):
     for col in range(width):
         if row == col:
             A[row][col] = 1
         else:
             A[row][col] = 0 
 return A


def innerCells(w,h):
    """returns a 2d array of all live cells- with the value of 1-
    except for a one-cell-wide border of empty cells around the edge"""
    A=createBoard(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
          A[row][col] = 1
    return A

def randomCells(w,h):
    """ returns an array of randomly-assigned 1's and 0's
except that the outer edge of the array is still completely
empty (all 0's) as in the case ofinnerCells"""
    A=createBoard(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
          A[row][col] = random.choice([0,1]) #same as inner but now choice between 0 and 1
    return A

def copy(A):
    """ will take in a 2d array A and it will output a new 2d array of
data that has the same pattern as the input array. """ 
    height = len(A)#rows
    width = len(A[0])#cols
    copyOfBoard = createBoard(width, height)
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            copyOfBoard[row][col] = A[row][col]
    return copyOfBoard


def innerReverse(A):
    """takes an old 2d array, creates a new generation of the same shape and
size. New generation should be the "opposite" of A's cells everywhere except
on the outer edge (like innerCells). However, for inner cells
- those not on the edge - where A[row][col] is a 1, the new array's value will 
be a 0 - and vice versa."""
    height = len(A)#rows
    width = len(A[0])#cols
    copyOfBoard = createBoard(width, height)
    #my idea is to use the base of copy but then inverse the insides.
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            copyOfBoard[row][col] = 1- A[row][col]
    return copyOfBoard


def countNeighbors(row, col, A):
    """that returns the number of live neighbors
for a cell in the board A at a particular row and col"""
    neighbor=0
    #3x3 check
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
          if A[i][j] == 1:
            if i == row and j == col:
              neighbor += 0
            else:
              neighbor += 1

    return neighbor



def next_life_generation( A ):
    """ makes a copy of A and then advanced one generation of Conway's
game of life within the *inner cells* of that copy. The outer
edge always stays 0. """
    height = len(A)#rows
    width = len(A[0])#cols
    newA = copy(A)
    count=0
    for row in range(1, height - 1):
        for col in range(1, width - 1):
          count = countNeighbors(row, col, A)
          if count < 2: #A cell that has fewer than two live neighbors dies
            newA[row][col] = 0
          elif count > 3: #A cell that has more than 3 live neighbors dies
            newA[row][col] = 0
          elif count == 3 and A[row][col] == 0:
              #A cell that is dead and has exactly 3 live neighbors comes to life
            newA[row][col] = 1
          else: #All other cells maintain their state
            newA[row][col] = A[row][col]
  
    return newA
    
