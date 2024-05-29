'''
Created on 11/6/23
@author:   Breona Pizzuta
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.


#numToBinary and binaryToNum from lab 6
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2 !=0

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


#Actual assignment below

compressedImage= ''

def compress(S):
    '''that takes a binary string S of length 64 as input and 
returns another binary string as output. The output binary string should be
a run-length encoding of the input string. '''
    global compressedImage #declared as global so it can be used throughout
    compressAllBlocks(S) #Called by itself since compressedImage is ouside so its global
    if S[0] == "1": #run-length strings start with number of consecutive  0s
        compressedImage = ('0' * COMPRESSED_BLOCK_SIZE) + compressedImage
        outputCompressedImage = compressedImage #Stores the compressed image
        compressedImage = '' #global resets
        return outputCompressedImage
    else:
        outputCompressedImage = compressedImage
        compressedImage = ''
        return outputCompressedImage


def compressAllBlocks(S):
    '''Compresses all blocks in input string S, and updates the compressedImage accordingly until completion.'''
    global compressedImage
    if S == "":
        return 0
    else:
        blockLength = compressSingleBlock(S, 1)
        '''Number of consecutive identical bits (length of bit block).
 Counter starts at one bc len of consecutive bits is at least 1'''
        compressedImage= compressedImage + toBinaryString(numToBinary(blockLength)) #Ensures binary strings are added
        return compressAllBlocks(S[blockLength:])


def compressSingleBlock(S, counter):
    '''counts the length of consecutive identical bits.
It returns the length of the consecutive block.'''
    if len(S) == 1:
        return 1
    elif ((S[0] == '1') and ('0' not in S)) or (S[0] == '0') and ('1' not in S):
        #If all bits are the same we should return the length of the string
        return len(S)
    elif S[0] == S[1]: #First two bits are identical we will count
        counter = counter + 1
        return compressSingleBlock(S[1:], counter) #recursive check 
    else:
        return counter #End of consecutive identical bits reached so return length


def toBinaryString(binaryString):
    '''Returns a binary string of a fixed length. '''
    if len(binaryString) == COMPRESSED_BLOCK_SIZE:
        return binaryString
    elif binaryToNum(binaryString) > MAX_RUN_LENGTH:
        #when there are more consecutive bits than one compressed block can represent, this does not specify the number
        binaryString = numToBinary(binaryToNum(binaryString) - MAX_RUN_LENGTH)
        #Get rid of max num of bits one compressed block can represet from the block of identical bits 
        return ('1' * COMPRESSED_BLOCK_SIZE) + ('0' * COMPRESSED_BLOCK_SIZE) + toBinaryString(binaryString)
    #return full block, empty block for other bit, then continue with the original block of consecutive bits
    else:
        binaryString = "0" + binaryString
        return toBinaryString(binaryString)



bitType = 0
#So uncompress knows 0 or 1
uncompressedImage = ''
def uncompress(C):
    '''"inverts" or "undoes" the compressing in your compress function.'''
    global bitType
    global  uncompressedImage
    if C == '':
        bitType = 0   #compressed string starts with 0s. 
        output = uncompressedImage
        uncompressedImage = '' #for global variable
        return output
    else:
        uncompressedImage= uncompressedImage + uncompressSingleBlock(C[0:COMPRESSED_BLOCK_SIZE])
        # only first block
        return uncompress(C[COMPRESSED_BLOCK_SIZE:])# remaining blocks

def uncompressSingleBlock(block):
    '''Converts a compressed binary block into its original binary string from the raw image.'''
    global bitType
    blockLength = binaryToNum(block)
    if bitType == 0:
        bitType = 1 #switches for next 
        return blockLength * '0' #Uncompresses given block
    if bitType == 1:
        bitType = 0
        return blockLength * '1'

def compression(S):
    '''return the ratio of the compressed size to the original size for 
image S.'''
    compressedLength = len(compress(S))
    length = len(S)
    return compressedLength / length



''' tests'''
Penguin= "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
Smile= "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
Five= "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"
test3= "11111111111111111111110000000000000000"
test4= '10' *20

def test(string):
    '''tests'''
    print("Original:",)
    print(string)
    print("Compressed:")
    print(compress(string))
    print("Uncompressed:")
    print(uncompress(compress(string)))
    print("Ratio:")
    print(compression(string))
    assert(uncompress(compress(string)) == string)


'''Comments from doc'''

'''Explain what is the largest number of bits that your compress algorithm could 
possibly use to encode a 64-bit string/image'''
# Since COMPRESSED_BLOCK_SIZE =5, (64 *5)+ 5= 325 bits.  

'''Describe the tests that you conducted and the compression ratios that you found'''
# I tried different tests using the test function above to easily compare the functions.
# I found that the best compression ratios occurred when there were the most consecutive 1s or 0s.
# To  make sure I was correct I created the strings test3 and test4. As I thought, when there is an
#alternating 1s and 0s, the compression ratio will be much worse in comparsion to consecutive 1s and 0s.

'''"I have developed a new image compression algorithm Laicompress(S) that takes a 
64-bit string and always outputs a shorter string that represents that image. That is, every image 
is compressed at least somewhat by my algorithm. Argue to NASA that Professor Lai is Lai-ing—such an algorithm cannot exist!
Try to make your reasoning as convincing and water-tight as possible. (In essence, you are 
proving that such an algorithm cannot exist.'''
# It is known that perfect compression algorithms are not always possible. For a compression algorithm
# to always output shorter string it would need to elimate information, so the compress method
#could not always produce shorter since complexity of the string is different in every problem
#This is just my idea, im not sure if it is 100% correct.

