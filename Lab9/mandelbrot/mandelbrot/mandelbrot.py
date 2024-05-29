# mandelbrot.py
# Lab 9
# Name: Breona Pizzuta
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
# 

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:

def mult( c, n ):
 ''' mult uses only a loop and addition to multiply c by the integer n'''
 result = 0
 for x in range( n ):
     result= result+ c
 return result


def update( c, n ):
    ''' update starts with z=0 and runs z = z**2 + c
for a total of n times. It returns the final z.'''
    z=0
    for x in range(n):
        z=z**2+c
    return z

def inMSet(c,n):
    '''Takes c (complex num)and n as input. Will return boolean, true if
complex number c is in the Mandelbrot set and False otherwise. So False as soon as abs(z)
gets larger than 2, True if abs(z) never gets larger than 2 (for n iterations)  '''
    #c= x+y*1j would assign the variable c to the complex number with real part x and imaginary part y.
    z=0
    for x in range(n):
        z=z**2+c
        if abs(z)>2: #need to check inside loop
            return False
    return True


def weWantThisPixel( col, row ):
    """ a function that returns True if we want
 the pixel at col, row and False otherwise"""
    if col % 10 == 0 or row % 10 == 0:
        return True
    else:
        return False
    
def test():
    """ a function to demonstrate how to create and save a png image"""
    width = 300
    height = 200
    image = PNGImage(width, height)
 # create a loop in order to draw some pixels
 
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
 # we looped through every image pixel; we now write the file
    image.saveFile()


'''in weWantThisPixel
if col % 10 == 0 and row % 10 == 0: will give a dotted grid
to the line
if col % 10 == 0 or row % 10 == 0: will give a grid with lines'''

def scale(pix, pixMax, floatMin, floatMax):
    ''' scale takes in pix, the CURRENT pixel column (or row)
pixMax, the total # of pixel columns floatMin, the min floating-point value
floatMax, the max floating-point value scale returns the floating-point value that
corresponds to pix.
 should use: quantity 1.0*pix / pixMax and quantity floatMax - floatMin in a return'''
    return (pix/pixMax) *(floatMax-floatMin) + floatMin


def mset():
    '''creates a 300x200 image of the Mandelbrot set'''
    width = 300
    height = 200
    image = PNGImage(width, height)
 # create a loop in order to draw some pixels
 
    for col in range(width):
        for row in range(height):
            # here is where you will need
            # to create the complex number, c!
            x= scale(col,width,-2, 1)
            y= scale(row, height, -1,1)
            #-2 with -1 and -1 with -1 based on the limit of the image as described in doc
            c= x+ y*1j
            if inMSet( c, 25 ) == True:
                image.plotPoint(col, row)
 # we looped through every image pixel; we now write the file
    image.saveFile()


     
