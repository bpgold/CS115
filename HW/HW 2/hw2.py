'''
Created on 10/2/23
@author:   Breona Pizzuta
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."
CS115 - Hw 2
'''
import sys
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    '''takes as input a single letter string called letter and a list where each element in that list is itself a list of the form [character, 
value] where character is a single letter and value is a number associated with that 
letter (scrabble score). The letterScore function then returns a single number, 
namely the value associated with the given letter'''
    
    if scorelist == []:
        return 0 #base
    if scorelist[0][0]== letter:
        return scorelist[0][1] #returns value
    #searches to find letter equal
    return letterScore(letter, scorelist[1:])


def wordScore(S, scorelist):
    '''should take as input a string S and a scorelist in the format 
described above, which will have only lowercase letters, and should return as output the 
scrabble score of that string'''
    if len(S)==0:
        return 0 #base
    #take first letter using letterScore and adds to rest of the values
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)


def removeLetter(letter, scorelist):
    '''removes one letter, to be used when checking if words exist'''
    if scorelist==[]:
        return [] #base
    if scorelist[0]== letter:
        return scorelist[1:] #if match, return rest of letters
    return [scorelist[0]]+ removeLetter(letter, scorelist[1:])#if first doesnt match, keep it and try rest of list.

def isWord(word, scorelist):
    '''word is target word you are looking for. Returns True if word can be formed'''
    if scorelist==[] and len(word)>0: #no more letters in the list, but there are still letters left in the target word
        return False
    elif len(word)==0: #the whole word has been formed
        return True
    if not word[0] in scorelist:
        return False #if the letter is not in the list, word cannot be formed
    return isWord(word[1:], removeLetter(word[0], scorelist))
    
    
'''need to create helper funcs to use the Dictionary within scoreList and bestWord'''


def scoreList(Rack):
    ''' takes as input a Rack which is a list of lower-case letters and returns a 
list of all of the words in the global Dictionary that can be made from those letters and the 
score for each one. Specifically, this function returns a list of lists, each of which contains a 
string that can be made from the Rack and its Scrabble score.'''
    def helperScoreList(Dictionary, Rack):
        if Dictionary== []: #empty dictionary
            return []
        if isWord(Dictionary[0], Rack): #if it can form, creates a list with the word and the score
            return [[Dictionary[0], wordScore(Dictionary[0], scrabbleScores)]] + helperScoreList(Dictionary[1:], Rack)
        else: #continues to check the rest 
            return helperScoreList(Dictionary[1:], Rack) 
    return helperScoreList(Dictionary, Rack)
    

def bestWord(Rack):
    '''takes as input a Rack as above and returns a list with two elements: the 
highest possible scoring word from that Rack followed by its score. If there are ties, they can 
be broken arbitrarily'''
    def helperBestWord(rackScoreList, word):
        if rackScoreList== []: #A list of lists where each element is a word from the Rack and its corresponding Scrabble score.
            return word
        if rackScoreList[0][1]>= word[1]:
        #If the score of the first word is greater than or equal to the score of the current highest-scoring word the continues
            return helperBestWord(rackScoreList[1:],rackScoreList[0])
        else:
        #if its not greater, continue with the word
            return helperBestWord(rackScoreList[1:], word)

    return helperBestWord(scoreList(Rack), ['',0])
    
