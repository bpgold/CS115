'''
Created on 10/12/23
@author:   Breona Pizzuta
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."
CS115 - Lab 5
'''
import time

words = []
HITS = 10
memo={} #memosation

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    def helperFastED(first, second, mem):
        '''uses memosation'''
        if(first, second) in mem: #if it already exists in memosation
            return mem[(first, second)]
        if first == '':
            end= len(second)
        elif second == '':
            end= len(first)
        elif first[0] == second[0]:
            end= fastED(first[1:], second[1:]) #recusive call 
        else:
            # same as normal, just add the memosation
            substitution = 1 + helperFastED(first[1:], second[1:], mem)
            deletion = 1 + helperFastED(first[1:], second, mem)
            insertion = 1 + helperFastED(first, second[1:], mem)
            end= min(substitution, deletion, insertion) #min is the smallest edit dist
        mem[(first, second)] = end
        return end
    return helperFastED(first, second, memo)


        
def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return list(map(lambda x:(fastED(user_input,x), x),words))
               


def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
